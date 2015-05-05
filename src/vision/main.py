
import sys

from camera import Camera

import random
rand = random.Random()
def main():
   
   #sys.argv=["C:\Users\Adil\Desktop\camera\main.py",'C:\Users\Adil\Desktop\img',"C:\Program Files (x86)\opencv\data\lbpcascades\lbpcascade_frontalface.xml"]
   #sys.argv=["","D:\utilisateurs\tlelepvr\Desktop", "D:\utilisateurs\tlelepvr\Downloads\opencv\sources\data\lbpcascades\lbpcascade_frontalface.xml"]
   sys.argv=["","../../../../test", "../../../../Downloads/opencv/sources/data/lbpcascades/lbpcascade_frontalface.xml"]
   imagePath=sys.argv[1]
   cascadePath=sys.argv[2]
   camera = Camera(imagePath, cascadePath)
   camera._runCaptureLoop()
  
   


if __name__ == '__main__':
    main()