import cv2
import sys
import numpy as np


def detectFaces(img,faceCascade,rectangleColor,scaleFact,faceCascade2=None):
    #Img is a color imag
    #faceCascade is a cv2.CascadeClassifier)
    #rectange is a tuple in the form (B,G,R) B,G,R >=0 and <=255 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=scaleFact,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), rectangleColor, 2)
        if faceCascade2 != None:
            img2 = gray[y:y+h,x:x+w]
            img2 = gray[y + h/2:y+h,x:x+w] #for mouth
            y = y +h/2
            cv2.imshow('Video2',img2)
            faces2 = faceCascade2.detectMultiScale(
            img2,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
            )
            for (x2,y2,w2,h2) in faces2:
                #cv2.rectangle(img, (x+x2, y+y2), (x + x2+w2, y + y2+h2), (0,0,255), 2)
                cv2.ellipse(img, (x+x2+w2/2, y+y2+h2/2), (w2/2, h2/2),0,0,360, rectangleColor, 2)

    


#Initialize Filters
cascPath = './filters/haarcascade_frontalface_default.xml'
cascPath2 = './filters/haarcascade_profileface.xml'
cascPath3 = './filters/haarcascade_smile.xml'
cascPath3 = './filters/haarcascade_eye.xml'
cascPath3 = './filters/Mouth.xml'
#cascPath3 = './filters/Nose.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade2 = cv2.CascadeClassifier(cascPath2)
faceCascade3 = cv2.CascadeClassifier(cascPath3)
#config WebCam
video_capture = cv2.VideoCapture(0)
cv2.imshow('Video', np.empty((5,5),dtype=float))


while cv2.getWindowProperty('Video', 0) >= 0:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    detectFaces(frame,faceCascade,(0,255,0),1.3,faceCascade3)
    detectFaces(frame,faceCascade2,(0,255,255),1.3)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    #detectFaces(img,faceCascade3)

    cv2.waitKey(1)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
