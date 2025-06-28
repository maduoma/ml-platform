# ml_platform/components/drift_detection/Dockerfile

FROM python:3.9-slim

WORKDIR /app

# Install pandas and evidently
RUN pip install pandas==1.5.3 evidently==0.3.2

COPY detect_drift.py .

ENTRYPOINT ["python", "detect_drift.py"]


