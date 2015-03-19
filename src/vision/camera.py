import os
import sys
import cv2
import numpy as np
import utils

import random as rand	
from scipy import ndimage  #seulement parce que imread de OpenCV retourne "None" au lieu d'une liste



class Camera:
	
    def __init__(self, imagePath, cascadePath):
        self.name = "unknown"
        self.isSomebody = False
        self.xPosition = 0
        self.yPosition = 0

        self._cascadePath= cascadePath
        self._imagePath=imagePath

        self._cascade = False
        self._cam = False
   


    def setup(self):

        imgdir=self._imagePath        
        try:
            os.mkdir(imgdir)
        except:
            pass # le chemin existe deja

        
        self._cam = cv2.VideoCapture(0)       
        if ( not self._cam.isOpened() ):
           print "camera non detectee!"
           sys.exit()      
        print "camera detectee!."
		
        self._cascade = cv2.CascadeClassifier(self._cascadePath)
        if ( self._cascade.empty() ):
            print "aucune cascade precisee!"
            sys.exit()
        print "cascade ok"





    def runCapture(self):
		
        imgdir = self._imagePath
        cam = self._cam
        cascade = self._cascade
         
        faceSize= (90, 90)
        model= cv2.createLBPHFaceRecognizer(threshold=70.0) 
        
                
        images,labels,names = utils.retrain(imgdir,model,faceSize)
        #print "Nouvel etat:",len(images),"images",len(names),"personnes"
        
        self.isSomebody = False
                  
        ret, img = cam.read()
                         
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #a voir si c'est necessaire
        gray = cv2.equalizeHist(gray)
        # dectection de visage
        rects = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(40, 40), flags=cv2.cv.CV_HAAR_SCALE_IMAGE) #flags = cv2.CASCADE_SCALE_IMAGE     

        # ne prend que la region de l'image qui nous interesse (le visage)
        roi = None
        if len(rects)>0:
            (x, y, w, h) = rects[0]
            # crop & resize it 
            roi = cv2.resize( gray[y:y+h, x:x+h], faceSize )
            #calcule les coordonnees du rectangle et les affiche
            xCentre1=(2*x+w)/2
            yCentre1=(2*y+h)/2  
            xCentre=str(xCentre1)
            yCentre=str(yCentre1)
            centre="("+xCentre+":"+yCentre+")"

            cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0),2)

            if len(images)>0:
                
                [p_label, p_confidence] = model.predict(np.asarray(roi))
                name="unknown"
                if p_label !=-1 :
                    name = names[p_label]
                    self.isSomebody = True
                cv2.putText( img, "%s %.2f %.2f" % (name,p_confidence,p_label),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
                self.name = name
                self.xPosition = xCentre1
                self.yPosition = yCentre1

        #cv2.imshow('Face Recognition For Poppy', img)


    # def _runCaptureLoop(self):
        
    #     print "  cliquer sur 'Echap' pour quitter"
    #     print "  cliquer sur 'a' pour ajouter une image a la base de donnees"
    #     print "  cliquer sur 't' pour retenir le modele"
    
    #     # si le dossier n'existe pas, on le cree
    #     imgdir=self._imagePath        
    #     try:
    #         os.mkdir(imgdir)
    #     except:
    #         pass # le chemin existe deja

    #     # taille des images dans la bdd

    
    #      # open the webcam
       
    #     cam = cv2.VideoCapture(0)
                
    #     if ( not cam.isOpened() ):
    #        print "camera non detectee!"
    #        sys.exit()      
    #     print "camera detectee!."         
    
    #     # load the cascadefile:
    #     cascadePath= self._cascadePath
    #     cascade = cv2.CascadeClassifier(cascadePath)
    #     if ( cascade.empty() ):
    #         print "aucune cascade precisee!"
    #         sys.exit()         
    #     print "cascade:",cascadePath
    
         
    #     faceSize= (90, 90)
    #     model= cv2.createLBPHFaceRecognizer(threshold=70.0) 
        
                
    #     images,labels,names = utils.retrain(imgdir,model,faceSize)
    #     print "Nouvel etat:",len(images),"images",len(names),"personnes"
    #     while True:
        
    #          self._isSomebody = False
                  
    #          ret, img = cam.read()
                         
    #          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #          #a voir si c'est necessaire
    #          gray = cv2.equalizeHist(gray)
    #          # dectection de visage
    #          rects = cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(40, 40), flags=cv2.cv.CV_HAAR_SCALE_IMAGE) #flags = cv2.CASCADE_SCALE_IMAGE     
        
    #          # ne prend que la region de l'image qui nous interesse (le visage)
    #          roi = None
    #          for x, y, w, h in rects:
    #              # crop & resize it 
    #              roi = cv2.resize( gray[y:y+h, x:x+h], faceSize )
    #              #calcule les coordonnees du rectangle et les affiche
    #              xCentre1=(2*x+w)/2
    #          yCentre1=(2*y+h)/2  
    #          xCentre=str(xCentre1)
    #          yCentre=str(yCentre1)
    #          centre="("+xCentre+":"+yCentre+")"
        
    #              cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0),2)
    #              if len(images)>0:
                
    #                 [p_label, p_confidence] = model.predict(np.asarray(roi))
    #                 name="unknown"
    #                 if p_label !=-1 :
    #                     name = names[p_label]
    #                     self._isSomebody = True
    #                 cv2.putText( img, "%s %.2f %.2f" % (name,p_confidence,p_label),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
    #                 self._name = name
    #                 self._xPosition = xCentre1
    #                 self._yPosition = yCentre1
    #              break # use only 1st detected
    #          cv2.imshow('Face Recognition For Poppy', img)
    #          k = cv2.waitKey(5) & 0xFF
        
    #          # quitter avec Echap
    #          if k == 27: break
       
    #          # on clique sur 'a' et on ajoute la personne a la bdd
    #          if (k == 97) and (roi!=None): 
    #              print "Entrer le nom de la personne: "
    #              name = sys.stdin.readline().strip('\r').strip('\n')
    #              #creer un dossier pour cette personne
    #              dirname = os.path.join(imgdir,name)
    #              try:
    #                  os.mkdir(dirname)
    #              except:
    #                  pass #on continue si le dossier existe deja
    #             # on sauvegarde l'image
    #              path=os.path.join(dirname,"%d.png" %(rand.uniform(0,10000)))
    #              print "added:",path
    #              cv2.imwrite(path,roi)
        
    #          # on met a jour le modele
    #          if (k == 116): # 't' pressed
    #              images,labels,names = utils.retrain(imgdir,model,faceSize)
    #              print "Nouvel etat:",len(images),"images",len(names),"personnes"
             		 
