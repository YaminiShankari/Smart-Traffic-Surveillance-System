from ultralytics import YOLO
import easyocr
import cv2

model = YOLO("../models/best.pt")
reader = easyocr.Reader(['en'])

def detect_plate(image_path):

    results = model(image_path)

    image = cv2.imread(image_path)

    for result in results:

        boxes = result.boxes.xyxy.cpu().numpy()

        print("Boxes:", boxes)

        for box in boxes:

            x1, y1, x2, y2 = map(int, box)

            plate = image[y1:y2, x1:x2]

            cv2.imwrite("ENTER_THE_ACTUAL_PATH", plate)

            ocr_result = reader.readtext(plate)

            print("OCR Result:", ocr_result)

            if len(ocr_result) > 0:
                return ocr_result[0][1]

    return "No Plate Found"
