#!/usr/bin/env python3
import freenect
import cv2
import frame_convert2

cv2.namedWindow('Depth')
cv2.namedWindow('Video')
print('Press ESC in window to stop')


def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth_with_res(format = freenect.DEPTH_11BIT)[0])


def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video_with_res(resolution=freenect.RESOLUTION_HIGH)[0])


while 1:
    cv2.imshow('Depth', get_depth())
    cv2.imshow('Video', get_video())
    if cv2.waitKey(10) == 27:
        break
