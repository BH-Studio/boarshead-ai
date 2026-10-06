#requires -Version 5.1
<# Windows entry point. No installation, elevation, or execution-policy changes.
   Example: .\Tools\BH\Invoke-BH.ps1 --root . preflight
   Python 3.11+ is a declared prerequisite, not presumed installed. #>
$ErrorActionPreference = 'Stop'
$entry = Join-Path $PSScriptRoot 'bh.py'
$launcher = Get-Command py -CommandType Application -ErrorAction SilentlyContinue
if ($launcher) {
    & $launcher.Source -3 $entry @args
    exit $LASTEXITCODE
}
$python = Get-Command python -CommandType Application -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Error 'BLOCKED: Python 3.11+ is required. Configure it deliberately; this launcher does not download software.'
    exit 2
}
& $python.Source $entry @args
exit $LASTEXITCODE
