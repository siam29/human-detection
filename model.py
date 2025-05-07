import cv2

# Load pre-trained Haar cascade classifier
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

def detect_humans(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

    for (x, y, w, h) in humans:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    output_image = "output.jpg"
    cv2.imwrite(output_image, img)

    return output_image, humans


# from ultralytics import YOLO
# import cv2

# # Load pre-trained YOLOv8 model (you can choose a smaller version if needed)
# model = YOLO("yolov8n.pt")  # 'n' stands for Nano, use 's' or 'm' for more accuracy

# def detect_humans(image_path):
#     results = model(image_path)

#     # Read original image
#     img = cv2.imread(image_path)

#     # Draw boxes for detected humans (class 0 = 'person')
#     for r in results:
#         for box in r.boxes:
#             cls = int(box.cls[0])
#             if cls == 0:  # class 0 is 'person' in COCO dataset
#                 x1, y1, x2, y2 = map(int, box.xyxy[0])
#                 cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

#     output_image = "output.jpg"
#     cv2.imwrite(output_image, img)
#     return output_image, results
