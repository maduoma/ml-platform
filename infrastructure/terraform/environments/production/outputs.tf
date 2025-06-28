# infrastructure/terraform/environments/production/outputs.tf
# Outputs from the production environment configuration.

output "cluster_name" {
  description = "Name of the production EKS cluster."
  value       = module.kubernetes_cluster.cluster_name
}

output "cluster_endpoint" {
  description = "Endpoint for the production EKS cluster."
  value       = module.kubernetes_cluster.cluster_endpoint
}

output "mlflow_server_ip" {
    description = "Public IP of the production MLflow server."
    value       = module.mlflow_server.mlflow_public_ip
}
