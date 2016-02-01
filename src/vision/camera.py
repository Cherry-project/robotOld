import os
import sys
import cv2
import numpy as np
import utils
import time

import random as rand	
from scipy import ndimage  #seulement parce que imread de OpenCV retourne "None" au lieu d'une liste


def readimage(path, sz=None):
    """
    Reads the images in a given folder, resizes images on the fly if size is given.

    Args:
        path: Path to a folder with subfolders representing the subjects (persons).
        sz: A tuple with the size Resizes 

    Returns:
        A list [X,y]

        X: The images, which is a Python list of numpy arrays.
        y: The corresponding labels (the unique number of the subject, person) in a Python list.
    """
    sz = (90,90)
    
    c = 0
    X,y,z = [], [], []
    for dirname, dirnames, filenames in os.walk(path):
        for subdirname in dirnames:
            subject_path = os.path.join(dirname, subdirname)
            for filename in os.listdir(subject_path):
                try:
                    im = cv2.imread(os.path.join(subject_path, filename), cv2.IMREAD_GRAYSCALE)
                    # resize to given size (if given)
                    if (sz is not None):
                        im = cv2.resize(im, sz)
                    X.append(np.asarray(im, dtype=np.uint8))
                    y.append(c)
                except IOError, (errno, strerror):
                    print "I/O error({0}): {1}".format(errno, strerror)
                except:
                    print "Unexpected error:", sys.exc_info()[0]
                    raise
            c = c+1
            z.append(subdirname)
    return [X,y,z]
        



