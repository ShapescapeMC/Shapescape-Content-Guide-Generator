(generator-functions)=
# Generator Functions

Generator functions are the functions you can use to insert text into the documentation. To do this, use the `:generate:` tag. The syntax is as follows
```
:generate: <function_name>([arguments])

- <function_name> - the name of the function
- [arguments] - the list of arguments. The arguments are separated and must be written in the same order as in the function's documentation. Some functions allow you to skip some arguments at the end of the list. If an argument is optional, the "[OPTIONAL]" tag is added to its description.
```

The tag and functions are replaced by the text that the function returns.

```{note}
This page refers to function arguments by their data types, or by short descriptive words that tell you what they are (like glob pattern). If you don't know what that means, you should read the {ref}`Argument Types<argument-types>`
```

```{note}
Some of the functions use "custom entity properties" or "custom item properties". You can read about them in the {ref}`Custom Properties<custom-properties>` section.
```

## completion_guide()
Generates the completion guide for the map based on the completion guide functions. Function names must follow the pattern `<step>_<title>`. Where `<step>` is an integer specifying the order of the steps and `<title>` is the title of the step. The `<title>` should be written in snake_case. The function will change this to title_case in the output.

**Syntax**
```
generate: completion_guide(search_patterns, exclude_patterns)
```

**Properties:**
- `search_patterns` - glob pattern or list of glob patterns to match files to include in the completion guide.
- `exclude_patterns [OPTIONAL]` - glob pattern or list of glob patterns to exclude from the completion guide (even if they match the `search_patterns`). The value of this property is `null` by default. You don't need to specify it if you don't want to exclude any files.

**Example**

Input
> :generate: completion_guide("completion_guide/*.mcfunction")

Output

> ### 1 - Start level 1
> Start level 1 using the menu in lobby.
> 
> You can complete this step using: `function completion_guide/1_start_level_1`
> 
> ### 2 - Complete level 1
> Win the level 1 by killing the fruits. You can use the
> `debug/win_wave` function to win a wave. You can use the `debug/win_level`
> function to automatically win the level.
> 
> You can complete this step using: `function completion_guide/2_complete_level_1`
> ...


## warp()
Generates descriptions of locations that can be accessed using warp functions. The contents of the matching files should follow this pattern:
```
# <description using comments (can have multiple lines)>
<tp command>
```
The `warp()` function extracts the coordinates from the `tp` command and adds the description.

**Syntax**
```
:generate: warp(search_patterns, exclude_patterns)
```


**Properties:**
- `search_patterns` - glob pattern or list of glob patterns to match against files to include.
- `exclude_patterns [OPTIONAL]` - glob pattern or list of glob patterns to match against files to exclude (even if they match the `search_patterns`). The value of this property is `null` by default. You don't need to specify it if you don't want to exclude any files.

**Example:**

Input

> :generate: warp("game_loop/level/*/warp.mcfunction")

Output

> - Spawn location of level 9 (113 -60 -597)
> - The lobby. This is the location where you can choose the level you want to
>   play and view the credits screen. (1278 -60 -876)
> ...



## insert()
Inserts an external MD file into the `TEMPLATE.md` file.

**Syntax**
```
:generate: insert(path)
```
**Properties**
- `path` - path to the MD file relative to the `TEMPLATE.md` file.

**Example:**

Input

> :generate: insert("templates/mechanics.md")

Output

> The content of the mechanics.md file

## list_entities(), summarize_entities() and summarize_entities_in_tables()
The functions that list entities by their identifiers. Some of them provide additional information based on custom entity properties.

- `list_entities()` is the simplest. It just lists the identifiers.
- `summarize_entities()` writes a summary in formatted text form.
- `summarize_entities_in_tables()` writes the summary in a table form.


**Syntax**
```
:generate: list_entities(search_patterns, exclude_patterns, categories)
```
```
:generate: summarize_entities(search_patterns, exclude_patterns, categories)
```
```
:generate: summarize_entities_in_tables(search_patterns, exclude_patterns, categories)
```
**Properties:**
- `search_patterns` - glob pattern or list of glob patterns to match files to include.
- `exclude_patterns [OPTIONAL]` - glob pattern or list of glob patterns to match files to exclude (even if they match the `search_patterns`). The value of this property is null by default. You don't need to specify it if you don't want to exclude any files.
 - `categories [OPTIONAL]` - the categories of entities to include. The category is a custom property of the entity, added to the description file in the entity behaviour. Category is a string. You can choose from categories listed on the {ref}`Custom Properties<custom-properties>` documentation page. The default value is `null`, which means that all entities are included.

