# tests/component_tests/test_data_ingestion.py
import pandas as pd
import os
from ml_platform.components.data_ingestion.ingest import ingest_data

def test_ingest_data(tmpdir):
    output_file = os.path.join(tmpdir, 'data.csv')
    ingest_data(output_file)
    assert os.path.exists(output_file)
    df = pd.read_csv(output_file)
    assert 'target' in df.columns
    assert len(df) > 0

