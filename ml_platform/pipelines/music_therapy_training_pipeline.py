# ml_platform/pipelines/music_therapy_training_pipeline.py
from kfp import dsl
from kfp.components import load_component_from_file

# Load all component definitions
ingestion_op = load_component_from_file('../components/data_ingestion/component.yaml')
validation_op = load_component_from_file('../components/data_validation/component.yaml')
feature_op = load_component_from_file('../components/feature_engineering/component.yaml')
training_op = load_component_from_file('../components/model_training/component.yaml')
evaluation_op = load_component_from_file('../components/model_evaluation/component.yaml')
pusher_op = load_component_from_file('../components/model_pusher/component.yaml')


@dsl.pipeline(
    name='Initial Music Therapy Model Training Pipeline',
    description='The first full pipeline to train and validate the music recommender model.'
)
def music_therapy_initial_training_pipeline():
    # 1. Ingest Data
    ingestion_task = ingestion_op()

    # 2. Validate Data
    validation_task = validation_op(raw_data=ingestion_task.outputs['raw_data'])
    validation_task.after(ingestion_task)

    # 3. Engineer Features
    feature_task = feature_op(raw_data=ingestion_task.outputs['raw_data'])
    feature_task.after(validation_task)

    # 4. Train Model
    training_task = training_op(features=feature_task.outputs['engineered_features'])
    training_task.after(feature_task)

    # 5. Evaluate Model
    evaluation_task = evaluation_op(
        model=training_task.outputs['model'],
        validation_data=feature_task.outputs['engineered_features'] # Using same data for simplicity
    )
    evaluation_task.after(training_task)

    # 6. Push Model to Registry
    pusher_task = pusher_op(model=training_task.outputs['model'])
    pusher_task.after(evaluation_task)


if __name__ == '__main__':
    from kfp.compiler import Compiler
    Compiler().compile(
        pipeline_func=music_therapy_initial_training_pipeline,
        package_path='music_therapy_initial_training_pipeline.yaml'
    )
    print("Initial training pipeline compiled successfully.")
