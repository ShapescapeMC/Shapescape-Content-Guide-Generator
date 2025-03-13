from shapescape_content_guide_generator.main import main_regolith
import json
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        config = json.loads(sys.argv[1])
        if 'output_paths' in config:
            output_paths = config['output_paths']
        else:
            output_paths = ["OUTPUT.md"]
    else:
        output_paths = ["OUTPUT.md"]
    main_regolith(output_paths)
