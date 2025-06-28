# infrastructure/terraform/modules/kubernetes_cluster/main.tf
# Note: This is an update to the existing file.

# Using the official AWS EKS module for simplicity and robustness
# See: https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest
module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "19.15.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.27"

  vpc_id     = var.vpc_id
  subnet_ids = var.private_subnet_ids

  eks_managed_node_groups = {
    # Existing general purpose node group
    general = {
      instance_types = var.instance_types
      min_size     = var.min_size
      max_size     = var.max_size
      desired_size = var.desired_size
    }
    # NEW: GPU-enabled node group for ML training
    gpu_training = {
      instance_types = var.gpu_instance_types
      min_size     = var.gpu_min_size
      max_size     = var.gpu_max_size
      desired_size = var.gpu_desired_size

      # Use an AMI optimized for EKS with GPU drivers
      ami_type = "AL2_x86_64_GPU"

      # Taints ensure only pods that tolerate GPUs will schedule here
      taints = [{
        key    = "nvidia.com/gpu"
        value  = "true"
        effect = "NO_SCHEDULE"
      }]

      labels = {
        "node-type" = "gpu-training"
      }
    }
  }
}
