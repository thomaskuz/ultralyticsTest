# Import libraries
from vidgear.gears import CamGear
import cv2
from ultralytics import YOLO

# load the model

model = YOLO('yolov8n-seg.pt')


# Video stream
# stream = CamGear(source='https://www.youtube.com/watch?v=1ZupwFOhjl4', stream_mode=True, logging=True).start() # YouTube Video URL as input
stream = CamGear(source='https://www.youtube.com/watch?v=WvhYuDvH17I', stream_mode=True, logging=True).start() # YouTube Video URL as input

# Infinite loop
while True:
    
    frame = stream.read() # read frames

    # Check if frame is None
    if frame is None:
        # If True break the infinite loop
        break
    
    cv2.imshow("Output Frame", frame) # Show output window
    # yolo
    results = model(frame)
    #display the annotated frame
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Inference", annotated_frame)

    # end yolo

    key = cv2.waitKey(1) & 0xFF # Check for 'q' key-press
    if key == ord("q"):
        # If 'q' key-pressed break out
        break

cv2.destroyAllWindows()
stream.stop()
