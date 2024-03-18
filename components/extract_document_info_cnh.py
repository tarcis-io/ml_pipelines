def extract_document_info_cnh(document_file : str, tesseract_config : str):
    """
    Extracts the 'Nome' information from the CNH document.
    """

    import cv2
    import os
    import pytesseract

    artifacts_directory = os.path.join('/', 'pipeline', 'artifacts')
    document_file       = os.path.join(artifacts_directory, document_file)

    image        = cv2.imread(document_file)
    gray         = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 127, 255, 0)
    contours, _  = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    height, width, _ = image.shape
    image_area       = width * height

    nome = ''

    for contour in contours:

        area = cv2.contourArea(contour)

        if area > image_area * 0.8 or area < image_area * 0.003:
            continue

        x, y, w, h     = cv2.boundingRect(contour)
        x0, x1, y0, y1 = x, x + w, y - 8, y + h

        if y0 < 0:
            y0 = 0

        img = image[y0:y1, x0:x1]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ocr = pytesseract.image_to_string(img, config = tesseract_config)
        ocr = ocr.lower()

        if not any(word in ocr for word in ['nome', 'ome', 'nom']):
            continue

        img  = image[y + 3:y + h - 4, x + 4: x + w - 6]
        img  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ocr  = pytesseract.image_to_string(img, config = tesseract_config)
        ocr  = list(filter(None, ocr.splitlines()))
        nome = ocr[-1]

    print('Nome: {}'.format(nome))

    with open(document_file + 'ocr.txt', 'w') as doc:
        doc.write(nome)