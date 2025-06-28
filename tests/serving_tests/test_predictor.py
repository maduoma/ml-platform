# tests/serving_tests/test_predictor.py
import numpy as np
from ml_platform.serving.predictors.music_recommender_predictor import MusicRecommenderPredictor
import joblib
import os

def test_predictor(tmpdir):
    # Create a dummy model file
    model_path = os.path.join(tmpdir, 'model.joblib')
    dummy_model = "dummy model object"
    joblib.dump(dummy_model, model_path)

    # Mock the joblib.load to not depend on a real model
    class MockModel:
        def predict(self, data):
            return np.array([1] * len(data))

    joblib.load = lambda path: MockModel()

    predictor = MusicRecommenderPredictor(name="test-model", model_path=model_path)
    predictor.load()

    assert predictor.ready

    payload = {'instances': [[1, 2, 3], [4, 5, 6]]}
    result = predictor.predict(payload)

    assert 'predictions' in result
    assert result['predictions'] == [1, 1]
