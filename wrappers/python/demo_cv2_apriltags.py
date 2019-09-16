#!/usr/bin/env python3
import freenect
import cv2
import frame_convert2
import numpy as np
from apriltag import apriltag

cv2.namedWindow('Video')
print('Press ESC in window to stop')

def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video_with_res(resolution=freenect.RESOLUTION_HIGH)[0])

freenect.init()
freenect.sync_get_video_with_res(resolution=freenect.RESOLUTION_HIGH)
freenect.sync_set_autoexposure(False)
freenect.sync_set_whitebalance(False)

detector = apriltag("tag36h11", threads=4, decimate=2.0)

object_points = np.array([[-0.1,-0.1,0.0],
                          [0.1, -0.1, 0.0],
                          [0.1, 0.1, 0.0],
                          [-0.1, 0.1, 0.0]],dtype = "double")
camera_matrix = np.array([[1.09194704e+03, 0.00000000e+00, 6.79986322e+02],
                          [0.00000000e+00, 1.09300427e+03, 5.09471427e+02],
                          [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]], dtype = "double")

dist_coeffs = np.array([0.17099743, -0.24604911,  0.00678919,  0.01108217,  0.02124964])
#dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
while 1:
    image = get_video()
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = detector.detect(image_gray)
    if(len(detections)>1):
        for tag in detections:
            if(tag['id']==9):
                print(tag['id'])
                #print(tag)
                image_points = tag['lb-rb-rt-lt']
                print(image_points)
                (success, rotation_vector, translation_vector) = cv2.solvePnP(object_points, image_points, camera_matrix, dist_coeffs, flags=cv2.SOLVEPNP_ITERATIVE)
                if(success):
                    print(rotation_vector)
                    print(translation_vector)
    cv2.imshow('Video', image)
    if cv2.waitKey(10) == 27:
        break
cv2.CV