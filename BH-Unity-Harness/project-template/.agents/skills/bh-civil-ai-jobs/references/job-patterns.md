# Village job design patterns

All entries below are **design templates**, not verified CIVIL-AI import files. Bind actual actions and filters through installed-version editor/API inspection.

| Job | Candidate CIVIL-AI flow | Ronin economy contract |
|---|---|---|
| Well water | Locate eligible well → interact → collect → carry → Locate destination → Drop Off | reserve source quantity, create cargo, confirm destination credit |
| Fishing | Locate eligible fishing spot → interact → collect → deliver | stock yield, depletion/respawn, tool and season checks |
| Rice farming | Locate assigned field/plot → harvest → haul | crop stage, harvest yield, plot reset and regrowth |
| Porter | Locate specified pickup → Pick Up → Locate specified receiver → Drop Off | order ID, reservations, cargo custody, atomic delivery |
| Cook | Locate kitchen and ingredients → interact at stove → output | ingredient reservation, recipe commit, fuel and capacity |
| Blacksmith | Locate forge, fuel, metal → work actions → finished item | staged recipe, tool requirements, durable output |
| Lumberjack | Locate eligible tree → chop → collect → haul | tree state, log yield, depletion/regrowth |
| Charcoal burner | Locate kiln → load wood → tend → unload | timed conversion, fuel and storage |
| Carpenter | Locate workshop → craft → store | wood inputs, tool and recipe outputs |
| Potter | Locate clay source/kiln → craft → store | clay, water, fuel, fired goods |
| Weaver | Locate loom → weave → store | fiber inputs, cloth outputs |
| Herbalist | Locate eligible plants → collect → store | seasonality, yield and regrowth |
| Builder | Locate work site → fetch materials → build | construction reservation, staged consumption |
| Guard | Locate entrance → Follow Route → Follow Route Reverse | optional patrol alarms; no resource yield |
| Vendor | Move to counter and interact with customers | customer-facing service; distinct from production |

## Shared design requirements
Every job plan must identify: workplace role/job match; valid worker; item names/types; action selection/filter rules; use/interaction spots; navigation mode and reachable goals; work-zone restrictions; tools; stock inputs and outputs; capacity; reservation lifecycle; interruption and cancellation semantics; persistence; concurrency; and failure recovery.

**Nearest target:** Built-in `Locate` searches nearest *matching* item. A depleted resource must be excluded by verified CIVIL-AI requirements or an approved Ronin bridge; otherwise workers may target empty nodes. Explicit delivery orders should target specific producer/consumer instances, not merely nearest item type.

**Transactional rule:** Never credit destination stock merely because `Drop Off` ran. Require confirmed delivery event and exactly-once transaction key. Conservation invariant: available source + reserved source + cargo in transit + destination (plus explicitly consumed/spoiled amounts) reconciles across transitions.
