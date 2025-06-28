# tests/pipeline_tests/test_training_pipeline.py
from ml_platform.pipelines.music_therapy_training_pipeline import music_therapy_initial_training_pipeline

def test_pipeline_compiles():
    from kfp.compiler import Compiler
    try:
        Compiler().compile(
            pipeline_func=music_therapy_initial_training_pipeline,
            package_path='test_compile.yaml'
        )
    except Exception as e:
        assert False, f"Pipeline compilation failed: {e}"