**Example list_entities()**

Input

> :generate: summarize_entities_in_tables("**/*.json", null, ["projectile"])

Output

> - shapescape:apple_projectile
> - shapescape:potato_bullet
> - shapescape:potato_bullet_turret
> ...

**Example summarize_entities()**

Input

> :generate: summarize_entities("**/*.json", null, ["projectile"])

Output

> ### shapescape:apple_projectile
> A projectile shoot by the apple enemy.
> 
> ### shapescape:potato_bullet
> A projectile used by the potato launching weapons (Potato Yammer, Potato Masher, and Potato Shooter).
> 
> ### shapescape:potato_bullet_turret
> A projectile used by the Potato Turret.
> ...

**Example summarize_entities_in_tables()**

Input

> :generate: summarize_entities_in_tables("**/*.json", null, ["projectile"])

Output

> | Entity | Description | Locations |
> |-------|----------|------|
> | shapescape:apple_projectile | A projectile shoot by the apple enemy. | N/A |
> | shapescape:potato_bullet | A projectile used by the potato launching weapons (Potato Yammer, Potato Masher, and Potato Shooter). | N/A |
> | shapescape:potato_bullet_turret | A projectile used by the Potato Turret. | N/A |
> ...

## list_items(), summarize_items() and summarize_items_in_tables()
The functions that list items by their identifiers. Some of them provide some additional information based on custom item properties.

- `list_items()` is the simplest. It just lists the identifiers.
- `summarize_items_in_tables()` writes the summary in table form.
- `summarize_items()` writes the summary in a formatted text form. This is the most detailed format. It contains the list of entities that drop the item, a list of entities that trade with the item, and a list of recipes that create the item.

**Syntax**
```
:generate: list_items(search_patterns, exclude_patterns ,player_facing)
```
```
:generate: summarize_items(search_patterns, exclude_patterns ,player_facing)
```
```
:generate: summarize_items_in_tables(search_patterns, exclude_patterns ,player_facing)
```
**Properties:**
- `search_patterns` - glob pattern or list of glob patterns to match files to include.
- `exclude_patterns [OPTIONAL]` - glob pattern or list of glob patterns to match files to exclude (even if they match the `search_patterns`). The value of this property is null by default. You don't need to specify it if you don't want to exclude any files.
 - `player_facing [OPTIONAL]` - a string that determines whether player-facing, non-player-facing or both types of items should be included. You can choose one of the following values `"player_facing"`, `"non_player_facing"`, `"all"`. The default is `all`, which means that both types of items are included.


**Example list_items()**

Input

> :generate: list_items("**/*.json", null, "player_facing")

Output

> - shapescape:coin
> - shapescape:fire_extinguisher
> - shapescape:flame_thrower
> ...

**Example summarize_items()**

Input

> :generate: summarize_items("**/*.json", null, "player_facing")

Output

> ### shapescape:coin
> Drops from fruits. When collected, it is removed from the player's inventory and added to the coin counter.
> 
> ### shapescape:fire_extinguisher
> Fire extinquisher weapon. Freezes enemies. It can be purchased from the weapon shop.
> 
> ### shapescape:dragon_pants
> No, they're not made out of dragon skin, but they have a very cool dragon pattern on them.
> #### **Crafting recipe:**
> **Ingredients:**
> - minecraft:bone as N
> - minecraft:dragon_breath as D
> 
> **Pattern:**
> ```
> NNN
> NDN
> N N
> ```
> 
> #### **Dropped by:**
> - shapescape:skeleton_dummy
> #### **Traded by:**
> - shapescape:armor_trader1

**Example summarize_items_in_tables()**

Input

> :generate: summarize_items_in_tables("**/*.json", null, "player_facing")

Output

