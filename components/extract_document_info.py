def extract_document_info(document_file : str):
    """
    Extracts the informations from the document.
    """

    import os
    import pytesseract
    from PIL import Image

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    document_file       = os.path.join(artifacts_directory, document_file)

    ocr = pytesseract.image_to_string(Image.open(document_file))
    print(ocr)

    with open(document_file + '.ocr.txt', 'w') as doc:
        doc.write(ocr)