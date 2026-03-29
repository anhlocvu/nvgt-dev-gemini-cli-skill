# Porting from BGT to NVGT

NVGT is designed to be "mostly compatible" with BGT, but there are some key differences due to the underlying AngelScript engine.

## General Tips
1. **File Extension**: Change your `.bgt` files to `.nvgt`.
2. **Handles (@ symbol)**: NVGT requires the `@` symbol for all object handles. This is the biggest change.
   - BGT: `sound s; s.load("test.wav");`
   - NVGT: `sound@ s = sound(); s.load("test.wav");`
3. **Reference Counting**: Objects are automatically reference-counted. You don't need to explicitly delete them, just set the handle to `null`.
4. **Keyword Changes**: Some keywords might have changed or become more strict.

## Sound Differences
- The `sound` class in NVGT is more powerful and supports 3D audio via Steam Audio.
- Use `mixer` classes for grouped sound control.
- Volume is now in decibels (dB) instead of the percentage-based system in BGT.

## Speech and Screen Readers
- Use the `#include "speech.nvgt"` module.
- Instead of the global `speak()` function in BGT, NVGT uses a standard AngelScript function from the `speech` module.

## Networking
- The `network` object is more modern and supports HTTPS out of the box.
- Asynchronous networking is preferred in NVGT using callbacks.

## Key Codes
NVGT uses standard key codes (e.g., `KEY_UP`, `KEY_DOWN`) which are largely compatible with BGT's constants, but check the documentation if a key doesn't work.

## Breaking Changes
- `include` must use double quotes or angle brackets: `#include "file.nvgt"` or `#include <file.nvgt>`.
- `void main()` is the required entry point.
- Global variables must be initialized or declared outside functions.
- `array<T>` is the standard way to handle arrays, replacing the old `T[]` syntax (though `T[]` might still work in some contexts, `array<T>` is safer).
