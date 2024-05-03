from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
WEBCAM = 'Webcam'
YOUTUBE = 'YouTube'
SOURCES_LIST = [IMAGE, WEBCAM, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'assets/images'
DEFAULT_IMAGE = IMAGES_DIR / 'ates.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'fire_detected.jpg'

# Videos config
'''
VIDEO_DIR = ROOT / 'assets/videos'
VIDEOS_DICT = {
    'video_1': VIDEO_DIR / 'fire.mp4',
    #'video_2': VIDEO_DIR / 'video_2.mp4',
    #'video_3': VIDEO_DIR / 'video_3.mp4',
}
'''
# ML Model config
MODEL_DIR = ROOT / 'models'
DETECTION_MODEL = MODEL_DIR / 'yolov8s_best.pt'


#SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0