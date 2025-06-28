# --- Outputs ---
# infrastructure/terraform/modules/mlflow_server/outputs.tf
output "mlflow_public_ip" {
  value = aws_instance.mlflow_server.public_ip
}