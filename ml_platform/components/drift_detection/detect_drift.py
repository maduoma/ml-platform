# ml_platform/components/drift_detection/detect_drift.py
# This script uses Evidently AI to generate a data drift report.

import argparse
import pandas as pd
from evidently import Report, DataDriftPreset

def detect_data_drift(reference_data_path: str, current_data_path: str, report_path: str):
    """
    Generates a data drift report comparing reference and current datasets.

    Args:
        reference_data_path (str): Path to the reference data (CSV).
        current_data_path (str): Path to the current data (CSV).
        report_path (str): Path to save the output HTML report.
    """
    print(f"Loading reference data from {reference_data_path}")
    reference_df = pd.read_csv(reference_data_path)

    print(f"Loading current data from {current_data_path}")
    current_df = pd.read_csv(current_data_path)

    print("Generating Data Drift report...")
    data_drift_report = Report(metrics=[
        DataDriftPreset(),
    ])
    
    # Assuming the target column is named 'target'
    # In a real scenario, this would be more robust.
    target_column = 'target'
    if target_column in reference_df.columns and target_column in current_df.columns:
         data_drift_report.run(reference_data=reference_df, current_data=current_df, column_mapping=None)
    else:
         data_drift_report.run(reference_data=reference_df, current_data=current_df)


    print(f"Saving report to {report_path}")
    data_drift_report.save_html(report_path)

    # Example of checking drift status
    report_dict = data_drift_report.as_dict()
    is_drift_detected = report_dict['metrics'][0]['result']['dataset_drift']
    
    print(f"Drift detected: {is_drift_detected}")
    # You could use this boolean to make decisions in the pipeline.

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Detect data drift.")
    parser.add_argument('--reference_data', type=str, required=True, help='Path to reference dataset.')
    parser.add_argument('--current_data', type=str, required=True, help='Path to current dataset.')
    parser.add_argument('--report_path', type=str, required=True, help='Path to save the HTML report.')

    args = parser.parse_args()
    detect_data_drift(args.reference_data, args.current_data, args.report_path)
