from ultralytics import YOLO
import time
import streamlit as st
import cv2
from pytube import YouTube
import config
import io

model_path = 'models/yolov8s_best.pt'

def load_model(model_path):
    model = YOLO(model_path)
    return model


def display_tracker_options():
    is_display_tracker = True
    if is_display_tracker:
        tracker_type = "bytetrack.yaml"
        return is_display_tracker, tracker_type
    return is_display_tracker, None


def _display_detected_frames(model, st_frame, image, is_display_tracking=None, tracker=None):

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )


def play_youtube_video(model):
    
    source_youtube = st.sidebar.text_input("YouTube Video URL")

    is_display_tracker, tracker = display_tracker_options()

    if st.sidebar.button('Detect Fire'):
        try:
            yt = YouTube(source_youtube)
            stream = yt.streams.filter(file_extension="mp4", res=720).first()
            vid_cap = cv2.VideoCapture(stream.url)

            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(
                                             model,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker,
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))



def play_webcam(model):

    source_webcam = config.WEBCAM_PATH
    is_display_tracker, tracker = display_tracker_options()
    if st.sidebar.button('Detect Fire'):
        try:
            vid_cap = cv2.VideoCapture(source_webcam)
            st_frame = st.empty()
            while (vid_cap.isOpened()):
                success, image = vid_cap.read()
                if success:
                    _display_detected_frames(
                                             model,
                                             st_frame,
                                             image,
                                             is_display_tracker,
                                             tracker,
                                             )
                else:
                    vid_cap.release()
                    break
        except Exception as e:
            st.sidebar.error("Error loading video: " + str(e))

