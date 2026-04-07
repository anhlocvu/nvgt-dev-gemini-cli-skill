# NVGT Syntax Reference

NVGT uses the **AngelScript** language, which has a C++/C#/Java-like syntax.

## Variables and Types

### Basic Types
- `int`, `uint` (32-bit signed and unsigned)
- `int64`, `uint64` (64-bit signed and unsigned)
- `float`, `double` (floating-point numbers)
- `bool` (`true` or `false`)
- `string` (standard string type)

### Complex Types
- `array<T>`: A template-based array (e.g., `array<int> numbers = {1, 2, 3};`).
- `dictionary`: A key-value pair container (e.g., `dictionary d; d.set("key", "value");`).

## Handles and Object Pointers
In NVGT, objects are managed using **handles**, denoted by the `@` symbol.

```nvgt
sound@ s = sound(); // Create a handle and instantiate a sound object
@s = null;          // Clear the handle
```

- Use `@` for assignment to copy handles, not the object's value.
- Use `is` and `!is` to check handle equality (e.g., `if(s is null)`).

## Control Flow
NVGT supports standard control flow structures:

- `if`, `else if`, `else`
- `switch` (on integers or strings)
- `for`, `while`, `do-while`
- `break`, `continue`

## Functions
Functions are declared like in C++:

```nvgt
int add(int a, int b) {
    return a + b;
}
```

- Supports default parameters.
- Supports overloading (multiple functions with the same name but different signatures).

## Classes
You can define custom classes:

```nvgt
class Player {
    int health;
    string name;

    Player(string n) {
        this.name = n;
        this.health = 100;
    }

    void take_damage(int amount) {
        health -= amount;
    }
}
```

## Preprocessor Directives
- `#include "filename.nvgt"`: Include another script.
- `#pragma asset "filename"`: Mark a file as an asset to be included in the final package.
- `#pragma plugin "pluginname"`: Load a specific NVGT plugin.
- `#pragma compiler_opt "option"`: Set compiler options.
