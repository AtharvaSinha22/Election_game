import cv2
import numpy as np
myimage = cv2.imread('download.jpg', cv2.IMREAD_COLOR)

cv2.line(myimage, (50,50), (100,100), (255,0,0),2)
cv2.circle(myimage, (50,50), 25, (255,0,0),2)
cv2.rectangle(myimage, (50,50), (100,100), (255,0,0),2)
points_array = np.array([[50,50] , [60,90] , [80,90]] , np.int32)
cv2.polylines(myimage,  [points_array], True, [255,255,255,],2)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(myimage, "Atharva", [50,150], font,2,[255,255,0],5,cv2.LINE_AA)
cv2.imshow("modified", myimage)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
