def extract_document_info_escritura(document_file : str, tesseract_config : str):
    """
    Extracts the information from the ESCRITURA document.
    """

    import cv2
    import os
    import pytesseract

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    document_file       = os.path.join(artifacts_directory, document_file)

    image = cv2.imread(document_file)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ocr  = pytesseract.image_to_string(image, config = tesseract_config)
    print(ocr)

    with open(document_file + '.ocr.txt', 'w') as doc:
        doc.write(ocr)