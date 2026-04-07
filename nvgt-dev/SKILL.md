---
name: nvgt-dev
description: Expert guidance for developing games and applications using the NVGT (Non-Visual Game Toolkit) programming language. Use when creating audiogames, working with AngelScript-based syntax, or porting BGT (Blastbay Gaming Toolkit) projects.
---

# NVGT Dev Skill

This skill provides expert knowledge and workflows for the NVGT (Non-Visual Game Toolkit) programming language. NVGT is a cross-platform, modern engine designed for creating audiogames, primarily used by visually impaired developers and gamers.

## Core Knowledge

NVGT is based on the **AngelScript** scripting language and is designed to be mostly compatible with the legacy **BGT (Blastbay Gaming Toolkit)**.

> **CRITICAL: Dynamic Updates**
> NVGT is updated frequently. If you are performing a complex task or the user asks for the latest features, you MUST use `web_fetch` to check:
> 1. [https://nvgt.dev/docs/nvgt.txt](https://nvgt.dev/docs/nvgt.txt) for the latest API changes.
> 2. [https://github.com/samtupy/nvgt](https://github.com/samtupy/nvgt) (specifically the `src/` or `release/include/` folders) for new classes or syntax.

Always check nvgt's GitHub repository to learn the latest syntax.

- **Official Website**: [https://nvgt.dev/](https://nvgt.dev/)
- **Documentation**: [https://nvgt.dev/docs/nvgt.txt](https://nvgt.dev/docs/nvgt.txt)
- **GitHub Repository**: [https://github.com/samtupy/nvgt](https://github.com/samtupy/nvgt)

## Key Concepts

### Entry Point
Every NVGT script starts with the `void main()` function.

```nvgt
void main() {
    alert("Hello", "Welcome to NVGT!");
}
```

### Sound Handling
The `sound` class is central to NVGT. Use the `@` symbol for handles (reference counting).

```nvgt
sound@ s = sound();
if(s.load("jump.wav")) {
    s.play_wait();
}
```

### Accessibility
Integrated screen reader support via `speech.nvgt` and the `speak()` function.

## Detailed Guides

For specific topics, refer to these documents:

- **Syntax & Basics**: [references/syntax.md](references/syntax.md) - AngelScript syntax, variables, and control structures.
- **API Reference**: [references/api.md](references/api.md) - Classes like `sound`, `mixer`, `network`, and `file`.
- **Advanced Features**: [references/advanced.md](references/advanced.md) - Multi-threading, plugins, and cross-platform development.
- **BGT Porting**: [references/bgt_porting.md](references/bgt_porting.md) - Tips for migrating from BGT to NVGT.

## Workflows

### 1. Starting a New Project
1. Create a `.nvgt` file.
2. Define the `void main()` function.
3. Include necessary modules using `#include "module_name.nvgt"`.
4. Use `#pragma asset "path/to/file"` to embed resources.

### 2. Debugging
- Use `alert()` or `speak()` for simple trace debugging.
- Check the console output if running from the command line.

### 3. Packaging
NVGT scripts can be compiled into standalone executables for Windows, Mac, Linux, and Android using the NVGT compiler.
