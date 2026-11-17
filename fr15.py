'''import cv2
from cv2 import VideoCapture

cam= VideoCapture(0)

while True:
    ret,frame=cam.read()
    cv2.imshow("frame", frame)
    code=cv2.waitKey(1)
    if code>0:
        if chr(code)== "q":
            break
        if chr(code)== "c":
            cv2.imwrite("myimage1.jpg", frame)
cam.release()
cv2.destroyAllWindows()'''
    
import cv2
from cv2 import VideoCapture

cam= VideoCapture(0)
Count=1
while True:
    ret,frame=cam.read()
    cv2.imshow("frame", frame)
    code=cv2.waitKey(1)
    if code>0:
        if chr(code)== "q":
            break
        if chr(code)== "c":
            filename= f'myimage_{Count}.png'
            cv2.imwrite(filename, frame)
            Count=Count+1
            
cam.release()
cv2.destroyAllWindows()
