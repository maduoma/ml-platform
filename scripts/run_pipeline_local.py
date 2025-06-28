# scripts/run_pipeline_local.py
import kfp
from kfp.compiler import Compiler

# Import the pipeline function
from ml_platform.pipelines.music_therapy_training_pipeline import music_therapy_initial_training_pipeline

def main():
    """Compiles and runs a Kubeflow pipeline."""
    # This script is for local compilation. Running requires a KFP client configured
    # to connect to a Kubeflow deployment.

    pipeline_func = music_therapy_initial_training_pipeline
    pipeline_filename = f"{pipeline_func.__name__}.yaml"

    print(f"Compiling pipeline to {pipeline_filename}...")
    Compiler().compile(pipeline_func=pipeline_func, package_path=pipeline_filename)
    print("Compilation successful.")

    # Example of how you would run it
    # client = kfp.Client(host='http://your-kubeflow-url')
    # experiment = client.create_experiment(name='lucid-local-runs')
    # run = client.run_pipeline(
    #     experiment.id,
    #     'initial-training-run',
    #     pipeline_filename
    # )
    # print(f"Run started: {run.id}")

if __name__ == '__main__':
    main()