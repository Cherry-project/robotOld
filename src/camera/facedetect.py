

import numpy as np
import cv2
import cv2.cv as cv
from video import create_capture
from common import clock, draw_str

help_message = '''
USAGE: facedetect.py [--cascade <cascade_fn>] [--nested-cascade <cascade_fn>] [<video_source>]
'''

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=10, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
	        
		xCentre1=(x1+x2)/2
		yCentre1=(y2+y1)/2  
		xCentre=str(xCentre1)
	        yCentre=str(yCentre1)
	        centre="("+xCentre+":"+yCentre+")"
	        cv2.putText(img,centre, (xCentre1, yCentre1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 255, 0), thickness = 2, lineType=cv2.CV_AA)
	        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
	       
		    
	     
		  
              	

if __name__ == '__main__':
    import sys, getopt
    print help_message

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)
	
    cascade_fn = args.get('--cascade', "C:/Program Files (x86)/opencv/data/haarcascades/haarcascade_frontalface_alt.xml")
	
   

    cascade = cv2.CascadeClassifier(cascade_fn)
   

    cam = create_capture(video_src, fallback='synth:bg=../cpp/lena.jpg:noise=0.05')
    # Define the codec and create VideoWriter object
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('facedetect_Natural_Light.avi',fourcc, 25.0, (640,480))
    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))
	   
		
	
           
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow('facedetect', vis)
	out.write(vis)
	
		
        
        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()

