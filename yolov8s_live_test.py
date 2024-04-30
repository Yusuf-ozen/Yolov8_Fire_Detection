from ultralytics import YOLO
import cv2

model = YOLO("models/yolov8s_best.pt")
cap = cv2.VideoCapture(0)


while cap.isOpened():
    
    success, frame = cap.read()


    if success:
        results = model(frame)

        
        annotated_frame = results[0].plot()

        
        cv2.imshow('YOLOv8 Inference', annotated_frame)

        
        if cv2.waitKey(1) == 13:  
            break
    else:
        
        break



cap.release()
cv2.destroyAllWindows()