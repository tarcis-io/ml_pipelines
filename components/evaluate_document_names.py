def evaluate_document_names(document_cnh : str, document_escritura : str) -> int:

    import os

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    document_cnh        = os.path.join(artifacts_directory, document_cnh)
    document_escritura  = os.path.join(artifacts_directory, document_escritura)

    with open(document_cnh + '.ocr.txt', 'r') as file:
        cnh_name = file.read()

    with open(document_escritura + '.ocr.txt', 'r') as file:
        escritura = file.read()

    if not cnh_name:
        return -1

    if not escritura:
        return -1

    if cnh_name.lower() not in escritura.lower():
        return -1

    return 0