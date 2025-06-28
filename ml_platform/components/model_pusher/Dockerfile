# ml_platform/components/model_pusher/Dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN pip install mlflow==2.3.2
COPY push_model.py .
