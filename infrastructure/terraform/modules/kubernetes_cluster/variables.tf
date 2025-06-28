# infrastructure/terraform/modules/kubernetes_cluster/variables.tf
# Add new variables for the GPU node group.

variable "cluster_name" { type = string }
variable "vpc_id" { type = string }
variable "private_subnet_ids" { type = list(string) }

# General instance variables
variable "instance_types" { type = list(string) }
variable "min_size" { type = number }
variable "max_size" { type = number }
variable "desired_size" { type = number }

# NEW: GPU instance variables
variable "gpu_instance_types" {
  description = "List of instance types for the GPU node group."
  type        = list(string)
  default     = ["g4dn.xlarge"]
}
variable "gpu_min_size" {
  type    = number
  default = 0
}
variable "gpu_max_size" {
  type    = number
  default = 2
}
variable "gpu_desired_size" {
  type    = number
  default = 0
}
