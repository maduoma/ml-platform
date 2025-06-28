# scripts/build_and_push_images.sh
# This script automates the building and pushing of Docker images for all
# ML platform components to a container registry.

set -e # Exit immediately if a command exits with a non-zero status.

# --- Configuration ---
# Replace with your actual container registry URL.
# For AWS ECR, it looks like: 123456789012.dkr.ecr.ca-central-1.amazonaws.com
# For Google GCR, it looks like: gcr.io/your-gcp-project-id
REGISTRY_URL="your_container_registry_url"

# Use the first command-line argument as the image tag, or default to "latest".
IMAGE_TAG=${1:-latest}

# Get the absolute path of the script's directory
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PROJECT_ROOT=$(realpath "$SCRIPT_DIR/..")

# --- Helper Function ---
# Builds a Docker image and pushes it to the configured registry.
# Arguments:
#   $1: The directory containing the Dockerfile and source code.
#   $2: The name of the image to build (without the registry URL).
build_and_push() {
  local component_dir=$1
  local image_name=$2
  local full_image_name="${REGISTRY_URL}/${image_name}:${IMAGE_TAG}"

  echo "--------------------------------------------------"
  echo "Processing Component: ${image_name}"
  echo "Directory: ${component_dir}"
  echo "Full Image Name: ${full_image_name}"
  echo "--------------------------------------------------"

  docker build -t "${full_image_name}" -f "${component_dir}/Dockerfile" "${PROJECT_ROOT}"

  echo "Pushing image: ${full_image_name}"
  docker push "${full_image_name}"
  echo "Push complete for ${image_name}."
  echo ""
}

# --- Build and Push All Components ---
echo "Starting build and push process for all components..."

# Loop through each component directory in ml_platform/components
for component in $(ls -d "${PROJECT_ROOT}/ml_platform/components"/*/); do
    # Get the component name from the directory path (e.g., "data_ingestion")
    component_name=$(basename "${component}")
    # Create the image name (e.g., "lucid-data-ingestion")
    image_name="lucid-${component_name}"
    build_and_push "${component}" "${image_name}"
done

# Build the main serving image
build_and_push "${PROJECT_ROOT}/ml_platform/serving" "lucid-serving"

echo "=================================================="
echo "All images have been built and pushed successfully."
echo "=================================================="
