def train_model():
    """
    Trains the model using the cats_and_dogs dataset.
    """

    import os
    import tensorflow as tf

    artifacts_directory          = os.path.join('/', 'pipeline', 'artifacts')
    dataset_directory            = os.path.join(artifacts_directory, 'dataset', 'cats_and_dogs')
    dataset_train_directory      = os.path.join(dataset_directory, 'train')
    dataset_validation_directory = os.path.join(dataset_directory, 'validation')

    image_size = (160, 160)

    dataset_train = tf.keras.preprocessing.image_dataset_from_directory(
        directory  = dataset_train_directory,
        image_size = image_size
    )

    dataset_validation = tf.keras.preprocessing.image_dataset_from_directory(
        directory  = dataset_validation_directory,
        image_size = image_size
    )

    model_directory = os.path.join(artifacts_directory, 'model', 'cats_and_dogs')
    model           = tf.keras.models.load_model(model_directory)

    model.fit(
        dataset_train,
        validation_data = dataset_validation,
        epochs          = 10,
        verbose         = 2
    )

    model.save(model_directory)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tensorflow==2.15.0'])

    train_model()