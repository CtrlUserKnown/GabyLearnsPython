# Changelog

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
