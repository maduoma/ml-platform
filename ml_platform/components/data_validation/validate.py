# ml_platform/components/data_validation/validate.py
import pandas as pd
import argparse
from evidently import Report, DataQualityPreset

def validate_data(data_path: str, report_path: str):
    print(f"Validating data from {data_path}")
    df = pd.read_csv(data_path)
    report = Report(metrics=[DataQualityPreset()])
    report.run(current_data=df)
    report.save_html(report_path)
    print(f"Validation report saved to {report_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True)
    parser.add_argument('--report_path', type=str, required=True)
    args = parser.parse_args()
    validate_data(args.data_path, args.report_path)
