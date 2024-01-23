def download_dataset():
    """
    Downloads the cats_and_dogs dataset.
    """

    import os
    import urllib.request
    import zipfile

    dataset_directory = os.path.join('/', 'pipeline', 'artifacts', 'dataset')
    os.makedirs(dataset_directory)

    url  = 'https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip'
    file = os.path.basename(url)

    urllib.request.urlretrieve(url, file)

    with zipfile.ZipFile(file, 'r') as zip_file:

        zip_file.extractall(dataset_directory)

    os.rename(os.path.join(dataset_directory, 'cats_and_dogs_filtered'), os.path.join(dataset_directory, 'cats_and_dogs'))


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    download_dataset()