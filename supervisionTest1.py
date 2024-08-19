import cv2
import supervision as sv
from ultralytics import YOLO
from inference import get_model

image = cv2.imread("bus.jpg")
model = YOLO('yolov8n.pt')
result = model(image)[0]
detections = sv.Detections.from_ultralytics(result)

box_annotator = sv.BoxAnnotator()
annotated_frame = box_annotator.annotate(
    scene=image.copy(),
    detections=detections
)

len(detections)
# 5