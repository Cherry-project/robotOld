#Converts all 213 jaffe images to pixel lists, then outputs all data to the file 'jaffePixelData.txt'
#jaffePixelData.txt can be viewed in Excel (choose commas as the delimiter), though the number of
#pixels in one row (256X256) exceeds the Excel limit, so all data will not be displayed.

#The first column of jaffePixelData.txt contains the filename of the original image, the second column
#contains the classification of that image, and the following columns contain the value of each pixel.


from PIL import Image
import numpy
import os

rootdir = 'C:/Users/Adil/Desktop/cs221Project-master/cs221Project-master'

f = open('jaffePixelData.txt', 'w')
for subdir, dires, files in os.walk(rootdir):
    for file in files:
        print file #prints filename to terminal
        im = Image.open(os.path.join(subdir,file))
        pixels = list(im.getdata())
        print(len(pixels)) #prints number of pixels in image to terminal
        fileVals = str(file) + str(",") + str(file[3:5])
        for val in pixels:
            fileVals = fileVals + str(",") + str(val)
        print >>f, fileVals

        
#*NOTE: these images are 256x256, not 48x48, so grid partitioning won't work, and there is higher dimensionality
