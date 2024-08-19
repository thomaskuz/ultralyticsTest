from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # Load an official Detect model

results = model.track(source="https://youtu.be/LNwODJXcvt4", stream=True, show=True)  # Tracking with default tracker
# results = model.track("https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker