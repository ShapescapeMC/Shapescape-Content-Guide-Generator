(custom-properties)=
# Custom properties
Custom properties are the properties that you add to various JSON Minecraft files to provide the generator with additional information about the entity that needs to be documented. This page lists and explains all the custom properties that can be added to the project's JSON files to control the generation process.

## Behaviour Pack Entity Files
This section describes the custom properties that can be added to the entity files in the behavior pack. The properties are added to the `["minecraft:entity"].description` object in the JSON file.

### description

- Path: `BP/entities/*.json`.
- JSON path: `["minecraft:entity"].description.description`.

```{note}
The `description` is a property of `description` object.
```

Description is a string or list of strings that describes the entity in the `summarize_entities()` and `summarize_entities_in_tables()` functions. If description is written as a list, it is assumed that each string is a separate line of the description. You can read more about the functions in {ref}`Generator Functions<generator-functions>` section.

**Examples**
```
"description": "This is the main entity used for running commands."
```
```
"description": [
    "This entity serves as player's companion. It has multiple purposes:",
    "- It can heal the player",
    "- It helps with telling the story"
]
```


### locations
- Path: `BP/entities/*.json`.
- JSON path: `["minecraft:entity"].description.locations`.

Locations is a list of locations where the entity can be found. Locations should be written as a list of strings. The strings should follow this format `<x> <y> <z>` where `<x>`, `<y>` and `<z>` are numbers.

If it doesn't make sense to provide locations for information about the entity (e.g. the entity is a mob and spawns dynamically in the world), the property should be an empty list (`[]`).


**Examples**
```
"locations": []
```
```
"locations": ["1 2 3", "1.1 -2.3 10"]
```


### category
- Path: `BP/entities/*.json`
- JSON Path: `["minecraft:entity"].description.category`

Category is a string that classifies the entity into one of the following groups
- `"character"` - this category was added to follow Microsoft's suggestion of describing how to write the content guide. The entities used to tell the story should be placed in this category. Entities in this group should be added to the Characters and Villagers section of the Content Guide.
- `"trader"` - this category has been added to follow Microsoft's suggestion of how to write a content guide. The living entities used for trading should be placed in this category. The entities in this group should be added to the Characters and Villagers section of the content.
- `"non_player_facing_utility"` - any invisible entity like (path markers, main entity, invisible spawners, etc.) should be added to this category. Entities in this category should be placed in the Non-Player Facing Entities section of the content guide.
- `"player_facing_utility"` - this category can be treated as an "other" category. It describes visible utility entities that don't interact with the player in any way. Here are some examples
    - A portal (with particle effect) that spawns mobs. This would be non_player_facing, but it's visible.
    - An entity that represents a cloud of poisonous gas.
    - A unit that is only used to spawn certain particles and despawns immediately after spawning.
    - an automatic turret or other traps
- `"projectile"` - any entity that uses the "minecraft:projectile" component
- `"vehicle"` - inanimate units that the player can ride on
- `"creature"` - any living entity that doesn't fit into a character or trader category (mobs and monsters).
- `"decoration"` - any entity used for purely visual purposes (e.g. furniture)
- `"interactive_entity"` - inanimate entities you spawn in the world to interact with (e.g. entity-based menus, stationary shop entities, etc.)
- `"block_entity"` - entities used to mimic the properties of a block.

**Examples**
```
"category": "block_entity"
```


### spawn_egg_description

- Path: `BP/entities/*.json`
- JSON Path: `["minecraft:entity"].description.spawn_egg_description`

Description of the spawn egg. It's analogous to the item's `description` property. It's used in the functions that describe spawn eggs.

**Examples**
```
"spawn_egg_description": "An item that spawns a dragon"
```
```
"spawn_egg_description": ["An item that spawns a dragon"]
```

### spawn_egg_player_facing

- Path: `BP/entities/*.json`
- JSON Path: `["minecraft:entity"].description.spawn_egg_player_facing`

A boolean indicating whether the spawn egg is player facing or not. It's analogous to the `player_facing` property of the item. It's used for the functions that describe spawn eggs.

**Examples**
```
"spawn_egg_player_facing": true
```

## Behavior Pack Item Files
This section describes the custom properties that can be added to the item files in the behavior pack. The properties are added to the `["minecraft:item"].description` object in the JSON file.

### description

- Path: `packs/BP/items/*.json`
- JSON Path: `["minecraft:item"].description.description`

Description is a string or list of strings that describes the item in the `summarize_items()` and `summarize_items_in_tables()` functions. If description is written as a list, it is assumed that each string is a separate line of the description. You can read more about the functions in {ref}`Generator Functions<generator-functions>` section.

**Examples**
```
"description": "This is the main entity used for running commands."
```
```
"description": [
    "This entity serves as player's companion. It has multiple purposes:",
    "- It can heal the player",
    "- It helps with telling the story"
]
```

### player_facing

- Path: `packs/BP/items/*.json`
- JSON Path: `["minecraft:item"].description.player_facing`

Player-facing is a boolean value that determines whether or not the item is a "player-facing" item. Most items are player-facing, but Microsoft's recommendation is to split them into two groups for documentation purposes.

## Behavior Pack Block Files

This section describes the custom properties that can be added to the block files in the behavior pack. The properties are added to the `["minecraft:block"].description` object in the JSON file.

**Examples**
```
"player_facing": true
```

```{note}
All of the properties used by the block are the same as the ones used by the item. The only difference is the path to the file and JSON path inside the file.

Blocks are stored in 'blocks' flder and the JSON path is using 'minecraft:block' instead of 'minecraft:item'.
```


### description

- Path: `packs/BP/blocks/*.json`
- JSON Path: `["minecraft:block"].description.description`

Description is a string or list of strings that describes the block in the `summarize_blocks()` and `summarize_blocks_in_tables()` functions. If description is written as a list, it is assumed that each string is a separate line of description. You can read more about the functions in {ref}`Generator Functions<generator-functions>` section.

**Examples**
```
"description": "This is the main entity used for running commands."
```
```
"description": [
    "This entity serves as player's companion. It has multiple purposes:",
    "- It can heal the player",
    "- It helps with telling the story"
]
```

### player_facing

- Path: `packs/BP/blocks/*.json`
- JSON Path: `["minecraft:block"].description.player_facing`

Player facing is a boolean value that determines whether the block is a "player-facing" block or not. Most blocks are player-facing, but Microsoft's recommendation is to split them into two groups for documentation purposes.

**Examples**
```
"player_facing": true
```
