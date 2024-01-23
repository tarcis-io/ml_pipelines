def prepare_dataset():
    """
    Prepares the cats_and_dogs dataset for training.
    """

    import os
    import random
    import shutil

    dataset_directory                 = os.path.join('/', 'pipeline', 'artifacts', 'dataset', 'cats_and_dogs')
    dataset_validation_directory      = os.path.join(dataset_directory, 'validation')
    dataset_validation_cats_directory = os.path.join(dataset_validation_directory, 'cats')
    dataset_validation_dogs_directory = os.path.join(dataset_validation_directory, 'dogs')
    dataset_test_directory            = os.path.join(dataset_directory, 'test')
    dataset_test_cats_directory       = os.path.join(dataset_test_directory, 'cats')
    dataset_test_dogs_directory       = os.path.join(dataset_test_directory, 'dogs')

    os.makedirs(dataset_test_cats_directory)
    os.makedirs(dataset_test_dogs_directory)

    number_of_files = 100

    for _ in range(number_of_files):

        file = os.path.join(dataset_validation_cats_directory, random.choice(os.listdir(dataset_validation_cats_directory)))
        shutil.move(file, dataset_test_cats_directory)

        file = os.path.join(dataset_validation_dogs_directory, random.choice(os.listdir(dataset_validation_dogs_directory)))
        shutil.move(file, dataset_test_dogs_directory)


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    prepare_dataset()