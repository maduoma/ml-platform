# infrastructure/terraform/environments/staging/outputs.tf
# Outputs from the staging environment configuration.

output "cluster_name" {
  description = "Name of the EKS cluster."
  value       = module.kubernetes_cluster.cluster_name
}

output "cluster_endpoint" {
  description = "Endpoint for the EKS cluster."
  value       = module.kubernetes_cluster.cluster_endpoint
}

output "mlflow_server_ip" {
    description = "Public IP of the MLflow server."
    value       = module.mlflow_server.mlflow_public_ip
}
