#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/contacthorse/forever-app.git"
APP_DIR="forever-app"

# --- Helpers: Colors ---
green() { echo -e "\033[32m$1\033[0m"; }
red()   { echo -e "\033[31m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }

# --- Prompt function that works in curl | bash ---
confirm() {
  local prompt="${1:-Are you sure?}"
  local default="${2:-N}"
  local response

  if [ -t 0 ]; then
    read -r -p "$prompt [y/N] " response
  elif [ -e /dev/tty ]; then
    read -r -p "$prompt [y/N] " response < /dev/tty
  else
    echo "⚠️  Cannot prompt (no terminal). Assuming '$default'."
    response="$default"
  fi

  response="${response:-$default}"
  [[ "$response" =~ ^[Yy]$ ]]
}

# --- 1. Check for Git ---
if ! command -v git >/dev/null 2>&1; then
  red "❌ Git is not found."
  if confirm "Do you want to install Git now?"; then
    sudo apt update && sudo apt install -y git
    green "✅ Git installed."
  else
    red "🚫 Git is required. Aborting."
    exit 1
  fi
else
  green "✅ Git is already installed."
fi

# --- 2. Check for Docker ---
if ! command -v docker >/dev/null 2>&1; then
  red "❌ Docker is not installed."
  if confirm "Install Docker (with Docker Compose v2)?"; then
    curl -fsSL https://get.docker.com | sudo bash
    sudo usermod -aG docker "$USER"
    newgrp docker || true
    green "✅ Docker installed. You may need to log out and back in."
  else
    red "🚫 Docker is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker is already installed."
fi

# --- 3. Check for Docker Compose v2 ---
if ! docker compose version >/dev/null 2>&1; then
  red "❌ Docker Compose v2 not found (needs 'docker compose' command)."
  if confirm "Upgrade Docker to get Compose v2?"; then
    curl -fsSL https://get.docker.com | sudo bash
    green "✅ Docker upgraded."
  else
    red "🚫 Docker Compose v2 is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker Compose v2 is available."
fi

# --- 4. Clone the App Repo ---
if [ ! -d "$APP_DIR" ]; then
  green "📥 Cloning repository from $REPO_URL"
  git clone "$REPO_URL" "$APP_DIR"
else
  yellow "📁 $APP_DIR already exists. Using existing folder."
fi

cd "$APP_DIR"

# --- 5. Create .env if needed ---
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  green "⚙️ Creating .env from .env.example"
  cp .env.example .env
fi

# --- 6. Start App with Docker Compose ---
if [ -f "docker-compose.yml" ]; then
  green "🚀 Starting app using Docker Compose..."
  docker compose up -d
  green "✅ App is starting! Visit http://localhost:3000"
else
  red "❌ docker-compose.yml not found. Aborting."
  exit 1
fi
