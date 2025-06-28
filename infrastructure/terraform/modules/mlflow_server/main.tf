
# --- MLflow Server Module ---
# infrastructure/terraform/modules/mlflow_server/main.tf

resource "aws_security_group" "mlflow_sg" {
  name        = "${var.project_name}-mlflow-sg-${var.environment}"
  description = "Allow inbound traffic for MLflow UI"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "mlflow_server" {
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu 22.04 LTS for ca-central-1
  instance_type = "t2.micro"
  subnet_id     = var.public_subnet_id
  vpc_security_group_ids = [aws_security_group.mlflow_sg.id]
  associate_public_ip_address = true

  # User data to install Docker and run MLflow
  user_data = <<-EOF
              #!/bin/bash
              sudo apt-get update
              sudo apt-get install -y docker.io
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo docker run -d -p 5000:5000 --name mlflow ghcr.io/mlflow/mlflow mlflow server --host 0.0.0.0
              EOF

  tags = {
    Name = "${var.project_name}-mlflow-server-${var.environment}"
  }
}
