# ml_platform/components/model_evaluation/evaluate.py
import pandas as pd
import joblib
import argparse
from sklearn.metrics import accuracy_score, roc_auc_score

def evaluate_model(data_path: str, model_path: str):
    print(f"Evaluating model {model_path} with data from {data_path}")
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    y = df['target']
    model = joblib.load(model_path)
    preds = model.predict(X)
    pred_proba = model.predict_proba(X)[:, 1]
    accuracy = accuracy_score(y, preds)
    auc = roc_auc_score(y, pred_proba)
    print(f"Accuracy: {accuracy}")
    print(f"AUC: {auc}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--model_path', type=str, required=True)
    args = parser.parse_args()
    evaluate_model(args.data_path, args.model_path)
