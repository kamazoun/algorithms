#!/usr/bin/env bash
set -e

# ---------------- CONFIG ----------------
REPO_URL="https://github.com/contacthorse/forever-app.git"
APP_DIR="forever-app"
DOCKER_CMD="docker"  # fallback to sudo if needed
# ----------------------------------------

# -------- COLORS ----------
green()  { echo -e "\033[1;32m$1\033[0m"; }
red()    { echo -e "\033[1;31m$1\033[0m"; }
yellow() { echo -e "\033[1;33m$1\033[0m"; }
blue()   { echo -e "\033[1;34m$1\033[0m"; }

# -------- LOGO ----------
banner() {
  echo -e "\033[1;36m"
  cat << "EOF"

 ╔═╗ ╔═╗ ╔╗╔ ╔╦╗ ╔═╗ ╔═╗ ╔╦╗    ╦ ╦ ╔═╗ ╦═╗ ╔═╗ ╔═╗
 ║   ╠ ╣ ║║║  ║  ╠═╣ ║    ║     ╠═╣ ╠ ╣ ╠╦╝ ╚═╗ ║╣ 
 ╚═╝ ╚═╝ ╝╚╝  ╩  ╩ ╩ ╚═╝  ╩     ╩ ╩ ╚═╝ ╩╚═ ╚═╝ ╚═╝
     🐎  Welcome to ContactHorse Installer 🐎

EOF
  echo -e "\033[0m"
}

# -------- PROMPT ----------
confirm() {
  local prompt="${1:-Continue?}"
  local default="${2:-N}"
  local reply

  if [ -t 0 ]; then
    read -r -p "$prompt [y/N] " reply
  elif [ -e /dev/tty ]; then
    read -r -p "$prompt [y/N] " reply < /dev/tty
  else
    reply="$default"
  fi

  reply="${reply:-$default}"
  [[ "$reply" =~ ^[Yy]$ ]]
}

# -------- DETECT --------
detect_os() {
  if [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "$ID"
  elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "macos"
  else
    uname -s | tr '[:upper:]' '[:lower:]'
  fi
}

detect_arch() {
  arch=$(uname -m)
  case "$arch" in
    arm64|aarch64) echo "arm" ;;
    x86_64)        echo "x86" ;;
    *)             echo "unknown" ;;
  esac
}

# -------- INSTALLERS --------
install_git() {
  local os_id="$1"
  case "$os_id" in
    amzn|amazon) sudo dnf install -y git ;;
    ubuntu|debian) sudo apt update && sudo apt install -y git ;;
    macos) brew install git ;;
    *) red "❌ Unsupported OS for Git installation: $os_id"; exit 1 ;;
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
    macos)
      if ! command -v brew &>/dev/null; then
        red "Homebrew is required. Please install Homebrew first."
        exit 1
      fi
      brew install --cask docker
      ;;
    *) red "❌ Unsupported OS for Docker install: $os_id"; exit 1 ;;
  esac
}

install_compose_v2() {
  local plugin_dir="/usr/local/lib/docker/cli-plugins"
  sudo mkdir -p "$plugin_dir"
  sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-linux-x86_64 \
    -o "$plugin_dir/docker-compose"
  sudo chmod +x "$plugin_dir/docker-compose"
}

# -------- MAIN --------

banner

OS_ID="$(detect_os)"
ARCH="$(detect_arch)"
blue "🧠 Detected OS: $OS_ID, Architecture: $ARCH"

# --- Git ---
if ! command -v git >/dev/null 2>&1; then
  red "❌ Git not found."
  if confirm "Install Git?"; then
    install_git "$OS_ID"
    green "✅ Git installed."
  else
    red "Git is required. Aborting."
    exit 1
  fi
else
  green "✅ Git already installed."
fi

# --- Docker ---
if ! command -v docker >/dev/null 2>&1; then
  red "❌ Docker not found."
  if confirm "Install Docker?"; then
    install_docker "$OS_ID"
    green "✅ Docker installed."
  else
    red "Docker is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker already installed."
fi

# --- Docker Compose ---
if ! docker compose version >/dev/null 2>&1; then
  red "❌ Docker Compose v2 not found."
  if confirm "Install Compose v2?"; then
    install_compose_v2
    green "✅ Compose v2 installed."
  else
    red "Compose is required. Aborting."
    exit 1
  fi
else
  green "✅ Docker Compose v2 is available."
fi

# --- Docker Socket Test ---
if ! docker info >/dev/null 2>&1; then
  yellow "⚠️  You do not have permission to access Docker socket. Using sudo..."
  DOCKER_CMD="sudo docker"
fi

# --- Clone Repo ---
if [ ! -d "$APP_DIR" ]; then
  green "📥 Cloning $REPO_URL"
  git clone "$REPO_URL" "$APP_DIR"
else
  yellow "📁 $APP_DIR already exists. Using it."
fi

cd "$APP_DIR"

# --- .env File ---
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  green "⚙️ Creating .env from .env.example"
  cp .env.example .env
fi

# --- Run App ---
if [ -f "docker-compose.yml" ]; then
  green "🚀 Starting app with Docker Compose..."
  $DOCKER_CMD compose up -d
  green "✅ App running at http://localhost:3000"
else
  red "❌ docker-compose.yml not found!"
  exit 1
fi
