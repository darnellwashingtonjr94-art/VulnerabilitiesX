#!/bin/bash

# Stop execution if any command fails
set -e

# ==========================================
# CONFIGURATION
# Ensure you have exported DOCKERHUB_USERNAME and DOCKERHUB_TOKEN in your terminal!
IMAGE_NAME="vulnerabilitiesx"
TAG="latest"
# ==========================================

# Check if credentials are provided
if [ -z "$DOCKERHUB_USERNAME" ] || [ -z "$DOCKERHUB_TOKEN" ]; then
  echo "❌ Error: DOCKERHUB_USERNAME and DOCKERHUB_TOKEN environment variables must be set."
  exit 1
fi

echo "🔐 Step 1: Logging into Docker Hub..."
echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

echo "🚀 Step 2: Building the Docker image..."
docker build -t $IMAGE_NAME .

echo "🏷️ Step 3: Tagging the image..."
docker tag $IMAGE_NAME $DOCKERHUB_USERNAME/$IMAGE_NAME:$TAG

echo "☁️ Step 4: Pushing to Docker Hub..."
docker push $DOCKERHUB_USERNAME/$IMAGE_NAME:$TAG

echo "✅ Successfully published $DOCKERHUB_USERNAME/$IMAGE_NAME:$TAG to Docker Hub!"
