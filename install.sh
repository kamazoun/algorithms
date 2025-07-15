#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/contacthorse/forever-app.git"
APP_DIR="forever-app"

green() { echo -e "\033[32m$1\033[0m"; }
red()   { echo -e "\033[31m$1\033[0m"; }

# -- Prompt that works via curl | bash --
confirm() {
  local prompt="${1:-Are you sure?}"
  local default="${2:-N}"
  local response

  if [[ -t 0 ]]; then
    read -rp "$prompt [y/N] " response
  fi

  response="${response:-$default}"

  [[ "$response" =~ ^[Yy]$ ]]
}

# --- Git Check ---
if ! command -v git >/dev/null 2>&1; then
  red "❌ Git is not installed."
  if confirm "Install Git now?"; then
    sudo apt update && sudo apt install -y git
    green "✅ Git installed."
  else
    red "🚫 Git is required. Aborting."
    exit 1
  fi
else
  green "✅ Git is already installed."
fi

# --- Docker Check ---
if ! command -v docker >/dev/null 2>&1; then
  red "❌ Docker is not installed."
  if confirm "Install Docker (with Docker Compose V2)?"; then
    curl -fsSL https://get.docker.com | sudo bash
    sudo usermod -aG docker "$USER"
    green "✅ Docker installed. You may need to log out and back in."
  else
    red "🚫 Docker is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker is already installed."
fi

# --- Docker Compose Check ---
if ! docker compose version >/dev/null 2>&1; then
  red "❌ Docker Compose V2 not available."
  if confirm "Upgrade Docker to enable Compose V2?"; then
    curl -fsSL https://get.docker.com | sudo bash
    green "✅ Docker updated."
  else
    red "🚫 Docker Compose V2 is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker Compose V2 is available."
fi

# --- Clone repo ---
if [ ! -d "$APP_DIR" ]; then
  green "📥 Cloning repository from $REPO_URL"
  git clone "$REPO_URL" "$APP_DIR"
fi

cd "$APP_DIR"

# --- Copy .env ---
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  green "⚙️ Creating .env from .env.example"
  cp .env.example .env
fi

# --- Start App ---
if [ -f "docker-compose.yml" ]; then
  green "🚀 Starting app using Docker Compose..."
  docker compose up -d
  green "✅ App
