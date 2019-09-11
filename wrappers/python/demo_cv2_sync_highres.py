#!/usr/bin/env python3
import freenect
import cv2
import frame_convert2

cv2.namedWindow('Depth')
cv2.namedWindow('Video')
print('Press ESC in window to stop')

def get_depth():
    return frame_convert2.pretty_depth_cv(freenect.sync_get_depth_with_res(format = freenect.DEPTH_REGISTERED)[0])

def get_video():
    return frame_convert2.video_cv(freenect.sync_get_video_with_res(resolution=freenect.RESOLUTION_HIGH)[0])

freenect.init()
freenect.sync_get_video_with_res(resolution=freenect.RESOLUTION_HIGH)
freenect.sync_set_autoexposure(False)
freenect.sync_set_whitebalance(False)

while 1:
    depth_gray = get_depth()
    depth_color = cv2.applyColorMap(depth_gray,cv2.COLORMAP_JET)
    cv2.imshow('Depth', depth_color)
    cv2.imshow('Video', get_video())
    if cv2.waitKey(10) == 27:
        break
