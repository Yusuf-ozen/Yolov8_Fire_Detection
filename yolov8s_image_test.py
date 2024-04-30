import argparse
import os
from ultralytics import YOLO
import cv2
from datetime import datetime

def main(image_path, resize_width, resize_height):
    model = YOLO("models/yolov8s_best.pt")

    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (resize_width, resize_height))

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow('YOLOv8 Inference', annotated_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    output_dir = "predicts_yolov8/images"
    os.makedirs(output_dir, exist_ok=True)


    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


    output_path = os.path.join(output_dir, f"predict_{timestamp}.jpg")
    cv2.imwrite(output_path, annotated_frame)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='YOLOv8 Inference')
    parser.add_argument('image_path', type=str, help='Path to the image')
    parser.add_argument('--resize_width', type=int, default=800, help='Resized image width')
    parser.add_argument('--resize_height', type=int, default=600, help='Resized image height')
    args = parser.parse_args()

    main(args.image_path, args.resize_width, args.resize_height)
