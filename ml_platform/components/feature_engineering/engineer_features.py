# ml_platform/components/feature_engineering/engineer_features.py
import pandas as pd
import argparse
import os

def engineer_features(data_path: str, output_path: str):
    print(f"Engineering features for data at {data_path}")
    df = pd.read_csv(data_path)
    df['feature3'] = df['feature1'] * df['feature2']
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Engineered features saved to {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    engineer_features(args.data_path, args.output_path)
