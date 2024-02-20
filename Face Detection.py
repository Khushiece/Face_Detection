#For building Face Detection we will use HAAR CASCADE FRONTAL FACE ALGORITHM.
#DetectMultiScale...
#face=face_cascade.detectMultiScale(src,scalefactor,minNeighbors)
import cv2
#First step is to load the haarcascade  face detection algorithm
alg="C:\\Users\\khush\\Desktop\\khushicode\\course 1\\AI\\haarcascade_frontalface_default.xml"
haar_cascade=cv2.CascadeClassifier(alg)
#second Step is to initializing the camera.....
cam=cv2.VideoCapture(0)
#Third Step is to read the frame from camera
while True:
    ret,img=cam.read()
#Fourth step is to convert the color image into gray scale image.
    grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#fifth step is to obtained face coordinates by passing algorithm
    face=haar_cascade.detectMultiScale(grayImg,1.3,2)
#sixth step is to draw rectangle on the face coordinates
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Face Detection",img)
    key=cv2.waitKey(1)&0xff
    if key==ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
    

