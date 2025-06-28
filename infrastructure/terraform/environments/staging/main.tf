# infrastructure/terraform/environments/staging/main.tf
# Update the module call to pass GPU parameters.

# Module to create the EKS (Kubernetes) cluster
module "kubernetes_cluster" {
  source = "../../modules/kubernetes_cluster"

  cluster_name    = "${var.project_name}-cluster-staging"
  vpc_id          = module.networking.vpc_id
  private_subnet_ids = module.networking.private_subnet_ids

  # General purpose nodes
  instance_types  = ["t3.medium"]
  min_size        = 2
  max_size        = 5
  desired_size    = 3

  # NEW: GPU nodes (starts at 0 and scales up when needed)
  gpu_instance_types = ["g4dn.xlarge"]
  gpu_min_size       = 0
  gpu_max_size       = 2
  gpu_desired_size   = 0
}


