# ml_platform/pipelines/drift_retraining_pipeline.py
# This Kubeflow pipeline defines the complete retraining workflow.

from kfp import dsl
from kfp.components import load_component_from_file

# Load component definitions from their YAML files
# Note: The component spec files for these would need to be created similarly
# to the drift_detection one. This is a structural representation.
data_ingestion_op = load_component_from_file('../components/data_ingestion/component.yaml')
feature_engineering_op = load_component_from_file('../components/feature_engineering/component.yaml')
model_training_op = load_component_from_file('../components/model_training/component.yaml')
model_evaluation_op = load_component_from_file('../components/model_evaluation/component.yaml')
model_pusher_op = load_component_from_file('../components/model_pusher/component.yaml')
drift_detection_op = load_component_from_file('../components/drift_detection/component.yaml')

@dsl.pipeline(
    name='Music Therapy Model Retraining Pipeline',
    description='A pipeline that retrains, evaluates, and validates the model upon drift detection.'
)
def music_therapy_retraining_pipeline(
    api_endpoint: str = "https://example.com/api/new_data" # Parameter for new data source
):
    """
    Defines the pipeline steps for retraining.
    """
    # 1. Ingest new data
    ingestion_task = data_ingestion_op(api_endpoint=api_endpoint)

    # 2. Engineer features from the new data
    feature_engineering_task = feature_engineering_op(
        raw_data=ingestion_task.outputs['raw_data']
    )

    # 3. Train a new model candidate
    training_task = model_training_op(
        features=feature_engineering_task.outputs['engineered_features']
    )

    # 4. Evaluate the new model against a validation set
    evaluation_task = model_evaluation_op(
        model=training_task.outputs['model'],
        validation_data=feature_engineering_task.outputs['validation_set']
    )

    # 5. Push the model to the registry if it performs well
    # This step would contain logic to decide if the new model is better
    # than the currently deployed one.
    with dsl.Condition(evaluation_task.outputs['is_better_than_production'] == True):
        pusher_task = model_pusher_op(
            model=evaluation_task.outputs['blessed_model']
        )
        pusher_task.after(evaluation_task)

if __name__ == '__main__':
    from kfp.compiler import Compiler
    Compiler().compile(
        pipeline_func=music_therapy_retraining_pipeline,
        package_path='music_therapy_retraining_pipeline.yaml'
    )
    print("Retraining pipeline compiled successfully.")
