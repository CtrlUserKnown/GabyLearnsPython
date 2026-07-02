# Changelog

## 2026-06-13

### Added
- **Pylings TUI**: Full keyboard-navigable Terminal User Interface written in Swift (zero dependencies). Inspired by lazygit/mole — navigate exercises with ↑↓/jk, press Enter to run, `h` for hints, `e` to open in editor, `r` to refresh, `q` to quit. Displays test output inline and smart-scrolls for small terminals.
- **Swift package**: `PylingsTUI/Package.swift` (Swift 5.9, macOS 13+, no external dependencies). Universal binary build (arm64 + x86_64) via `Makefile`.
- **`install.sh`**: Portable `sh` installer — checks prerequisites, builds universal binary, installs to `~/.local/bin` (or `/usr/local/bin` as root), detects PATH membership, prints config instructions.
- **`pylings-tui`**: Convenience wrapper script at project root to launch the TUI without installing.
- **Practice exercises migrated to submodule**: All 16 `Practice/Mod*.py` files and the `pylings` Python runner now live inside `PylingsTUI/` as a self-contained git submodule.
- **PylingsTUI/README.md**: Dedicated documentation for the submodule in Caine-style game show host voice.

### Changed
- **Python TTY detection**: `check()` and `run_mod()` now use `sys.stdout.isatty()` — shows `\r`-based progress bar in interactive terminals, clean per-test lines when captured as subprocess (critical for clean TUI output).
- **Project restructuring**: `Practice/` directory and `pylings` script removed from root, now housed entirely within the `PylingsTUI/` submodule.
- **README.md**: Rewritten entirely in Caine-style arcade game show host voice referring to the learner as "the Gaby". Updated project structure to reflect submodule layout, added TUI usage documentation.

## 2026-06-04

### Added
- **Auto-watch on no args**: Running `pylings` with no arguments now starts watch mode on the next incomplete exercise.
- **Real-time syntax checking**: Before running tests, the module is parsed with `ast.parse()`. On a syntax error, a clean message shows the file, line, column, and error — no raw tracebacks.
- **Keyboard shortcuts in watch mode**: Press `q` to quit, `h` to show hints.
- **Hints system**: Pressing `h` in watch mode lists all remaining `# TODO` items and unimplemented functions (`raise NotImplementedError`) for the current module.

### Changed
- **Practice modules rewritten**: All 8 `Practice/Mod*.py` files now look like real project code:
  - Module docstrings with realistic context (City Config, User Profile, Order Processing, etc.)
  - `# TODO` comments instead of `# YOUR CODE HERE`
  - `raise NotImplementedError()` for function stubs (standard Python pattern)
  - Removed numbered exercise lists and untested exercises
