#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/alleyforge/contacthorse-alpha-app.git"
APP_DIR="ContactHorse"


#  Clone repo if not present
if [ ! -d "$APP_DIR" ]; then
  git clone "$REPO_URL"
  cd "$APP_DIR"
else
  cd "$APP_DIR"
fi

#  Copy .env.example to .env if present and .env does not exist
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  cp .env.example .env
fi

#  Start the app
if [ -f "docker-compose.yml" ]; then
  docker compose up -d
  echo "Waiting for containers to initialize..."
  echo "Please allow 2-3 minutes for the app to start."
else
  echo "docker-compose.yml not found!"
  exit 1
fi

echo "App is starting! Visit http://localhost:3000" 