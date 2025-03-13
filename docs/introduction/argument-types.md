(argument-types)=
# Arguments Types
This section describes the types of arguments that can be used in the generator functions.

- **String** - Text variable. Strings must be enclosed in double quotes (`""`).
  **Examples:**
  - `"Hello World"` - a string that says "Hello World".
- **Glob pattern** - a string with a pattern that matches one or more file paths. Glob patterns can use special wildcards to match any file or directory name (single asterisk `*`), any number of characters (double asterisk `**`). **Examples:**
  - `"hello/*.json"` - all `.json` files in the `hello` directory
  - `"**/*.mcfunction"` - all `.mcfunction` files in the project
- **List** - multiple values grouped together. Lists use square brackets
  (`[]`). **Examples:**
  - `["hello", "world"]` - list of two strings
  - `["hello", 1, 2, 3]` - list with one string and three numbers
- **null** - no value. Null is written as literal `null` (lowercase).
- **bool** - boolean value. Boolean values are written as `true` or `false`.
