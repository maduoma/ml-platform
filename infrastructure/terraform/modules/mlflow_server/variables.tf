# --- Variables ---
# infrastructure/terraform/modules/mlflow_server/variables.tf
variable "project_name" { type = string }
variable "environment" { type = string }
variable "vpc_id" { type = string }
variable "public_subnet_id" { type = string }
