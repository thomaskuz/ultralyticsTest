from ultralytics import YOLO

model = YOLO("yolov8m.pt")
# model = YOLO("yolov8n.pt")

#run inference on the source
results = model(source=0, show=True, tracker="bytetrack.yaml") # source 0 voor webcam te gebruiken
#tracker zorgt ervoor dat er niet elke keer een nieuwe box wordt gerenderd