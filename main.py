import cv2
import laser_tracker
import time


ship_pos = 0

def gstreamer_pipeline(
    capture_width=1280,
    capture_height=720,
    display_width=1280,
    display_height=720,
    framerate=60,
    flip_method=0,
): return (
        "nvarguscamerasrc ! "
        "video/x-raw(memory:NVMM), "
        "width=(int)%d, height=(int)%d, "
        "format=(string)NV12, framerate=(fraction)%d/1 ! "
        "nvvidconv flip-method=%d ! "
        "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
        "videoconvert ! "
        "video/x-raw, format=(string)BGR ! appsink"
        % (
            capture_width,
            capture_height,
            framerate,
            flip_method,
            display_width,
            display_height,
        )
    )


cap = cv2.VideoCapture(gstreamer_pipeline(flip_method=2), cv2.CAP_GSTREAMER)
cap.set(3, 1280)
cap.set(4, 720)


def move_ship(laser_x, laser_y):
    # Ship at (615, 360)

    if laser_x > 625: # right screen
        if laser_y > 542:
            ship_pos = 7
        elif laser_y > 485:
            ship_pos = 6
        elif laser_y > 428:
            ship_pos = 5
        elif laser_y > 371:
            ship_pos = 4
        elif laser_y > 314:
            ship_pos = 3
        elif laser_y > 257:
            ship_pos = 2
        else:
            ship_pos = 1
    elif laser_x < 600: # left screen
        if laser_y > 502:
            ship_pos = 9
        elif laser_y > 445:
            ship_pos = 10
        elif laser_y > 388:
            ship_pos = 11
        elif laser_y > 331:
            ship_pos = 12
        elif laser_y > 274:
            ship_pos = 13
        elif laser_y > 217:
            ship_pos = 14
        else:
            ship_pos = 15
    else: # center screen
        if laser_y < 360:
            ship_pos = 0
        else:
            ship_pos = 8

    return


while(True):
    ret, frame = cap.read()

    laser_coords, radius = laser_tracker.detect(frame)

    if laser_coords is not None:
        laser_x = laser_coords[0]
        laser_y = laser_coords[1]
        if laser_y > 140 and laser_y < 600 and laser_x > 250 and laser_x < 910:
            # print("{0}, {1}".format(laser_x, laser_y))
            move_ship(laser_x, laser_y)
            print(ship_pos)
            #cv2.circle(frame, (int(laser_x), int(laser_y)), int(radius), (0, 255, 255), 2)
            #cv2.imwrite('test.jpg', frame)