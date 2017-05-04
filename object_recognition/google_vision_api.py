#import time, sys
#import numpy as np
#import cozmo
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision

path = os.path.join(
    os.path.dirname(__file__),
    'img/1.jpg')

def detect_labels(path):
    """Detects labels in the file."""
    vision_client = vision.Client()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision_client.image(content=content)

    labels = image.detect_labels()
    print('Labels:')

    for label in labels:
        print(label.description)

if __name__ == '__main__':
    detect_labels(path);
