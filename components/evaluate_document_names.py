def evaluate_document_names(document_cnh : str, document_escritura : str):

    import os

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    document_cnh        = os.path.join(artifacts_directory, document_cnh)
    document_escritura  = os.path.join(artifacts_directory, document_escritura)

    with open(document_cnh, 'r') as file:
        cnh = file.read()

    with open(document_escritura, 'r') as file:
        escritura = file.read()