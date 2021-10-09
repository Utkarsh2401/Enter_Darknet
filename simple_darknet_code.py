import numpy as np
import darknet
import cv2
import random

network, class_names, class_colors = darknet.load_network('/home/andros/darknet/cfg/yolov4.cfg','/home/andros/darknet/cfg/coco.data','/home/andros/darknet/yolov4.weights', batch_size=1)
darknet_width = darknet.network_width(network)
darknet_height = darknet.network_height(network)

input_path = input("Enter input path: ")
if input_path:
    cap = cv2.VideoCapture(input_path)
else:
    cap = cv2.VideoCapture(0)

while (cap.isOpened()):

    _,frame = cap.read()
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_resized = cv2.resize(frame_rgb, (darknet_width, darknet_height), interpolation=cv2.INTER_LINEAR)
    img_for_detect = darknet.make_image(darknet_width, darknet_height, 3)
    darknet.copy_image_from_bytes(img_for_detect, frame_resized.tobytes())

    detection = darknet.detect_image(network, class_names, img_for_detect, thresh = 0.25)
    darknet.print_detections(detection, True)

    image = darknet.draw_boxes(detection, frame, class_colors)
    cv2.imshow('Inference', image)

    cv2.waitKey(10)
cv2.destroyAllWindows()
cap.release()
       

