import picamera
import time 

path = '/home/pi/src6/06_multimedia'

camera = picamera.PiCamera()

camera.resolution=(640, 480)
camera.start_preview()
time.sleep(3)

try:
    while 1:
        n = int (input ('photo:1, video:2, exist:9 >'))
        if n == 1:
            print('사진 촬영')
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.capture('%s/%s.jpg' % (path, now_str))
            
        elif n == 2:
            print('동영상 촬영')
            now_str = time.strftime("%Y%m%d_%H%M%S")
            camera.start_recording('%s/%s.h264' % (path, now_str))
            input('press enter to stop')
            camera.stop_recording()
            
        elif n == 9:
            break


finally:
    camera.stop_preview()