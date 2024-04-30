# Yolov8_Fire_Detection



[![Python 3.11.6](https://img.shields.io/badge/python-3.11.6-blue.svg)](https://www.python.org/downloads/release/python-3116/)
[![Git 2.39.1](https://img.shields.io/badge/git-2.39.1-red.svg)](https://git-scm.com/docs/git/2.39.0)


# Fire Detection With Yolov8

## Installation
Download the face detection repository:
`git clone https://github.com/Yusuf-ozen/face_detection_with_yolov8.git` 


Install all necessary library:
`pip install -r requirements.txt` 

Navigate to the project directory:
`cd Yolov8_Fire_Detection` 

## Testing On Real-Time Webcam
Run this code at git bash or cmd:
`python yolov8s_live_test.py` 

## Testing on an Image
Run this code at git bash or cmd and change `/path/image` according your files. Using `--resize_width 400` and `--resize_height 400` the size of output image can change:


`python yolov8s_image_test.py /path/image.jpg --resize_width 400 --resize_height 300` 

![Resim Açıklaması](predicts/images/predict.jpg)


## Testing on a Video
Run this code at git bash or cmd and change `/path/image` according your files. Using `--resize_width 400` and `--resize_height 400` the size of output of the video can change:


`python yolov8s_video_test.py /path/video.mp4 --resize_width 1280 --resize_height 720` 



<br>
<div class="gif">
<p align="center">
<img src='videos/kv_gif.gif' align="center" width=800>
</p>
</div>
</div>



## Referances
https://roboflow.com/

https://github.com/ultralytics/ultralytics
