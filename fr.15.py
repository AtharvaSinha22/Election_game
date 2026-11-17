import cv2
camera=cv2.VideoCapture(0)

smile_classifier=cv2.CascadeClassifier("haarcascade_smile.xml")

while camera.isOpened():
    ret,frame= camera.read()
    frame=cv2.flip(frame,1)
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    smiles= smile_classifier.detectMultiScale(gray_frame,2,20)
    if len(smiles)>0:
        for x,y,w,h in smiles:
            cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),5)
    cv2.imshow('smile video',frame)
    code=cv2.waitKey(1)
    if code>0 and chr(code)=='q':
        break

camera.release()
cv2.destroyAllWindows()
                      
