# scripts/setup_dev_environment.sh
#!/bin/bash
# Script to set up the local development environment.

echo "Setting up Python virtual environment with Poetry..."

# Check if Python 3.9+ is installed
if ! command -v python3 &> /dev/null || ! python3 -c 'import sys; assert sys.version_info >= (3, 9)' &> /dev/null; then
    echo "Python 3.9+ is required. Please install it."
    exit 1
fi

# Check if Poetry is installed
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed. Installing..."
    curl -sSL https://install.python-poetry.org | python3 -
fi

# Install project dependencies
poetry install

echo "Environment setup complete. Activate with 'poetry shell'"

#--- build_and_push_images.sh ---
# scripts/build_and_push_images.sh
#!/bin/bash
# This script builds and pushes Docker images for the ML components.

set -e # Exit immediately if a command exits with a non-zero status.

# Variables - replace with your container registry details
REGISTRY_URL="your_container_registry_url" # e.g., 123456789012.dkr.ecr.ca-central-1.amazonaws.com
IMAGE_TAG=${1:-latest} # Use the first argument as the tag, or default to 'latest'

# Navigate to the component directory, build, and push
build_and_push() {
  COMPONENT_DIR=$1
  IMAGE_NAME=$2
  
  echo "--- Building ${IMAGE_NAME}:${IMAGE_TAG} from ${COMPONENT_DIR} ---"
  docker build -t "${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}" -f "${COMPONENT_DIR}/Dockerfile" .
  
  echo "--- Pushing ${IMAGE_NAME}:${IMAGE_TAG} to ${REGISTRY_URL} ---"
  docker push "${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}"
}

# Example usage for one component
# In a real scenario, you would loop through all component directories
# build_and_push "ml_platform/components/data_ingestion" "lucid-data-ingestion"

echo "Building and pushing serving image..."
docker build -t "${REGISTRY_URL}/lucid-serving:${IMAGE_TAG}" -f "ml_platform/serving/Dockerfile.serving" .
docker push "${REGISTRY_URL}/lucid-serving:${IMAGE_TAG}"


echo "All images built and pushed successfully."

