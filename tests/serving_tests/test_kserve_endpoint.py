# tests/serving_tests/test_kserve_endpoint.py
import requests
import pytest

# This test requires a running KServe endpoint. It should be tagged appropriately.
# KSERVE_ENDPOINT = "[http://music-recommender.your-namespace.example.com/v1/models/music-recommender:predict](http://music-recommender.your-namespace.example.com/v1/models/music-recommender:predict)"
KSERVE_ENDPOINT = "" # Set this env var to run the test

@pytest.mark.skipif(not KSERVE_ENDPOINT, reason="KSERVE_ENDPOINT environment variable not set")
def test_kserve_endpoint():
    payload = {
        "instances": [
            [1.0, 0.5, 0.5] # Example features
        ]
    }
    response = requests.post(KSERVE_ENDPOINT, json=payload)
    
    assert response.status_code == 200
    response_json = response.json()
    assert 'predictions' in response_json
    assert isinstance(response_json['predictions'], list)
