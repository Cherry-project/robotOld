import cv2
import sys

#on choisit la cascade de classifieurs de Haar, disponible avec openCV
cascPath = "C:\Program Files (x86)\opencv\data\haarcascades\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
#on detecte la webcam par defaut de la camera
video_capture = cv2.VideoCapture(0)
# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('webcam_Natural_Light.avi',fourcc, 15.0, (640,480))
#on lit une frame dans chaque iteration et on retourne une frame avec visage detect
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 #gray: matrice de l'image tiree de la frame
 #scaleFactor: facteur de reduction de l'image
 #minNeighbors: nombre de voisinages le candidat doit avoir pour le retenir
 #minSize: taille minimum de l'objet detectee
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30), 
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # dessine un rectangle autour de l'objet
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # affiche l'image resultante
    cv2.imshow('Video', frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
