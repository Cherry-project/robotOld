import os
import sys
import cv2
import numpy as np

import random
from scipy import ndimage  #seulement parce que imread de OpenCV retourne "None" au lieu d'une liste



class Camera:

   is_somebody=0
   
   coor_X = 0
   coor_Y = 0
   def __init__(self, imagePath, cascadePath, scaleFactor= 1.2, minNeighbors=5 , 
                minSize=(40, 40), flags=cv2.cv.CV_HAAR_SCALE_IMAGE,
                cameraDeviceID=0, rectColor=(0, 255 ,0), face_size=(90,90), threshold=70, 
                title='facial recognition'):
          self._running= True	
          
          self._cameraDeviceID= cameraDeviceID
          self._capture= cv2.VideoCapture(cameraDeviceID)
          self._cascadePath= cascadePath
          self._imagePath=imagePath
          self._detector= cv2.CascadeClassifier(self._cascadePath)		  
          self._threshold= threshold
          self._recognizer= cv2.createLBPHFaceRecognizer(self._threshold)
          self._minNeighbors= minNeighbors
          self._minSize= minSize
          self._flags= flags
          self._rectColor= rectColor
          self._faceSize= face_size
          
   def _readImages(self, path, sz=None):
   
    c = 0
    X,y,z = [], [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            
            for filename in os.listdir(subject_path):
                try:
                    #im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)  #pourrait marcher dans d'autres supports. a tester
                    im= ndimage.imread(os.path.join(subject_path, filename),flatten=True)  #marche pour l'instant. a tester
                                         
                    if (len(im)==0):    #erreur si imread ne marche pas (ne retourne pas une liste)
                        continue                         
                    # resize to given size
                    if (sz is not None):
                        im = cv2.resize(im, sz)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError:
                    print ""   #exception lancee meme si le script marche. a verifier
                except:
                    print "Erreur inatendue:", sys.exc_info()[0]
                    raise
            c = c+1
            z.append(subdirname)
    return [X,y,z]
   def _retrain(self, imgpath, model,sz ) :
    # read in the image data. This must be a valid path!
    X,y,names = self._readImages(imgpath,sz) 
    if len(X) == 0:
        print "chemin vide", imgpath
        return [[],[],[]]
    #apprentissage. (ajout de photos pour plus de precision dans la reconnaissance
    
    model.train(np.asarray(X), np.asarray(y, dtype=np.int32)) 
    
    return [X,y,names] 
   def _runCaptureLoop(self):
        
        if len(sys.argv) < 3:
             print "USAGE: Face_Recognition.py </path/to/images> <path/to/cascadefile>"
             sys.exit()
         
        print "  cliquer sur 'Echap' pour quitter"
        print "  cliquer sur 'a' pour ajouter une image a la base de donnees"
        print "  cliquer sur 't' pour retenir le modele"
    
        # si le dossier n'existe pas, on le cree
        
        try:
            os.mkdir(self._imagePath)
        except:
            pass # le chemin existe deja

        # taille des images dans la bdd

    
         # open the webcam
        cam = cv2.VideoCapture(self._cameraDeviceID)
        if ( not cam.isOpened() ):
           print "camera non detectee!"
           sys.exit()      
        print "camera detectee!."         
    
        # load the cascadefile:
        cascade = cv2.CascadeClassifier(self._cascadePath)
        if ( cascade.empty() ):
            print "aucune cascade precisee!"
            sys.exit()         
        print "cascade:",self._cascadePath
    
         
   
        images,labels,names = self._retrain(self._imagePath,self._recognizer,self._faceSize)
        print "Nouvel etat:",len(images),"images",len(names),"personnes"
        while self._running:
             ret, img = self._capture.read()
             gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		     #a voir si c'est necessaire
             gray = cv2.equalizeHist(gray)
             # dectection de visage
             rects = cascade.detectMultiScale(gray, scaleFactor=self._scaleFactor, minNeighbors=self._minNeighbors, minSize=self._minSize, flags=self._flags)      
        
             # ne prend que la region de l'image qui nous interesse (le visage)
             roi = None
             for x, y, w, h in rects:
                 # crop & resize it 
                 roi = cv2.resize( gray[y:y+h, x:x+h], self._facesize )
                 #calcule les coordonnees du rectangle et les affiche
                 xCentre1=(2*x+w)/2
	         yCentre1=(2*y+h)/2  
	         xCentre=str(xCentre1)
	         yCentre=str(yCentre1)
	         centre="("+xCentre+":"+yCentre+")"
	    
                 cv2.rectangle(img, (x,y),(x+w,y+h), self._rectColor,2)
                 if len(images)>0:
                
                    [p_label, p_confidence] = self._recognizer.predict(np.asarray(roi))
                    name="unknown"
                    if p_label !=-1 : name = names[p_label]
                    cv2.putText( img, "%s %.2f %.2f" % (name,p_confidence,p_label),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, self._rectColor)
                 break # use only 1st detected
             cv2.imshow('Face Recognition For Poppy', img)
             k = cv2.waitKey(5) & 0xFF
        
             # quitter avec Echap
             if k == 27: break
       
             # on clique sur 'a' et on ajoute la personne a la bdd
             if (k == 97) and (roi!=None): 
                 print "Entrer le nom de la personne: "
                 name = sys.stdin.readline().strip('\r').strip('\n')
                 #creer un dossier pour cette personne
                 dirname = os.path.join(self._imagePath,name)
                 try:
                     os.mkdir(dirname)
                 except:
                     pass #on continue si le dossier existe deja
                # on sauvegarde l'image
                 path=os.path.join(dirname,"%d.png" %(rand.uniform(0,10000)))
                 print "added:",path
                 cv2.imwrite(path,roi)
        
             # on met a jour le modele
             if (k == 116): # 't' pressed
                 images,labels,names = self._retrain(imgdir,self._recognizer,self._faceSize)
                 print "Nouvel etat:",len(images),"images",len(names),"personnes"
   
	
   
             		 
