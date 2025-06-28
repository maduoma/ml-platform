# infrastructure/terraform/environments/production/main.tf
# Main configuration for the production environment.

provider "aws" {
  region = var.aws_region
}

# Module to create the VPC and networking resources
module "networking" {
  source = "../../modules/networking"

  vpc_name = "${var.project_name}-vpc-production"
  vpc_cidr = "10.1.0.0/16"
  public_subnets  = ["10.1.1.0/24", "10.1.2.0/24", "10.1.3.0/24"]
  private_subnets = ["10.1.101.0/24", "10.1.102.0/24", "10.1.103.0/24"]
  availability_zones = ["ca-central-1a", "ca-central-1b", "ca-central-1d"]
}

# Module to create the EKS (Kubernetes) cluster
module "kubernetes_cluster" {
  source = "../../modules/kubernetes_cluster"

  cluster_name    = "${var.project_name}-cluster-production"
  vpc_id          = module.networking.vpc_id
  private_subnet_ids = module.networking.private_subnet_ids

  # Larger instances for production workloads
  instance_types  = ["m5.large"]
  min_size        = 3
  max_size        = 10
  desired_size    = 3

  # Production GPU nodes
  gpu_instance_types = ["g4dn.xlarge"]
  gpu_min_size       = 1
  gpu_max_size       = 5
  gpu_desired_size   = 1
}

# Module for a production-grade MLflow server (e.g., using RDS backend)
module "mlflow_server" {
    source = "../../modules/mlflow_server"

    project_name = var.project_name
    environment  = "production"
    vpc_id       = module.networking.vpc_id
    public_subnet_id = module.networking.public_subnet_ids[0]
    # In production, you would configure RDS for the backend store and S3 for artifacts
}
