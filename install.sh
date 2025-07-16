#!/usr/bin/env bash
set -e

# ------------------------ CONFIG ------------------------
REPO_URL="https://github.com/contacthorse/forever-app.git"
APP_DIR="forever-app"
# --------------------- END CONFIG -----------------------

# ---------- UTILITIES ----------
green()  { echo -e "\033[32m$1\033[0m"; }
red()    { echo -e "\033[31m$1\033[0m"; }
yellow() { echo -e "\033[33m$1\033[0m"; }

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

detect_os() {
  if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "$ID"
  else
    uname -s | tr '[:upper:]' '[:lower:]'
  fi
}

install_git() {
  local os_id="$1"
  case "$os_id" in
    amzn|amazon)
      sudo dnf install -y git
      ;;
    ubuntu|debian)
      sudo apt update && sudo apt install -y git
      ;;
    *)
      red "Unsupported OS for Git install: $os_id"
      exit 1
      ;;
  esac
}

install_docker() {
  local os_id="$1"
  case "$os_id" in
    amzn|amazon)
      sudo dnf install -y docker
      sudo systemctl enable --now docker
      ;;
    ubuntu|debian)
      curl -fsSL https://get.docker.com | sudo bash
      ;;
    *)
      red "Unsupported OS for Docker install: $os_id"
      exit 1
      ;;
  esac
  sudo usermod -aG docker "$USER"
  newgrp docker || true
}

install_compose_v2() {
  local plugin_dir="/usr/local/lib/docker/cli-plugins"
  sudo mkdir -p "$plugin_dir"
  sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
    -o "$plugin_dir/docker-compose"
  sudo chmod +x "$plugin_dir/docker-compose"
}

# ---------- BEGIN EXECUTION ----------
OS_ID="$(detect_os)"

# --- Git ---
if ! command -v git >/dev/null 2>&1; then
  red "❌ Git is not installed."
  if confirm "Do you want to install Git now?"; then
    install_git "$OS_ID"
    green "✅ Git installed."
  else
    red "🚫 Git is required. Aborting."
    exit 1
  fi
else
  green "✅ Git is already installed."
fi

# --- Docker ---
if ! command -v docker >/dev/null 2>&1; then
  red "❌ Docker is not installed."
  if confirm "Install Docker now?"; then
    install_docker "$OS_ID"
    green "✅ Docker installed."
  else
    red "🚫 Docker is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker is already installed."
fi

# --- Docker Compose v2 ---
if ! docker compose version >/dev/null 2>&1; then
  red "❌ Docker Compose v2 not found."
  if confirm "Install Docker Compose v2 manually?"; then
    install_compose_v2
    green "✅ Docker Compose v2 installed."
  else
    red "🚫 Compose v2 is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker Compose v2 is available."
fi

# --- Clone repo ---
if [ ! -d "$APP_DIR" ]; then
  green "📥 Cloning repository from $REPO_URL"
  git clone "$REPO_URL" "$APP_DIR"
else
  yellow "📁 $APP_DIR already exists. Using existing folder."
fi

cd "$APP_DIR"

# --- Copy .env if missing ---
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  green "⚙️ Creating .env from .env.example"
  cp .env.example .env
fi

# --- Start App ---
if [ -f "docker-compose.yml" ]; then
  green "🚀 Starting app using Docker Compose..."
  docker compose up -d
  green "✅ App is starting! Visit http://localhost:3000"
else
  red "❌ docker-compose.yml not found. Aborting."
  exit 1
fi
