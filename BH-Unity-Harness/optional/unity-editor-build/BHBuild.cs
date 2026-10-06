// Candidate only: Unity compilation/live execution NOT_RUN. Install only by approved local pilot.
// Put in an Editor-only assembly/folder; no runtime inclusion. Does not change target/settings.
#if UNITY_EDITOR
using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Security.Cryptography;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEngine;

namespace BoarsHead.Harness
{
    public static class BHBuild
    {
        [Serializable] private sealed class Artifact { public string path; public string sha256; }
        [Serializable] private sealed class Facts { public int errors; public long total_bytes; }
        [Serializable] private sealed class Result
        {
            public string project_id, task_id, run_id, target, build_result;
            public int errors;
            public Facts observations = new Facts();
            public Artifact[] outputs = Array.Empty<Artifact>();
        }
        private static string Argument(string name)
        {
            var args = Environment.GetCommandLineArgs();
            var matches = Enumerable.Range(0,args.Length).Where(i=>args[i]==name).ToArray();
            if(matches.Length!=1 || matches[0]+1>=args.Length || string.IsNullOrWhiteSpace(args[matches[0]+1]))
                throw new InvalidOperationException("Exactly one value required for " + name);
            return args[matches[0]+1];
        }
        private static void NoLinks(string value)
        {
            var path=Path.GetFullPath(value);
            while(!string.IsNullOrEmpty(path))
            {
                if((File.Exists(path)||Directory.Exists(path)) && (File.GetAttributes(path)&FileAttributes.ReparsePoint)!=0)
                    throw new InvalidOperationException("Linked path rejected: "+path);
                path=Path.GetDirectoryName(path);
            }
        }
        private static string Hash(string path)
        {
            using(var stream=File.OpenRead(path)) using(var sha=SHA256.Create())
                return BitConverter.ToString(sha.ComputeHash(stream)).Replace("-", "").ToLowerInvariant();
        }
        public static void Run()
        {
            // Fail before any build when configuration/ownership arguments are missing.
            if(!Application.isBatchMode) throw new InvalidOperationException("Approved closed-editor batch only");
            var root=Path.GetFullPath(Path.Combine(Application.dataPath,".."));
            var output=Path.GetFullPath(Argument("-bhResult"));
            NoLinks(root); NoLinks(output);
            var allowed=Path.Combine(root,".bh","runs")+Path.DirectorySeparatorChar;
            if(!output.StartsWith(allowed,StringComparison.OrdinalIgnoreCase) || File.Exists(output))
                throw new InvalidOperationException("Result must be a fresh path in .bh/runs");
            var run=Argument("-bhRun");
            var relative=output.Substring(allowed.Length).Split(Path.DirectorySeparatorChar,Path.AltDirectorySeparatorChar);
            if(relative.Length!=3 || relative[0]!=run)
                throw new InvalidOperationException("Expected .bh/runs/<run>/<check>/<result>");
            var targetName=Argument("-bhTarget");
            if(!Enum.TryParse(targetName,out BuildTarget target) || target!=BuildTarget.StandaloneWindows64 || EditorUserBuildSettings.activeBuildTarget!=target)
                throw new InvalidOperationException("Candidate supports already-active StandaloneWindows64 only; no target switching");
            var scenes=EditorBuildSettings.scenes.Where(s=>s.enabled).Select(s=>s.path).ToArray();
            if(scenes.Length==0) throw new InvalidOperationException("No enabled build scenes");
            foreach(var scene in scenes)
            {
                var path=Path.GetFullPath(Path.Combine(root,scene)); NoLinks(path);
                if(!scene.StartsWith("Assets/",StringComparison.Ordinal) || !File.Exists(path) || !path.StartsWith(Path.Combine(root,"Assets")+Path.DirectorySeparatorChar,StringComparison.OrdinalIgnoreCase))
                    throw new InvalidOperationException("Invalid scene path");
            }
            var directory=Path.Combine(Path.GetDirectoryName(output),"player");
            NoLinks(directory);
            if(Directory.Exists(directory)||File.Exists(directory)) throw new InvalidOperationException("Player output must be fresh");
            Directory.CreateDirectory(directory);
            var result=new Result { project_id=Argument("-bhProject"),task_id=Argument("-bhTask"),run_id=run,target=targetName,build_result="Unknown" };
            var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions { scenes=scenes,locationPathName=Path.Combine(directory,"Player.exe"),target=target,options=BuildOptions.None });
            result.build_result=report.summary.result.ToString();
            result.errors=checked((int)report.summary.totalErrors);
            result.observations.errors=result.errors;
            result.observations.total_bytes=checked((long)report.summary.totalSize);
            // Traverse directories without following links. Record every nonempty output by hash.
            var artifacts=new List<Artifact>();
            Action<string> walk=null;
            walk=dir=>{ foreach(var path in Directory.EnumerateFileSystemEntries(dir))
            { NoLinks(path); if(Directory.Exists(path)) walk(path); else if(new FileInfo(path).Length>0)
                artifacts.Add(new Artifact {path=path.Substring(root.Length+1).Replace('\\','/'),sha256=Hash(path)}); } };
            walk(directory); result.outputs=artifacts.ToArray();
            using(var file=new FileStream(output,FileMode.CreateNew,FileAccess.Write))
            using(var writer=new StreamWriter(file,new System.Text.UTF8Encoding(false))) writer.Write(JsonUtility.ToJson(result,true));
            // Result parser, not process exit alone, determines whether the build passed.
            EditorApplication.Exit(0);
        }
    }
}
#endif
