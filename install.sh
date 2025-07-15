#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/contacthorse/forever-app.git"
APP_DIR="forever-app"

# Colors
green() { echo -e "\033[32m$1\033[0m"; }
red()   { echo -e "\033[31m$1\033[0m"; }

# --- Git Check ---
if ! command -v git >/dev/null 2>&1; then
  red "❌ Git is not installed."
  read -rp "Install Git now? (y/N) " confirm_git
  if [[ "$confirm_git" =~ ^[Yy]$ ]]; then
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
  read -rp "Install Docker + Compose now? (y/N) " confirm_docker
  if [[ "$confirm_docker" =~ ^[Yy]$ ]]; then
    green "📦 Installing Docker..."
    curl -fsSL https://get.docker.com | sudo bash
    sudo usermod -aG docker "$USER"
    newgrp docker
    green "✅ Docker installed."
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
  read -rp "Try to upgrade Docker to get Compose V2? (y/N) " confirm_compose
  if [[ "$confirm_compose" =~ ^[Yy]$ ]]; then
    curl -fsSL https://get.docker.com | sudo bash
    green "✅ Docker (with Compose v2) updated."
  else
    red "🚫 Docker Compose is required. Aborting."
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
  green "✅ App is starting! Visit http://localhost:3000"
else
  red "❌ docker-compose.yml not found. Aborting."
  exit 1
fi
