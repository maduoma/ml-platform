# ml_platform/serving/predictors/music_recommender_predictor.py

import kserve
import joblib
import numpy as np
from typing import Dict, List

class MusicRecommenderPredictor(kserve.Model):
    """
    A KServe model implementation for the LUCID music recommender.
    
    This class loads a trained model and uses it to predict therapeutic
    music categories based on input features.
    """
    def __init__(self, name: str, model_path: str):
        """
        Initializes the model.

        Args:
            name (str): The name of the model.
            model_path (str): The path to the trained model file.
        """
        super().__init__(name)
        self.name = name
        self.model_path = model_path
        self.model = None

    def load(self) -> bool:
        """
        Loads the model from the specified path.
        
        KServe calls this method to load the model into memory.
        """
        try:
            print(f"Loading model from: {self.model_path}")
            self.model = joblib.load(self.model_path)
            self.ready = True
            print("Model loaded successfully.")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.ready = False
        return self.ready

    def predict(self, payload: Dict, headers: Dict[str, str] = None) -> Dict:
        """
        Performs inference on the input payload.

        Args:
            payload (Dict): The input request payload. Expected to have an 'instances' key.
            headers (Dict): Request headers.

        Returns:
            Dict: A dictionary containing the prediction results.
        """
        if not self.ready:
            raise RuntimeError("Model is not loaded and not ready for predictions.")
            
        try:
            # The input is expected to be a list of feature vectors
            inputs = np.array(payload["instances"])
            
            # Get predictions from the scikit-learn model
            predictions = self.model.predict(inputs)
            
            # Return predictions in the format KServe expects
            return {"predictions": predictions.tolist()}
        except Exception as e:
            raise RuntimeError(f"Error during prediction: {e}")

if __name__ == "__main__":
    # The entrypoint for the KServe server
    # It expects MODEL_NAME and MODEL_PATH environment variables
    import os
    
    model_name = os.environ.get("MODEL_NAME")
    model_path = os.environ.get("MODEL_PATH")
    
    if not model_name or not model_path:
        raise ValueError("MODEL_NAME and MODEL_PATH environment variables must be set.")

    model = MusicRecommenderPredictor(model_name, model_path)
    model.load()
    kserve.ModelServer().start([model])

    print("Model server started.")