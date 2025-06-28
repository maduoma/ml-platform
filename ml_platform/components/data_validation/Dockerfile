# ml_platform/components/data_validation/Dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN pip install pandas==1.5.3 evidently==0.3.2
COPY validate.py .
