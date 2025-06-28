# ml_platform/components/model_pusher/push_model.py
import argparse
import mlflow

def push_model(model_path: str, model_name: str):
    print(f"Pushing model from {model_path} to MLflow registry as '{model_name}'")
    mlflow.set_tracking_uri("http://your-mlflow-server:5000") # Replace with your MLflow server
    # This is a simplified push. A real one would involve logging the model from a run
    # and then transitioning its stage.
    print("Model pushed successfully (simulation).")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, required=True)
    parser.add_argument('--model_name', type=str, default='lucid-music-recommender')
    args = parser.parse_args()
    push_model(args.model_path, args.model_name)