> | Item | Description |
> |------|-------------|
> | shapescape:coin | Drops from fruits. When collected, it is removed from the player's inventory and added to the coin counter. |
> | shapescape:fire_extinguisher | Fire extinguisher weapon. Freezes enemies. It can be purchased from the weapon shop. |
> | shapescape:flame_thrower | The Flameinator weapon. Sets enemies on fire. It can be purchased from the weapon shop. |
> ...

## list_spawn_eggs(), summarize_spawn_eggs() and summarize_spawn_eggs_in_tables()
These functions are analogous to `list_items()`, `summarize_items()` and `summarize_items_in_tables()`. They all print data in the same format. The only difference is that they expect paths to the entity files instead of the item files. Based on the entity files they generate information about the spawn eggs of the entities.

## list_blocks(), summarize_blocks() and summarize_blocks_in_tables() functions
These functions are analogous to `list_items()`, `summarize_items()` and `summarize_items_in_tables()`. They all print data in the same format. The only difference is that they expect paths to the block files instead of the item files. Based on the block files, they generate information about the custom blocks.


## sound_definitions()
Creates a list of sound definitions from the sound_definitions.json file. The list contains "friendly names" and the actual identifiers. The friendly names are based on the identifiers. This function does not take any properties.

**Syntax**
```
:generate: sound_definitions()
```
**Properties:** NONE

**Example**

Input

> :generate: sound_definitions()

Output

> - Custom - Shop Error (custom.shop.error)
> - Button - Click (button.click)
> - Shop - Buy (shop.buy)
> - Game state - Level lost (game_state.level_lost)
> - Game state - Level won (game_state.level_won)
> - Event - Wave complete (event.wave_complete)
> ...

## summarize_trades()
Creates a summary of all of the trades defined in the behavior pack. The summary contains simplified versions of the trade definitions and a list of entities that use each trade.

**Syntax**
```
:generate: summarize_trades(search_patterns, exclude_patterns)
```
**Properties:**
- `search_patterns` - glob pattern or list of glob patterns to match files to include.
- `exclude_patterns [OPTIONAL]` - glob pattern or list of glob patterns to match files to exclude (even if they match the `search_patterns`). The value of this property is null by default. You don't need to specify it if you don't want to exclude any files.

**Example**

Input

> :generate: summarize_trades("**/*.json", null)

Output

> ## Trade: ancient_builder/ancient_builder.trade.json
> #### Traded by:
> - shapescape:ancient_builder
> #### Content
> ```
> Tier 1 trades (Total EXP required: 0):
> ======================================
> 
> Group 1 - Selects 1 of following trades:
> ----------------------------------------
> 
> - Gives 16⨯shapescape:fur_block_orange FOR 4⨯minecraft:emerald
> - Gives 16⨯shapescape:fur_block_green FOR 4⨯minecraft:emerald
> - Gives 16⨯shapescape:fur_block_blue FOR 4⨯minecraft:emerald
> - Gives 16⨯shapescape:fur_block_purple FOR 4⨯minecraft:emerald
> 
> Group 2 - Selects 1 of following trades:
> ----------------------------------------
> 
> - Gives 4⨯shapescape:raw_primal_meat & 4⨯minecraft:dirt FOR 1⨯minecraft:emerald & 1⨯minecraft:gold
> 
> Group 3 - Selects 1 of following trades:
> ----------------------------------------
> 
> - Gives 2⨯shapescape:ancient_shard FOR 1⨯minecraft:emerald
> - Gives 7⨯shapescape:raw_primal_meat FOR 1⨯minecraft:emerald

## list_features(), summarize_features() and summarize_features_in_tables() functions
The feature summaries don't take any arguments. They list all the features defined in the behavior pack. The summaries contain the feature identifiers, the descriptions and the list of features that are placed by the described feature.

## list_feature_rules(), summarize_feature_rules() and summarize_feature_rules_in_tables() functions
The feature rule summaries don't take any arguments. They list all the feature rules defined in the behavior pack. The summaries contain the feature rule identifiers, the descriptions and the list of features that are placed by the described feature rule.

## feature_tree()
Creates a tree of features and feature rules. This is useful to give an overview of how the features are connected to each other. The function does not take any properties.
feature_tree
**Syntax**
```
:generate: feature_tree()
```
