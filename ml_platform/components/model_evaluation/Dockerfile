# ml_platform/components/model_evaluation/Dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN pip install pandas==1.5.3 scikit-learn==1.2.2 joblib==1.2.0
COPY evaluate.py .
