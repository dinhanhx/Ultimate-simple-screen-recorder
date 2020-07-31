import mss
import time
import numpy
from cv2 import cvtColor, COLOR_RGB2BGR, VideoWriter_fourcc, VideoWriter
from keyboard import is_pressed

vobj = VideoWriter("output.avi", VideoWriter_fourcc(*"XVID"), 1.0, (1920, 1080))
monitor = {"top": 0, "left": 0, "width": 1920, "height": 1080}

t0 = time.process_time()
frame = numpy.array(mss.mss().grab(monitor))[:, :, :3]
t1 = time.process_time()
vobj.write(frame)
t2 = time.process_time()

print(t1-t0)
print(t2-t1)

vobj.release()
