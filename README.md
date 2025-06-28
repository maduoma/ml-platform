# README.md
# Lucid ML Platform

This repository contains the code for the Machine Learning Platform at LUCID Therapeutics. It provides the infrastructure, pipelines, and tools to streamline the entire machine learning model lifecycle.

## Project Structure

- **`.github/workflows`**: CI/CD pipelines using GitHub Actions.
- **`infrastructure/`**: Infrastructure as Code (Terraform, Helm) for provisioning cloud resources.
- **`ml_platform/`**: Core source code for Kubeflow components, pipelines, and model serving.
- **`notebooks/`**: Jupyter notebooks for experimentation and analysis.
- **`scripts/`**: Utility scripts for developers.
- **`tests/`**: Unit and integration tests.

## Getting Started

1.  **Prerequisites**:
    * Python 3.9+
    * Terraform
    * Docker
    * kubectl
    * Helm

2.  **Setup Development Environment**:
    Run the setup script to create a virtual environment and install dependencies.
    ```bash
    make setup
    ```

3.  **Activate Virtual Environment**:
    ```bash
    poetry shell
    ```

## Infrastructure Deployment

The infrastructure is managed with Terraform.

1.  Navigate to the environment directory:
    ```bash
    cd infrastructure/terraform/environments/staging
    ```

2.  Initialize Terraform:
    ```bash
    terraform init
    ```

3.  Apply the configuration:
    ```bash
    terraform apply
    