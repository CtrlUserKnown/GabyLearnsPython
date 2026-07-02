#!/bin/sh
set -e

# ── pylings TUI installer ──────────────────────────────────────
# Builds and installs the pylings TUI, then ensures it's on PATH.
# Usage:  sh install.sh
#         curl -fsSL https://... | sh
# ────────────────────────────────────────────────────────────────

BOLD='\033[1m'
GREEN='\033[92m'
RED='\033[91m'
YELLOW='\033[93m'
CYAN='\033[96m'
DIM='\033[2m'
RESET='\033[0m'

info()  { printf "  ${CYAN}→${RESET}  %s\n" "$*"; }
ok()    { printf "  ${GREEN}✔${RESET}  %s\n" "$*"; }
err()   { printf "  ${RED}✘${RESET}  %s\n" "$*"; exit 1; }

# ── Detect project root (where this script lives) ──────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# ── Pre-flight checks ──────────────────────────────────────────
info "Checking prerequisites..."

if ! command -v swift >/dev/null 2>&1; then
    err "Swift is not installed. Install Xcode or run: xcode-select --install"
fi
if ! command -v python3 >/dev/null 2>&1; then
    err "Python 3 is required but not found on PATH."
fi
if [ ! -d PylingsTUI/Sources ]; then
    err "Run this script from the project root (PylingsTUI/Sources/ not found)."
fi
if [ ! -d PylingsTUI/Practice ]; then
    info "Initializing git submodule..."
    git submodule update --init --recursive 2>/dev/null || \
        err "Failed to initialize submodule. Try: git submodule update --init"
    ok "Submodule initialized"
fi
ok "Prerequisites met"

# ── Build ───────────────────────────────────────────────────────
info "Building pylings TUI (universal binary)..."
cd PylingsTUI
swift build -c release --arch arm64 --arch x86_64 2>&1 | \
    while IFS= read -r line; do printf "     ${DIM}%s${RESET}\n" "$line"; done
cd "$SCRIPT_DIR"

BINARY="PylingsTUI/.build/apple/Products/Release/pylings"
if [ ! -f "$BINARY" ]; then
    # Fallback: single-arch build
    info "Universal build failed, trying single-arch..."
    cd PylingsTUI
    swift build -c release 2>&1 | \
        while IFS= read -r line; do printf "     ${DIM}%s${RESET}\n" "$line"; done
    cd "$SCRIPT_DIR"
    BINARY="PylingsTUI/.build/arm64-apple-macosx/release/pylings"
    if [ ! -f "$BINARY" ]; then
        BINARY="PylingsTUI/.build/x86_64-apple-macosx/release/pylings"
    fi
    if [ ! -f "$BINARY" ]; then
        err "Build failed — could not find pylings binary."
    fi
fi
ok "Build complete"

# ── Determine install location ──────────────────────────────────
if [ "$(id -u)" = "0" ]; then
    # Running as root — install system-wide
    DEST="/usr/local/bin"
else
    # User install — prefer ~/.local/bin, then /usr/local/bin
    if [ -d "$HOME/.local/bin" ] || echo "$PATH" | grep -q "$HOME/.local/bin"; then
        DEST="$HOME/.local/bin"
    elif [ -d "/usr/local/bin" ] && [ -w "/usr/local/bin" ]; then
        DEST="/usr/local/bin"
    elif [ -d "$HOME/bin" ] || echo "$PATH" | grep -q "$HOME/bin"; then
        DEST="$HOME/bin"
    else
        DEST="$HOME/.local/bin"
    fi
fi

mkdir -p "$DEST"

# ── Install ─────────────────────────────────────────────────────
cp "$BINARY" "$DEST/pylings"
chmod 755 "$DEST/pylings"

ok "Installed to ${DEST}/pylings"

# ── Ensure on PATH ──────────────────────────────────────────────
case :$PATH: in
    *:$DEST:*)  ;;
    *)
        # Detect shell and offer to add to config
        SHELL_NAME="$(basename "$SHELL" 2>/dev/null || echo "sh")"
        case "$SHELL_NAME" in
            zsh|bash)
                RC="$HOME/.${SHELL_NAME}rc"
                if [ -f "$RC" ]; then
                    printf "\n  ${YELLOW}⚠${RESET}  ${DEST} is not on your PATH."
                    printf "\n     Add this line to ${BOLD}${RC}${RESET}:\n\n"
                    printf "         ${CYAN}export PATH=\"\$PATH:${DEST}\"${RESET}\n\n"
                fi
                ;;
        esac
        # Always print a note
        printf "  ${CYAN}→${RESET}  ${DEST} is not on your PATH.\n"
        printf "     Add it:  ${BOLD}export PATH=\"\$PATH:${DEST}\"${RESET}\n"
        ;;
esac

# ── Verify ──────────────────────────────────────────────────────
if command -v pylings >/dev/null 2>&1; then
    ok "pylings is ready to use — run ${BOLD}pylings${RESET}"
else
    printf "\n  ${CYAN}→${RESET}  Start a new terminal or run:  ${BOLD}export PATH=\"\$PATH:${DEST}\"${RESET}\n"
    printf "     Then launch with:  ${BOLD}pylings${RESET}\n"
fi
