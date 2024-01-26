def download_dataset():
    """
    Downloads the cats_and_dogs dataset.
    """

    import os
    import urllib.request
    import zipfile

    dataset_directory = os.path.join('/', 'pipeline', 'artifacts', 'dataset')
    os.makedirs(dataset_directory)

    dataset_url  = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
    dataset_file = os.path.basename(dataset_url)

    urllib.request.urlretrieve(dataset_url, dataset_file)

    with zipfile.ZipFile(dataset_file, 'r') as dataset_zipfile:

        dataset_zipfile.extractall(dataset_directory)

    os.rename(os.path.join(dataset_directory, 'cats_and_dogs_filtered'), os.path.join(dataset_directory, 'cats_and_dogs'))


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    download_dataset()