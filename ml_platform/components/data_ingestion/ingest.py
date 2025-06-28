# ml_platform/components/data_ingestion/ingest.py
import pandas as pd
import argparse
import os

def ingest_data(output_path: str):
    print("Ingesting data...")
    # In a real scenario, this would pull from a database or API
    data = {
        'feature1': [1.0, 2.1, 0.9, 3.4], 'feature2': [0.5, 0.4, 0.5, 0.6],
        'target': [0, 1, 0, 1]
    }
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output_path', type=str, required=True)
    args = parser.parse_args()
    ingest_data(args.output_path)
