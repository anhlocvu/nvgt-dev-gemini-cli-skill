# NVGT Advanced Features

This document covers advanced topics in NVGT development.

## Multi-threading and Asynchronicity
NVGT supports multi-threading and cooperative multitasking.

### Coroutines
- `create_coroutine("function_name")`: Create a new coroutine that runs concurrently with the main script.
- `yield()`: Yield execution back to the main thread.

### Async Operations
- `async<T> task = async<T>("function_name", args...)`: Start an asynchronous task.
- `task.get()`: Retrieve the result once finished.

## Plugins
NVGT can be extended with plugins written in C++.
- `#pragma plugin "my_plugin.dll"`: Load a plugin.
- Plugin functions are then available globally or within a specific namespace.

### Examples of Built-in Plugins
- `curl`: Enhanced networking capabilities.
- `git`: Integrated version control within scripts.

## Cross-Platform Development
NVGT scripts are compiled into bytecode that can run on any supported platform.

- **Windows**: Use the `.exe` compiler.
- **Mac-OS**: Use the Mac compiler to create `.app` bundles.
- **Linux**: Build for standard Linux distros.
- **Android**: Package your script into an `.apk`.

### Platform Detection
Use preprocessor flags or the `get_platform()` function (if available) to detect the current OS.

## 3D Audio and Steam Audio
NVGT includes built-in support for HRTF 3D audio.
- Use the `sound` object with 3D properties: `position`, `listener_position`, `reverb`.
- Tweak Steam Audio settings via the `audio_engine` class.

## Cheat Engine Protection
NVGT has built-in protections against common memory-editing cheat tools. This is useful for competitive online audiogames.
- Protected variables can be declared using specific engine-managed classes.
