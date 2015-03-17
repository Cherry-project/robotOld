import os
import sys
import cv2
import numpy as np

from scipy import ndimage  #seulement parce que imread de OpenCV retourne "None" au lieu d'une liste

import random
rand = random.Random()
#aucune idee sur la pertinence de cette ligne en terme de securite ou de qualite. sys.argv pas encore assimilee
#LBP est plus rapide mais moins precise 10 a 20% par rapport a Haar
#sys.argv=["C:\Users\Adil\Desktop\Face_Recognition.py",'C:\\Users\\Adil\\Desktop\\img',"C:\Program Files (x86)\opencv\data\lbpcascades\lbpcascade_frontalface.xml"]
#sys.argv=["C:\Users\Adil\Desktop\Face_Recognition.py",'C:\\Users\\Adil\\Desktop\\img',"C:\Program Files (x86)\opencv\data\haarcascades\haarcascade_frontalface_alt2.xml"]
sys.argv=["C:\Users\Adil\Desktop\Face_Recognition.py",'C:\\Users\\Adil\\Desktop\\img',"C:\Program Files (x86)\opencv\data\haarcascades\haarcascade_frontalface_default.xml"]

def read_images(path, sz=None):
   
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




#garde le modele
def retrain( imgpath, model,sz ) :
    # read in the image data. This must be a valid path!
    X,y,names = read_images(imgpath,sz) 
    if len(X) == 0:
        print "chemin vide", imgpath
        return [[],[],[]]
    #apprentissage. (ajout de photos pour plus de precision dans la reconnaissance
    
    model.train(np.asarray(X), np.asarray(y, dtype=np.int32)) #a modifier eventuellement pour les machines 64bit
    return [X,y,names]



if __name__ == "__main__":
   
   
    if len(sys.argv) < 3:
        print "USAGE: Face_Recognition.py </path/to/images> <path/to/cascadefile>"
        sys.exit()
        
    print "  cliquer sur 'Echap' pour quitter"
    print "  cliquer sur 'a' pour ajouter une image a la base de donnees"
    print "  cliquer sur 't' pour retenir le modele"
    
    # si le dossier n'existe pas, on le cree
    imgdir = sys.argv[1]
    try:
        os.mkdir(imgdir)
    except:
        pass # le chemin existe deja

    # taille des images dans la bdd
    face_size=(90,90)
    
    # open the webcam
    cam = cv2.VideoCapture(0)
    if ( not cam.isOpened() ):
         print "camera non detectee!"
         sys.exit()      
    print "camera detectee!."         
    
    # load the cascadefile:
    cascade = cv2.CascadeClassifier(sys.argv[2])
    if ( cascade.empty() ):
         print "aucune cascade precisee!"
         sys.exit()         
    print "cascade:",sys.argv[2]
    
    #a choisir entre les 3 modeles de reconnaissances disponibles
	#il faut aussi changer le chemin aux cascades en haut
    #model = cv2.createEigenFaceRecognizer()
    #model = cv2.createFisherFaceRecognizer()
    model = cv2.createLBPHFaceRecognizer(threshold=100.0)    
    
   
    images,labels,names = retrain(imgdir,model,face_size)
    print "Nouvel etat:",len(images),"images",len(names),"personnes"
    
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		#a voir si c'est necessaire
        gray = cv2.equalizeHist(gray)
        # dectection de visage
        rects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)       
        
        # ne prend que la region de l'image qui nous interesse (le visage)
        roi = None
        for x, y, w, h in rects:
            # crop & resize it 
            roi = cv2.resize( gray[y:y+h, x:x+h], face_size )
            #calcule les coordonnees du rectangle et les affiche
            xCentre1=(2*x+w)/2
	    yCentre1=(2*y+h)/2  
	    xCentre=str(xCentre1)
	    yCentre=str(yCentre1)
	    centre="("+xCentre+":"+yCentre+")"
	    
            cv2.rectangle(img, (x,y),(x+w,y+h), (0, 255, 0),2)
            if len(images)>0:
                
                [p_label, p_confidence] = model.predict(np.asarray(roi))
                name = "unknown"
                if p_label != -1 : name = names[p_label]
                cv2.putText( img, "%s %.2f %s" % (name,p_label,centre),(x+10,y+20), cv2.FONT_HERSHEY_PLAIN,1.5, (0,255,0))
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
            images,labels,names = retrain(imgdir,model,face_size)
            print "Nouvel etat:",len(images),"images",len(names),"personnes"
                         
