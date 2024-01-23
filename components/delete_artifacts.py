def delete_artifacts():
    """
    Deletes the pipeline artifacts.
    """

    import os
    import shutil

    shutil.rmtree(os.path.join('/', 'pipeline', 'artifacts'))


if __name__ == '__main__':
    """
    Elyra Pipelines
    """

    delete_artifacts()