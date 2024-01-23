def evaluate_model():
    """
    Evaluates the model using the cats_and_dogs test dataset.
    """

    import os
    import tensorflow as tf

    artifacts_directory    = os.path.join('/', 'pipeline', 'artifacts')
    dataset_test_directory = os.path.join(artifacts_directory, 'dataset', 'cats_and_dogs', 'test')

    image_size = (160, 160)

    dataset_test = tf.keras.preprocessing.image_dataset_from_directory(
        directory  = dataset_test_directory,
        image_size = image_size
    )

    model_directory = os.path.join(artifacts_directory, 'model', 'cats_and_dogs')
    model           = tf.keras.models.load_model(model_directory)

    model.evaluate(dataset_test, verbose = 2)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tensorflow==2.15.0'])

    evaluate_model()