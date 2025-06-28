# tests/component_tests/test_feature_engineering.py
import pandas as pd
import os
from ml_platform.components.feature_engineering.engineer_features import engineer_features

def test_engineer_features(tmpdir):
    input_file = os.path.join(tmpdir, 'input.csv')
    output_file = os.path.join(tmpdir, 'output.csv')

    data = {'feature1': [1.0, 2.0], 'feature2': [3.0, 4.0]}
    pd.DataFrame(data).to_csv(input_file, index=False)

    engineer_features(input_file, output_file)

    assert os.path.exists(output_file)
    df = pd.read_csv(output_file)
    assert 'feature3' in df.columns
    assert df['feature3'][0] == 3.0
    assert df['feature3'][1] == 8.0
