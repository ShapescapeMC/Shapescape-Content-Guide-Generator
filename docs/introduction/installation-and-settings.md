(installation-and-settings)=
# Installation & Settings

## Steps

### 1. Install the filter
Use the following command
```
regolith install shapescape_content_guide_generator
```

You can alternatively use this command:
```
regolith install github.com/ShapescapeMC/Shapescape-Content-Guide-Generator/shapescape_content_guide_generator
```

### 2. Add filter to a profile
Add the filter to the `filters` list in the `config.json` file of the Regolith project and add the settings:

```json
{
    "filter": "content_guide_generator",
    "settings": {
        "output_paths": ["OUTPUT.md"]
    }
},
```

# ⚙️ Configuration settings

- `output_paths: list` - A list of all the desired output paths. Default is "OUTPUT.md"
