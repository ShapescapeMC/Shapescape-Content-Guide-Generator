<!--
Cover page (full-bleed Oxford Blue).
PRODUCTNAME is substituted by generate_content_guide.py from release.json.
Edit cover-eyebrow / cover-meta strings if needed for your project.
-->
<section class="cover">
  <img class="cover-mark" src="./images/shapescape_logo_on_dark.svg" alt="Shapescape" />
  <p class="cover-eyebrow">Shapescape Studio</p>
  <h1 class="cover-title">PRODUCTNAME</h1>
  <p class="cover-subtitle">Content Guide</p>
  <div class="cover-meta">
    <span>shapescape.com</span>
    <span>Marketplace Submission</span>
  </div>
  <div class="cover-shapes" aria-hidden="true">
    <div class="shape shape-1"></div>
    <div class="shape shape-2"></div>
    <div class="shape shape-3"></div>
    <div class="shape shape-4"></div>
  </div>
</section>

<div style="page-break-after: always;"></div>

<h1 class="title">CONTENTS</h1>

_The purpose of this guide is to provide the reader with all the necessary information to review this product thoroughly._

_The items below are hyperlinks for easy navigation._

- **[Known Issues](#known-issues)**
  - [Assertion Errors](#assertion-errors)
  - [Technical Issues](#technical-issues)
  - [Intentional Design](#intentional-design)
- **[Design](#design)**
    - [Completion Guide](#completion-guide)
    - [Navigation](#navigation)
        - [General](#general)
        - [Key Locations](#key-locations)
        - [Landmarks](#landmarks)
        - [Containers](#containers)
        - [Hidden Content](#hidden-content)
    - [Characters and Villagers](#characters-and-villagers)
    - [Gameplay Elements](#gameplay-elements)
        - [Mechanics](#mechanics)
        - [User Interface](#user-interface)
        - [Added Key Bindings](#added-key-bindings)
- **[Technical Elements](#technical-elements)**
    - [Changes to Minecraft Functionality](#changes-to-minecraft-functionality)
    - [Custom Inventory Items](#custom-inventory-items)
        - [Spawn Eggs](#player-facing-spawn-eggs)
        - [Custom Blocks](#player-facing-custom-blocks)
        - [Regular Items](#player-facing-regular-items)
        - [Spawn Eggs](#non-player-facing-spawn-eggs)
        - [Custom Blocks](#non-player-facing-custom-blocks)
        - [Regular Items](#non-player-facing-regular-items)
    - [Custom Creatures, Entities and Decorations](#custom-creatures-entities-and-decorations)
        - [Player Facing Entities](#player-facing-entities)
        - [Non-Player Facing Entities](#non-player-facing-entities)
    - [Trades](#trades)
    - [Custom Sounds](#custom-sounds)
- **[Changelog](#changelog)**

<div style="page-break-after: always;"></div>

<h1 class="title">KNOWN ISSUES</h1>
This section lists issues that we have identified ourselves but are unable or unwilling to fix ourselves due to a multitude of reasons.

## Assertion Errors
Listed below are all the assertion errors that we have identified ourselves. Assertion errors are non-critical warning messages that highlight parts of the Minecraft code that break due to our product. These errors are not a concern for retail users, as they only occur in the development versions of the game. This information is also useful to QA testers to help identify assertions that are not caused by the ingestion process.

:generate: insert("templates/known_issues/assertion_errors.md")

## Technical Issues
Below is a list of technical issues that we have identified but are unable or unwilling to fix due to a variety of reasons.

:generate: insert("templates/known_issues/technical_issues.md")

## Intentional Design
Listed below are intentional design decisions that may not be clear enough when testing the product.

:generate: insert("templates/known_issues/intentional_design.md")


<h1 class="title">DESIGN</h1>
_This section contains all the relevant information that the user needs to successfully complete the product._


## World Settings
This section lists the intended world settings.
:generate: insert("templates/world_settings.md")


## Completion Guide
:generate: completion_guide("completion_guide/*.mcfunction")


## Navigation
### General
:generate: insert("templates/navigation_general.md")

### Key Locations
:generate: warp("warp/key_locations/*.mcfunction")

### Landmarks
:generate: warp("warp/landmarks/*.mcfunction")

### Containers
:generate: insert("templates/containers.md")

### Hidden Content
:generate: insert("templates/hidden_content.md")

## Characters and Villagers
**Characters**

Every entity relevant to the story:

:generate: summarize_entities_in_tables("**/*.json", null, ["character"])

**Villagers**

Every entity used for trading:

:generate: summarize_entities_in_tables("**/*.json", null, ["trader"])

## Gameplay Elements
### Mechanics
:generate: insert("templates/mechanics.md")

### User Interface
:generate: insert("templates/ui.md")

### Added Key Bindings
:generate: insert("templates/key_bindings.md")

<div style="page-break-after: always;"></div>

<h1 class="title">TECHNICAL ELEMENTS</h1>
_The purpose of this section is to inform the user about specific game entities, items, or sounds, enhancing their overall understanding of the product._

## Changes to Minecraft Functionality
:generate: insert("templates/mc_functionality_changes.md")

## Custom Inventory Items

### Player Facing Spawn Eggs
:generate: summarize_spawn_eggs("**/*.json", null, "player_facing")

### Player Facing Custom Blocks
:generate: summarize_blocks("**/*.json", null, "player_facing")

### Player Facing Regular Items
:generate: summarize_items("**/*.json", null, "player_facing")

### Non-Player Facing Spawn Eggs
:generate: summarize_spawn_eggs("**/*.json", null, "non_player_facing")

### Non-Player Facing Custom Blocks
:generate: summarize_blocks("**/*.json", null, "non_player_facing")

### Non-Player Facing Regular Items
:generate: summarize_items("**/*.json", null, "non_player_facing")

## Custom Creatures, Entities and Decorations
### Player Facing Entities

**Living creatures**

Every living entity that performs some actions on its own:

:generate: summarize_entities_in_tables("**/*.json", null, ["creature"])


**Menus and other interactive entities**

Shops and menus. non--living entities that player can interact with:

:generate: summarize_entities_in_tables("**/*.json", null, ["interactive_entity"])

**Projectiles**

Every projectile in the game:

:generate: summarize_entities_in_tables("**/*.json", null, ["projectile"])

**Vehicles**

Every vehicle in the game:

:generate: summarize_entities_in_tables("**/*.json", null, ["vehicle"])

**Decorations:**

Purely decorative entities:

:generate: summarize_entities_in_tables("**/*.json", null, ["decoration"])

**Block Entities:**

Entities imitating blocks:

:generate: summarize_entities_in_tables("**/*.json", null, ["block_entities"])

**Utilities:**

Entities that are visible but don't interact with the player directly:

:generate: summarize_entities_in_tables("**/*.json", null, ["player_facing_utility"])

### Non-Player Facing Entities

Invisible entities that affect the game in some way:

:generate: summarize_entities_in_tables("**/*.json", null, ["non-_player_facing_utility"])

## Trades

:generate: summarize_trades("**/*.json", null)

## Custom Sounds
:generate: sound_definitions()

## Features And Feature Rules

### Feature Rules
:generate: summarize_feature_rules_in_tables()

### Features
:generate: summarize_features_in_tables()

### The Feature Tree
:generate: feature_tree()

<div style="page-break-after: always;"></div>

<h1 class="title">CHANGELOG</h1>
_This section will contain the changelog in case of updates._
:generate: insert("templates/most_recent_changes.md")
