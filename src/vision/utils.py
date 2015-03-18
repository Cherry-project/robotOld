import os
import sys
import cv2
import numpy as np

from scipy import ndimage  #seulement parce que imread de OpenCV retourne "None" au lieu d'une liste


def readImages(path, sz=None):
   
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
	
	
def retrain( imgpath, model,sz ) :
    
    
    # read in the image data. This must be a valid path!
    X,y,names = readImages(imgpath,sz)
        	
    if len(X) == 0:
        print "chemin vide", imgpath
        return [[],[],[]]
         
    model.train(np.asarray(X), np.asarray(y, dtype=np.int32)) 
    
    return [X,y,names] 