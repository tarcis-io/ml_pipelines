def create_model():
    """
    Creates the Convolutional Neural Network model for binary image classification.
    """

    import os
    import tensorflow as tf

    model_directory = os.path.join('/', 'pipeline', 'artifacts', 'model', 'cats_and_dogs')
    os.makedirs(model_directory)

    model = tf.keras.models.Sequential([
        tf.keras.layers.Rescaling(
            name        = 'layer_0',
            scale       = 1. / 255.,
            input_shape = (160, 160, 3)
        ),
        tf.keras.layers.Conv2D(
            name        = 'layer_1',
            filters     = 16,
            kernel_size = 3,
            activation  = 'relu'
        ),
        tf.keras.layers.MaxPooling2D(
            name = 'layer_2'
        ),
        tf.keras.layers.Conv2D(
            name        = 'layer_3',
            filters     = 32,
            kernel_size = 3,
            activation  = 'relu'
        ),
        tf.keras.layers.MaxPooling2D(
            name = 'layer_4'
        ),
        tf.keras.layers.Conv2D(
            name        = 'layer_5',
            filters     = 64,
            kernel_size = 3,
            activation  = 'relu'
        ),
        tf.keras.layers.MaxPooling2D(
            name = 'layer_6'
        ),
        tf.keras.layers.Flatten(
            name = 'layer_7'
        ),
        tf.keras.layers.Dense(
            name       = 'layer_8',
            units      = 128,
            activation = 'relu'
        ),
        tf.keras.layers.Dense(
            name       = 'layer_9',
            units      = 1,
            activation = 'sigmoid'
        )
    ])

    model.compile(
        loss      = 'binary_crossentropy',
        optimizer = 'adam',
        metrics   = ['accuracy']
    )

    model.summary()
    model.save(model_directory)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    import subprocess
    import sys

    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tensorflow==2.15.0'])

    create_model()