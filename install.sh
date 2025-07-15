#!/usr/bin/env bash
set -e

REPO_URL="https://github.com/contacthorse/forever-app.git"
APP_DIR="forever-app"

# Clone if not present
if [ ! -d "$APP_DIR" ]; then
  echo "Cloning repository from $REPO_URL"
  git clone "$REPO_URL" "$APP_DIR"
fi

cd "$APP_DIR"

# Copy .env if needed
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
  echo "Creating .env from .env.example"
  cp .env.example .env
fi

# Start app
if [ -f "docker-compose.yml" ]; then
  echo "Starting app using Docker Compose..."
  docker compose up -d
  echo "App is starting! Served at http://localhost:3000"
else
  echo "docker-compose.yml not found!"
  exit 1
fi
