# ml_platform/components/model_training/train.py
import pandas as pd
import joblib
import argparse
import os
from sklearn.ensemble import RandomForestClassifier

def train_model(data_path: str, model_path: str):
    print(f"Training model with data from {data_path}")
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--model_path', type=str, required=True)
    args = parser.parse_args()
    train_model(args.data_path, args.model_path)