class Camera:
	
    def __init__(self,robot, imagePath, cascadePath):

        print "init camera"
        self.name = "unknown"
        self.isSomebody = False
        self.xPosition = 0
        self.yPosition = 0

        self._robot = robot

        self._cascadePath= cascadePath
        self._imagePath=imagePath

        self._cascade = False
        self._cam = False
        self._frame = False

        self._X = None
        self._Y = None
        self._Z = None
        self._model = None

        self._name = "unknown"


    def setup(self):

        imgdir=self._imagePath        
        try:
            os.mkdir(imgdir)
        except:
            pass # le chemin existe deja

        self._cascade = cv2.CascadeClassifier(self._cascadePath)

        [self._X,self._Y,self._Z] = readimage(imgdir)

        # Convert labels to 32bit integers. This is a workaround for 64bit machines,
        # because the labels will truncated else. This will be fixed in code as 
        # soon as possible, so Python users don't need to know about this.
        # Thanks to Leo Dirac for reporting:
        self._Y = np.asarray(self._Y, dtype=np.int32)

        # Create the Eigenfaces model. We are going to use the default
        # parameters for this simple example, please read the documentation
        # for thresholding:

        #model = cv2.createFisherFaceRecognizer()
        self._model = cv2.createLBPHFaceRecognizer() 

        # Read
        # Learn the model. Remember our function returns Python lists,threshold=70.0
        # so we use np.asarray to turn them into NumPy lists to make
        # the OpenCV wrapper happy:
        self._model.train(np.asarray(self._X), np.asarray(self._Y))


        
        self._cam = cv2.VideoCapture(1)       
        if ( not self._cam.isOpened() ):
           print "camera non detectee!"
           sys.exit()      
        print "camera detectee!."

    def stop(self):
        self._cam.release()
        cv2.destroyAllWindows()


    def runCapture(self):
		
        imgdir = self._imagePath
        cam = self._cam
        cascade = self._cascade
         
        faceSize= (90, 90)
        model= cv2.createLBPHFaceRecognizer(threshold=70.0) 
        
                
        images,labels,namess = utils.retrain(imgdir,model,faceSize)
        #print "Nouvel etat:",len(images),"images",len(namess),"personnes"
        
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
                    name = namess[p_label]
                    self.isSomebody = True
                cv2.putText( img, "%s %.2f %.2f" % (name,p_confidence,p_label),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
                self.name = name
                self.xPosition = xCentre1
                self.yPosition = yCentre1

        while True:

            cv2.imshow('Face Recognition For Poppy', img)

            k = cv2.waitKey(5) & 0xFF
        
            # quitter avec Echap
            if k == 27: break

    def runLoop2(self):

        cam = cv2.VideoCapture(0)

        while True:

            ret, img = cam.read()
            cv2.imshow('Face Recognition For Poppy', img)

            k = cv2.waitKey(5) & 0xFF
        
            # quitter avec Echap
            if k == 27: break

    def _runCaptureLoop(self):
        

        print "  cliquer sur 'Echap' pour quitter"
        print "  cliquer sur 'a' pour ajouter une image a la base de donnees"
        print "  cliquer sur 't' pour retenir le modele"
    
        # si le dossier n'existe pas, on le cree
        imgdir=self._imagePath        
        try:
            os.mkdir(imgdir)
        except:
            pass # le chemin existe deja

        # taille des images dans la bdd

    
        # open the webcam
       
        cam = cv2.VideoCapture(0)
                
        if ( not cam.isOpened() ):
            print "camera non detectee!"
            sys.exit()      
        print "camera detectee!."         
    
        # load the cascadefile:
        cascadePath= self._cascadePath
        cascade = cv2.CascadeClassifier(cascadePath)
        if ( cascade.empty() ):
            print "aucune cascade precisee!"
            sys.exit()         
        print "cascade:",cascadePath
    
         
        faceSize= (90, 90)
        model= cv2.createLBPHFaceRecognizer(threshold=70.0) 
        
                
        images,labels,namess = utils.retrain(imgdir,model,faceSize)
        print "Nouvel etat:",len(images),"images",len(namess),"personnes"
        while True:
        
            self._isSomebody = False
                  
            ret, img = cam.read()
                         
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #a voir si c'est necessaire
            #gray = cv2.equalizeHist(gray)
            # dectection de visage
            rects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE) #flags = cv2.CASCADE_SCALE_IMAGE     
        
            # ne prend que la region de l'image qui nous interesse (le visage)
            roi = None
            for x, y, w, h in rects:
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
                        name = namess[p_label]
                        self._isSomebody = True
                    cv2.putText( img, "%s %.2f %.2f" % (name,p_confidence,p_label),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
                    self._name = name
                    self._xPosition = xCentre1
                    self._yPosition = yCentre1
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
                dirname = os.path.join(imgdir,name)
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
                images,labels,namess = utils.retrain(imgdir,model,faceSize)
                print "Nouvel etat:",len(images),"images",len(namess),"personnes"
             		 

    def _runCaptureLoop2(self):
        
        print "  cliquer sur 'Echap' pour quitter"
        print "  cliquer sur 'a' pour ajouter une image a la base de donnees"
        print "  cliquer sur 't' pour retenir le modele"
    
        # si le dossier n'existe pas, on le cree
        imgdir=self._imagePath        
        try:
            os.mkdir(imgdir)
        except:
            pass # le chemin existe deja

        # taille des images dans la bdd

    
        # open the webcam
       
        cam = self._cam
                
        if ( not cam.isOpened() ):
            print "camera non detectee!"
            sys.exit()      
        print "camera detectee!."         
    
        # load the cascadefile:
        cascadePath= self._cascadePath
        cascade = cv2.CascadeClassifier(cascadePath)
        if ( cascade.empty() ):
            print "aucune cascade precisee!"
            sys.exit()         
        print "cascade:",cascadePath
    
         
        faceSize= (90, 90)
        model= cv2.createLBPHFaceRecognizer(threshold=70.0)

        self.compteur = 0
        
                
        images,labels,namess = utils.retrain(imgdir,model,faceSize)
        print "Nouvel etat:",len(images),"images",len(namess),"personnes"

        compteur = 0

        while compteur < 10:
        
            if self.compteur > 10:
                self.isSomebody = False
                compteur = 0


            ret, img = cam.read()
                         
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #a voir si c'est necessaire
            #gray = cv2.equalizeHist(gray)
            # dectection de visage
            rects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE) #flags = cv2.CASCADE_SCALE_IMAGE     
        
            # ne prend que la region de l'image qui nous interesse (le visage)
            roi = None
            for x, y, w, h in rects:
                self.isSomebody = True

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
                        name = namess[p_label]                    

                    cv2.putText( img, "%s %.2f %.2f" % (name,p_confidence,p_label),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
                    self.name = name
                    self.xPosition = xCentre1
                    self.yPosition = yCentre1
                break # use only 1st detected

            self.compteur += 1
            cv2.imshow('Face Recognition For Poppy', img)



                    
            k = cv2.waitKey(5) & 0xFF
        
            # quitter avec Echap
            if k == 27: break
       
            # on clique sur 'a' et on ajoute la personne a la bdd
            if (k == 97) and (roi!=None): 
                print "Entrer le nom de la personne: "
                name = sys.stdin.readline().strip('\r').strip('\n')
                #creer un dossier pour cette personne
                dirname = os.path.join(imgdir,name)
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
                images,labels,namess = utils.retrain(imgdir,model,faceSize)
                print "Nouvel etat:",len(images),"images",len(namess),"personnes"
            
            compteur = compteur + 1


    def runCaptureLoop3(self):

        _x = []
        _y = []
        _w = []
        _h = []

        X = self._X
        Y = self._Y
        Z = self._Z

        model = self._model

        cam = self._cam
        ret, frame = cam.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self._cascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        #print faces.x,face.y
        #Draw a rectangle around the faces
        self.isSomebody = False
        self._name="unknown"
        for (x, y, w, h) in faces:
            self.isSomebody = True

            crop_img = frame[y:y+w, x:x+h]

            roi = cv2.resize( crop_img, (90,90) )
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0,195,240), 1)
            #cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 1)


            if len(X)>0:
                
                [p_label, p_confidence] = model.predict(np.asarray(roi))
                if p_label !=-1 :
                    self._name = Z[p_label]
                    #self._robot.say_sentence_local.start("Bonjour, " + name)
                cv2.putText( frame, "%s" % ("Amandine"),(x,y-20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
            

            _x.append(x)
            _y.append(y)
            _w.append(w)
            _h.append(h)

            #if( ancienx < (2*x+w)/2  | ancieny < (2*x+w)/2) :
        if (self.isSomebody == True):

            x = np.amax(_x)
            y = np.amax(_y)
            w = np.amax(_w)
            h = np.amax(_h)

            self.xPosition=(2*x+w)/2
            self.yPosition=(2*y+h)/2


            #ancienx = self.xPosition
            #ancieny = self.yPosition
            #self.xPosition=x
            #self.yPosition=y

            # Display the resulting frame
        #cv2.imwrite('Video.png', frame)
        self._frame = frame

    def displayVideo(self):
        while True:
    
            cv2.imshow('Video', self._frame)
            time.sleep(0.02)

            if cv2.waitKey(30) & 0xFF == ord('q'):
                break

        #self._cam.release()
        cv2.destroyAllWindows()
