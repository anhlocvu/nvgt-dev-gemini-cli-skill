# NVGT API Reference

NVGT provides a rich set of built-in classes and functions for game development.

## Sound and Audio
The `sound` class is the primary interface for playing audio.

- `sound@ s = sound();`: Create a new sound object.
- `bool load(string filename)`: Load a sound file.
- `void play()`: Play the sound.
- `void play_looped()`: Play and loop the sound.
- `void play_wait()`: Play and wait until it finishes.
- `void stop()`: Stop playback.
- `void pause()`: Pause playback.
- `void resume()`: Resume playback.
- `bool active`: Returns true if the sound is currently playing.
- `float pitch`: Get or set the pitch (0.5 to 2.0).
- `float volume`: Get or set the volume (-100.0 to 0.0 in dB).
- `float pan`: Get or set the pan (-100 to 100).

### Mixers
Mixers are used to group sounds and apply effects globally.
- `mixer@ m = mixer();`
- `s.set_mixer(m);`

## Screen Reader and Speech
Requires `#include "speech.nvgt"`.

- `void speak(string text, bool interrupt = true)`: Speak text via the current screen reader.
- `void speak_interrupt(string text)`: Equivalent to `speak(text, true)`.
- `void stop_speech()`: Stop all ongoing speech.

## Input Handling
- `bool key_pressed(int key_code)`: Returns true if a key is currently pressed.
- `bool key_released(int key_code)`: Returns true if a key was just released.
- `bool key_down(int key_code)`: Returns true while a key is held down.

Standard key codes (e.g., `KEY_LEFT`, `KEY_RIGHT`, `KEY_SPACE`, `KEY_RETURN`).

## Networking
- `network@ n = network();`: Create a networking object for HTTP/HTTPS or low-level sockets.
- `void get(string url, string callback_func)`: Perform an asynchronous GET request.

## Files and Storage
- `file@ f = file();`: Create a file handle.
- `bool open(string path, string mode)`: Open a file (mode: "r", "w", "a", "rb", "wb").
- `string read(uint length)`: Read data from the file.
- `void write(string data)`: Write data to the file.
- `void close()`: Close the file.

### JSON and SQLite
- `json_object@ j = json_object();`: Work with JSON data.
- `sqlite3@ db = sqlite3();`: Work with SQLite databases.

## Utilities
- `void alert(string title, string message)`: Show a standard message box.
- `void wait(uint ms)`: Pause script execution for a given number of milliseconds.
- `uint get_ticks()`: Get the number of milliseconds since the program started.
- `int random(int min, int max)`: Generate a random number.
