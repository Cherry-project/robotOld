import numpy as np
import cv2 as cv2
import csv
import sys
import random
import collections
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import scipy.spatial.distance
import scipy.cluster.vq


##--------KAGGLE DATA PARAMETERS-------
#emotion key: (0 = Angry, 1 = Disgust, 2 = Fear, 3 = Happy, 4 = Sad, 5 = Surprise, 6 = Neutral)

#Set this to true to use a truncated version of the data of size smallKaggleDataSetSize'
smallKaggleDataSet = True
smallKaggleDataSetSize = 500 #number of data points in the smaller data set (for both the test and train data)
##-------------------------------------

##--------JAFFE DATA PARAMETERS--------
#emotion key: (0 = Neutral, 1 = Happy, 2 = Sad, 3 = Surprised, 4 = Angry, 5 = Disgust, 6 = Fear)

#Out of 213 images, set the size of the training set (must be <= 213 and note: jaffe_testing_set_size automatically set to (214 - training_set_size))
jaffe_training_set_size = 150
#set the training data to be randomized or not
randomize_jaffe_data = False
##-------------------------------------

#set by program arguments, <source> signifies which data set we are using
source = "jaffe"
useBW = False

def parseKaggleData(file_name):
    '''
    Function Purpose: parse input data from a csv file

    Return Value: 3-tuple: (training_data, testing_data1, testing_data2)
    - each element in training_data, testing_data1, and testing_data2 is a 2-tuple: (pixels, emotion category)
        - pixels: a list of pixel color values. The index of the color value represents the index of the pixel
        - emotion category: the emotion given in the image. this is a value in the range [0,6]
    

    Note: Entire Data set contains
    -Angry: 4953 data points
    -Disgust: 547 data points
    -Fear: 5121 data points
    -Happy: 8989 data points
    -Sad: 6077 data points
    -Surprised: 4002 data points
    -Neutral: 6198 data points

    Totaling to: 35,887 data points

    (0 = Angry, 1 = Disgust, 2 = Fear, 3 = Happy, 4 = Sad, 5 = Surprise, 6 = Neutral)
    '''

    data = open(file_name, 'r')
    dataLines = csv.reader(data)
    data.close()
    training_data = [] #list of tuples (pixels, emotion category) where pixels is a list ints representing the 
                        #color value for each pixel and 'emotion category' is an int is in the range [0, 6]
    
    testing_data1 = []
    testing_data2 = None

    emotionCounter = [0]*7

    #using a smaller data set for testing
    if smallKaggleDataSet:
        trainCounter = 0
        testCounter = 0
        for line in dataLines:

            if trainCounter >= smallKaggleDataSetSize and testCounter >= smallKaggleDataSetSize: break
            
            inputList = None
            if line[2] == 'Training':
                
                if trainCounter >= smallKaggleDataSetSize: continue
                inputList = training_data
                trainCounter += 1
            
            elif line[2] == 'PublicTest' or line[2] == 'PrivateTest':
                
                if testCounter >= smallKaggleDataSetSize: continue
                inputList = testing_data1
                testCounter +=1

            #append data point
            if inputList != None: 
                pixels = [int(val) for val in line[1].split(" ")]
                emotion = int(line[0])
                emotionCounter[emotion] += 1
                inputList.append((pixels, int(line[0])))


    #using all the data
    else: 
        testing_data2 = []
        for line in dataLines:
            #choose which list to append data point to
            inputList = None
            if line[2] == 'Training': inputList = training_data
            if line[2] == 'PublicTest': inputList = testing_data1
            elif line[2] == 'PrivateTest': inputList = testing_data2

            #append data point
            if inputList != None: 
                pixels = [int(val) for val in line[1].split(" ")]
                emotion = int(line[0])
                emotionCounter[emotion] += 1
                inputList.append((pixels, int(line[0])))

    print "emotionCounter: ", emotionCounter
    return (training_data, testing_data1, testing_data2)


def parseJaffeData(file_name):
    '''
    Function Purpose: parse input data from a .txt file

    Return Value: 2-tuple: (training_data, testing_data)
    - each element in training_data and testing_data is a 2-tuple: (pixels, emotion category)
        - pixels: a list of pixel color values. The index of the color value represents the index of the pixel
        - emotion category: the emotion given in the image. this is a value in the range [0,6]
            -Note for jaffe: 
            (0 = neutral, 1 = happy, 2 = sad, 3 = surprised, 4 = angry, 5 = disgust, 6 = fear)
    
    Note: Entire Data set contains
    -Neutral: 30 data points
    -Happy: 31 data points
    -Sad: 31 data points
    -Surprised: 30 data points
    -Angry: 30 data points
    -Disgust: 29 data points
    -Fear: 32 data points

    Totaling to: 213 data points
    '''

    data = open(file_name, 'r')
    dataLines = lines = data.readlines()
    data.close()
    training_data = [] #list of tuples (pixels, emotion category) where pixels is a list ints representing the 
                        #color value for each pixel and 'emotion category' is an int is in the range [0, 6]
    testing_data = []
    all_data = []
    emotion_to_index = {"NE": 0, "HA": 1, "SA": 2, "SU": 3, "AN": 4, "DI": 5, "FE": 6}

    emotionCounter = [0]*7

    print "number of Jaffe Images: ", len(dataLines)
    for i, line in list(enumerate(dataLines)):

        data_set = training_data
        if i >= jaffe_training_set_size: data_set = testing_data

        values = line.split(',')
        emotion = emotion_to_index[str(values[1])]
        emotionCounter[emotion] += 1

        pixels = [int(x) for x in values[2:]]
        data_set.append((pixels, emotion))
        all_data.append((pixels, emotion))

    print "emotionCounter: ", emotionCounter
    return (training_data, testing_data, all_data)



''' ---------------------- STOCHATIC GRADIENT DESCENT CODE ---------------------- '''

def evaluatePredictor(examples, predictor):
    '''
    predictor: a function that takes an x and returns a predicted y.
    Given a list of examples (x, y), makes predictions based on |predict| and returns the fraction
    of misclassiied examples.

    set emotion_evaluator to True to get a break down of which emotions are classified incorrectly
    '''

    #set to true if want the function to evaluate accuracy based on emotion
    emotion_evaluator = True
    ## emotion_couter[emotion index] =[#wrongly classified, #images of this emotion]
    emotion_counter = {0:[0,0], 1:[0,0], 2:[0,0], 3:[0,0], 4:[0,0], 5:[0,0], 6:[0,0]}

    error = 0
    i = 0
    for j in range(0, len(examples)):
        x,y = examples[j]
        i += 1
        emotion_counter[y][1] += 1
        if predictor(x) != y:
            error += 1
            emotion_counter[y][0] += 1

    if emotion_evaluator: 
        for emotion in range (0,7): print emotion, " --> accuracy rate: ", 1 - float(emotion_counter[emotion][0])/float(emotion_counter[emotion][1])
        print "overall accuracy: ", 1 - (1.0 * error / float(len(examples)))
    else: print "accuracy: ", 1 - (1.0 * error / float(len(examples)))

def pixelIndexFeatureExtractor(x):
    '''
    Function Purpose: Feature Extractor Function

    input: list of pixel values (ints) that correspond to an image
    output: phi(x) represented as a dictionary
        -feature (index of the pixel) --> value (color value of the pixel)
    
    '''
    featureVector = dict()
    if useBW:
        image = get2dImage(x)
        image = np.uint8(image)
        ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
        for i in range(0,len(thresh)):
            for j in range(0,len(thresh[i])):
                featureVector[i*256+j] = thresh[i][j]
    else:
        for i in range(len(x)):
            featureVector[i] = x[i]

    return featureVector


def getMaxBranchIndex(weightList, y, phi):
    '''
    Function Purpose: 
        determines and returns the arg max over i of: 
        {dotProduct(weightList[i], phi) - dotproduct(weightList[y], phi) + 1 * (indicator i equals not y)}
    '''

    branchValues = []
    true_weights = weightList[y]

    for i in range(0, len(weightList)):
        d = dotProduct(weightList[i], phi) - dotProduct(true_weights, phi)
        if y != i: d += 1
        branchValues.append(d)

    maxValue = None
    maxBranchIndex = None

    for i in range(0, len(branchValues)):
        if maxValue == None or branchValues[i] > maxValue:
            maxValue = branchValues[i]
            maxBranchIndex = i

    return maxBranchIndex


def learnPredictor(trainExamples, testExamples, featureExtractor):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, return the multiclass weight vector (sparse feature vector) learned.

    Stochastic gradient descent implemented with the multiclass version of the 
    Hinge Loss Function.
    '''

    #each category has its own set of weights
        # weights[0] = dictionary: key(feature) => value(weight)
    weightList = [{}, {}, {}, {}, {}, {}, {}]
    phiDict = {}

   
    def predictor(x):
        '''
        -returns argMax over i of: dotProduct(weightList[i], featureExtractor(x))
        -this argMax represents the category that gives the highest score for the given x
        '''
        maxScore = None
        bestCategory = None
        phi = featureExtractor(x)
        for i in range(0, len(weightList)):
            score = dotProduct(weightList[i], phi)
            if maxScore == None or score > maxScore: 
                bestCategory = i
                maxScore = score

        return bestCategory


    eta = 1
    numIters = 20
    for i in range(numIters):
        eta = 1 / ((i + 1)**(1/2.0)) #step size dependent on the interation number
        for x, y in trainExamples:
            if tuple(x) in phiDict:
                phi = phiDict[tuple(x)]
            else:
                phi = featureExtractor(x)
                phiDict[tuple(x)] = phi
            dominantWeightIndex = getMaxBranchIndex(weightList, y, phi)
            if dominantWeightIndex != y:
                HLG = phi
                incrementWeightList(weightList, y, eta, phi)
                incrementWeightList(weightList,dominantWeightIndex,-1*eta, HLG)


        print "------- iteration: ", i, " --------"
        print "train accuracy" 
        evaluatePredictor(trainExamples, predictor)
        print "test accuracy"
        evaluatePredictor(testExamples, predictor)

    return weightList

def incrementWeightList(weightList, index, scale, d2):
    # """
    # Implements weightList[index] += scale * d2 for sparse vectors.
    # @param weightList[index]: the feature vector which is mutated.
    # @param float scale
    # @param dict d2: a feature vector.
    # """
    for f, v in d2.items():
        weightList[index][f] = weightList[index].get(f, 0) + v * scale

def dotProduct(d1, d2):
    """
    @param dict d1: a feature vector represented by a mapping from a feature (string) to a weight (float).
    @param dict d2: same as d1
    @return float: the dot product between d1 and d2
    """
    if d1 is not None and d2 is not None:
        if len(d1) < len(d2):
            return dotProduct(d2, d1)
        else:
            return sum(d1.get(f, 0) * v for f, v in d2.items())
    else:
        return 0




''' ---------------------- KMEANS CLUSTERING CODE ---------------------- '''

def euclideanDist(point1, point2):
    '''
    ----
    Function Purpose: Given two points (inputted as lists), this function returns their Eucliedean 
    distance

    Arguments: 
        -two points represented as lists
    Return Value:
        -the Eculidean distance between the two points
    ----
    '''

    nDimensions = len(point1)
    sqSum = 0
    if point2 != []:
        for i in range(nDimensions):
            sqDifference = (point1[i] - point2[i])**(2.0)
            sqSum += sqDifference
    else:
        for i in range(nDimensions):
            sqDifference = (point1[i])**(2.0)
            sqSum += sqDifference
    
    return sqSum**(1.0/2.0)



def returnAverage(pointList):
    '''
    ----
    Function Purpose: Given a list of points, this function returns their average
    Arguments: 
        -a list of points
    Return Value:
        -the average of the points in the list
    ----
    '''
    nPoints = len(pointList)
    if nPoints == 0: return None

    nDimensions = len(pointList[0])
    average = [0] * nDimensions

    for point in pointList:
        for i in range(0, len(point)):
            average[i] += 1.0/nPoints * point[i]
    return average

def returnClosetCentroid(point, centroidsPrev):
    '''
    ----
    Function Purpose: Given a point and list of centroids, this function returns the index of the centroid
    closest to the point. Note: if multiples centroids are equidistant to the point, the 
    function randomly selects one of the equidistant centroids to return

    Arguments: 
        -a list representing a specfic point and a list of centroids
    Return Value:
        -the index of the closest centroid to the point
    ----
    '''
    runningMin = None
    closetCentroidIndex = 0 #default to being the centroid at index 0
    nCentroids = len(centroidsPrev)
    
    for i in range(nCentroids):
        centroid = centroidsPrev[i]
        distance = euclideanDist(centroid, point)
        if (runningMin == None) or ((distance < runningMin)):
            runningMin = distance
            closetCentroidIndex = i

        if((distance == runningMin)): closetCentroidIndex = random.choice([closetCentroidIndex, i])
    return closetCentroidIndex

def notConverged(centroidsPrev, centroidsNew):
    '''
    ----
    Function Purpose: Given the new centroids and the centroids calculated in the last iteration of the 
    algorithm, this function returns whether or not the two centroid lists are equivalent

    Arguments: 
        -two lists of centroids
    Return Value:
        -True: the two lists are different
        -False: the two lists are the same
    ----
    '''

    count = len([centroid for centroid in centroidsNew if centroid not in centroidsPrev])
    count += len([centroid for centroid in centroidsPrev if centroid not in centroidsNew])

    return count != 0


def kmeans(data, k, maxIterations):
    '''
    ----
    Function Purpose: This function performs the kmeans clustering algorithm. The
    algorithm stops iterating once the calculated centroids converge or the max 
    number of iterations is achieved.

    Arguments: 
        -data: list of data points (RBG values given in standardized order across all images)
        -k
        -max number of iterations
    Return Value:
        -cluster assignments (clusters[i] = cluster data[i] is assigned to)
        -final centroids
    ----
    '''

    centroidsPrev = [] 
    for i in range(0, k):
        centroidsPrev.append([])

    nDataPoints = len(data)
    
    clusters = []
    for i in range(0, nDataPoints): clusters.append(-1)
    centroidsNew = []
    for i in range(0, k):
        centroidsNew.append([])

    #initialize centroids to a random sample of size K from examples
    for i in range(k):
        choice = None
        while(choice == None):
            choice = random.choice(data)
        centroidsNew[i] = choice


    iteration = 0
    while(notConverged(centroidsPrev, centroidsNew) and iteration < maxIterations):
        print "iteration: ", iteration
        centroidsPrev = list(centroidsNew)

        #assign points to a centroid
        for i in range(0, nDataPoints):
            if data[i] != None:
                point = data[i]
                closetCentroidIndex = returnClosetCentroid(point, centroidsPrev)
                clusters[i] = closetCentroidIndex
            else: clusters[i] = None

        #recalculate centroids
        for centroidIndex in range(0, k):
            points = [data[i] for i in range(nDataPoints) if clusters[i]==centroidIndex]
            average = returnAverage(points)
            if average != None: centroidsNew[centroidIndex] = average
        iteration += 1

        #if iteration%10 == 0: print "iteration: ", iteration


    if(iteration != maxIterations): print "Converged!"
    
    '''print "---final centroids---"
    print "centroids: ", centroids
    print "iteration: ", iteration
    print "clusters: ", clusters
    '''

    return clusters, centroidsNew


def evaluatePartionedClusters(eye1ClusterAssignments, eye2ClusterAssignments, mouthClusterAssignments, data, k):
    '''
    function purpose: measure the accuracy of clustering by partitioning into eye1, eye2, and 
        mouthClusters. Each image has a sift feature placed run through eye1Kmeans, eye2Kmeans, and 
        mouthKmeans. These cluster assignments are denoated in the corresponding arguments to this 
        function. The most common emotion each image is mapped to is the final emotion the image
        is to predicted to represent.
        (NOTE: if an image doesn't have a sift feature that maps to one of these areas,
        it submits a feature of 'None' which is overlooked in the Kmeans implementation).
    arguments:
        -eye1ClusterAssignments: eye1ClusterAssignments[0] = the cluster eye1 of the 1st image was assigned to
        -eye2ClusterAssignments: eye2ClusterAssignments[0] = the cluster eye2 of the 1st image was assigned to
        -mouthClusterAssignments: mouthClusterAssignments[0] = the cluster the mouth of the 1st image was assigned to

    '''

    eye1_kmeansGroup_to_trueGroup = detmineGroupMapping(eye1ClusterAssignments, data, k)
    eye2_kmeansGroup_to_trueGroup = detmineGroupMapping(eye2ClusterAssignments, data, k)
    mouth_kmeansGroup_to_trueGroup = detmineGroupMapping(mouthClusterAssignments, data, k)

    correct = 0
    nDataPoints = len(eye1ClusterAssignments)
    dataPointsCounted = 0
    for i in range(0, nDataPoints):
        counter = collections.Counter()
        
        eye1ClusterAssignment = eye1ClusterAssignments[i]
        if eye1ClusterAssignment != None and eye1ClusterAssignment in eye1_kmeansGroup_to_trueGroup: 
            counter[eye1_kmeansGroup_to_trueGroup[eye1ClusterAssignment]] += 1


        eye2ClusterAssignment = eye2ClusterAssignments[i]
        if eye2ClusterAssignment != None and eye2ClusterAssignment in eye2_kmeansGroup_to_trueGroup:
            counter[eye2_kmeansGroup_to_trueGroup[eye2ClusterAssignment]] += 1

        mouthClusterAssignment = mouthClusterAssignments[i]
        if mouthClusterAssignment != None and mouthClusterAssignment in mouth_kmeansGroup_to_trueGroup:
            counter[mouth_kmeansGroup_to_trueGroup[mouthClusterAssignment]] += 1
        
        
        mostCommonList = counter.most_common(1)
        if len(mostCommonList) == 0: continue
        
        dataPointsCounted += 1
        maxCategory, maxCount = mostCommonList[0]
        if maxCount < 2:
            if eye1_kmeansGroup_to_trueGroup[eye1ClusterAssignment] == data[i][1]: correct += 1
        else:
            if maxCategory == data[i][1]: correct +=1

    
    accuracy = float(correct)/float(dataPointsCounted)

    print "----RESULTS----"
    print "nDataPoints: ", nDataPoints
    print "k: ", k
    print "accuracy: ", accuracy


def evaluateClusters(clusterAssignments, data, k):
    '''
    Function purpose:
        Evaluates accuracy of clustering by comparing an examples assigned 
        cluster in clusterAssignments to its true emotion (listed in data)
    '''

    #groupMapping[guessed group number] --> True Group number
    kmeansGroup_to_trueGroup = detmineGroupMapping(clusterAssignments, data, k)
    correct = 0
    nDataPoints = len(clusterAssignments)
    for i in range(0, nDataPoints):
        if clusterAssignments[i] not in kmeansGroup_to_trueGroup: continue
        if kmeansGroup_to_trueGroup[clusterAssignments[i]] == data[i][1]: correct +=1

    
    accuracy = float(correct)/float(nDataPoints)

    print "----RESULTS----"
    print "nDataPoints: ", nDataPoints
    print "k: ", k
    print "accuracy: ", accuracy



def detmineGroupMapping(clusterAssignments, data, k):
    '''
    Function Purpose: 
        To determine a mapping of cluster index to emotion (aka determine which
        emotion each cluster refers to)
    Returns a dictionary with:
        -key: cluster index (integer in range [0,k-1])
        -value: emotion category assigned to this cluster (integer in range[0,k-1])

    ex: kmeansClusterIndex_to_emotion[clusterIndex] --> emotion

    This function also provides code for two different approaches for cluster/emotion assignemnt
    '''


    '''
    ------------------------------------------
    SETUP: 
    Needed for both Approach 1 and Approach 2
    -----
    '''

    #emotionCounter[emotion] = number of data points in the data set classified as this emotion
    emotionCounter = collections.Counter()
    clusterList = [] #list of length k, clusterList[0] = a counter of how many data points of each emotion type were clustered to group 0
    for i in xrange(0, k): clusterList.append(collections.Counter())
    print len(clusterAssignments)
    for i in range(0, len(clusterAssignments)):
        if clusterAssignments[i] != None:
            clusterIndex = clusterAssignments[i]
            emotion = data[i][1]
            emotionCounter[emotion] += 1
            clusterList[clusterIndex][emotion] += 1

    clusterPercentList = []##list of length k, clusterPercentList[clusterIndex] = dictionary (key: emotion --> value: percent of this emotion's total data points assigned to this cluster)
    for i in xrange(0, k): clusterPercentList.append(dict())
    for clusterIndex in range(0, k):
        counter = clusterList[clusterIndex]
        for emotion, count in counter.items():  clusterPercentList[clusterIndex][emotion] = float(count)/float(emotionCounter[emotion])


    #print "cluster list: ", clusterList
    #print "emotionCounter: ", emotionCounter
    #print "clusterPercentList: ", clusterPercentList
    '''
    -----
    END SETUP
    -----------------------------------------
    '''

 
    '''
    ------------------------------------------
    APPROACH 1: 
    assign a cluster to the emotion that is most represented (based on count) in that cluster
    -----
    '''
    ''' 

    kmeansClusterIndex_to_emotion = dict()
    for i in range(0,k):
        if len(clusterList[i].most_common(1)) == 0: kmeansClusterIndex_to_emotion[i] = None
        else: kmeansClusterIndex_to_emotion[i] = (clusterList[i].most_common(1))[0][0]
        #kmeansClusterIndex_to_emotion[clusterIndex] --> emotion

    #print "kmeansClusterIndex --> emotion: ", kmeansClusterIndex_to_emotion
    return kmeansClusterIndex_to_emotion

    '''
    '''
    -----
    END APPROACH 1
    -----------------------------------------
    '''


    '''
    -----------------------------------------
    APPROACH 2: 
    assign an emotion to the cluster containing the highest percent of the emotion's data points
    -----
    '''
    
    kmeansClusterIndex_to_emotion = dict()

    #assign emotions to clusters in order of least prevelant emotion first

        #work around code to sort emotions by count
    emotionCounterRevItems = [(count, emotion) for emotion, count in emotionCounter.items()]
    sortedEmotions = sorted(emotionCounterRevItems)
    print "sortedEmotions: ", sortedEmotions


    for count, emotion in sortedEmotions:
        highestPercent = None
        bestCluster = None
        for clusterIndex in range(0, len(clusterPercentList)):
            if clusterIndex in kmeansClusterIndex_to_emotion: continue #don't want to assign two different emotions to the same cluster
            percentCounter = clusterPercentList[clusterIndex]
            if emotion not in percentCounter: continue
            if bestCluster == None or percentCounter[emotion] > highestPercent:
                bestCluster = clusterIndex
                highestPercent = percentCounter[emotion]
        kmeansClusterIndex_to_emotion[bestCluster] = emotion

    print "kmeansClusterIndex--> emotion: ", kmeansClusterIndex_to_emotion
    return kmeansClusterIndex_to_emotion

    '''
    -----
    END APPROACH 2
    --------------------------------------------
    '''


def convertDataPointsToDictionaries(data):
    ''' 
    returns list of size len(data). 
    For the returned list, list[0] = dictionary representation of data[0] where 
    dictionary[pixelIndex] = pixelValue
    '''

    examples = [] #list of dictionarys (pixel index --> pixel value)
    for i in range(0, len(data)):
        pixels = data[i][0]
        pixelDict = {}
        for j in range(0, len(pixels)): pixelDict[j] = pixels[j]
        examples[i] = pixelDict

    return examples

def clusterData(data, centroids):
    '''
    This function assigns each data point in data, to a centroid in centroids
    return value:
        -list of cluster assignments where list[0] = cluster data[0] was assigned to
    '''

    nDataPoints = len(data)
    clusters = [-1]*nDataPoints
    for i in range(0, nDataPoints):
        dataPoint = data[i]
        closetCentroidIndex = returnClosetCentroid(dataPoint, centroids)
        clusters[i] = closetCentroidIndex

    return clusters

def get2dImage(image):
    '''
    Function Purpose:
        converts an image (represented as a list of pixels) into a 2D arry
    '''
    row = []
    twoDArray = []
    d = 48
    if source == "jaffe":
        d = 256
    for i in range(0, len(image)):
        if i % d == 0 and i!= 0:
            twoDArray.append(row)
            row = []
        row.append(image[i])
    twoDArray.append(row)
    return twoDArray


def faceFeatureExtractor(image, combo = False):
    image1d = image
    image = get2dImage(image)
    features = {}
    image =  np.uint8(np.array(image))
    face_cascade = cv2.CascadeClassifier('opencv/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
    face = face_cascade.detectMultiScale(image, minSize=(2, 2))
    facewidth = 256.0
    faceheight = 256.0
    e1x=80
    e1y=90
    e1w=40
    e1h=65
    e2x=140
    e2y=90
    e2w=40
    e2h=45
    mx=100
    my=180
    mw=55
    mh=40

    if len(face) ==1 :
        f = face[0]
        #features["facex"] = f[0]
        #features["facey"] = f[1]
        #features["facew"] = f[2]
        #facewidth = f[2]
        #features["faceh"] = f[3]
        faceheight = f[3]
        # cv2.rectangle(image,(f[0],f[1]),(f[0]+f[2],f[1]+f[3]),(255,0,0),1)
        #cv2.rectangle(image,(0,0,0,0),(255,0,0),2)
        #img2 = cv2.drawKeypoints(np.uint8(np.array(image)),None,None,(255,0,0),4)
        
        #plt.imshow(image),plt.show()
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    eye_cascade = cv2.CascadeClassifier('opencv/opencv/data/haarcascades/haarcascade_eye.xml')
    eye = eye_cascade.detectMultiScale(image, minSize=(0, 0))
    if len(eye)>=1:
        e = eye[0]
        e1x = e[0]
        e1y = e[1]
        e1w = e[2]
        e1h = e[3]
        #features["eye1x"] = e[0]
        #features["eye1y"] = e[1]
        # print "e1w", e[2]
        # print "e1h", e[3]
        features["eye1w"] = e[2]/facewidth
        features["eye1h"] = e[3]/faceheight
        #cv2.rectangle(image,(e[0],e[1]),(e[0]+e[2],e[1]+e[3]),(255,0,0),1)
    if len(eye)>=2:
        e = eye[1]
        e2x = e[0]
        e2y = e[1]
        e2w = e[2]
        e2h = e[3]        
        #features["eye2x"] = e[0]
        #features["eye2y"] = e[1]
        features["eye2w"] = e[2]/facewidth
        #cv2.rectangle(image,(e[0],e[1]),(e[0]+e[2],e[1]+e[3]),(255,0,0),1)
        features["eye2h"] = e[3]/faceheight

    smile_cascade = cv2.CascadeClassifier('opencv/opencv/data/haarcascades/mouth.xml')
    smile = smile_cascade.detectMultiScale(image)
    if len(smile)>=1:
        s = smile[0]
        mx = s[0]
        my = s[1]
        mw = s[2]
        mh = s[3]
        features["smilew"] = s[2]/facewidth
        #cv2.rectangle(image,(s[0],s[1]),(s[0]+s[2],s[1]+s[3]),(255,0,0),1)
        features["smileh"] = s[3]/faceheight     

    #plt.imshow(image,'gray'),plt.show()
    # cv2.rectangle(image,(e1x,e1y),(e1x+e1w,e1y+e1h),(255,0,0),1)
    # cv2.rectangle(image,(e2x,e2y),(e2x+e2w,e2y+e2h),(255,0,0),1)
    # cv2.rectangle(image,(mx,my),(mx+mw,my+mh),(255,0,0),1)

        # cv2.rectangle(image,(15,33),(35,43),(255,0,0),1)
    #ret,thresh = cv2.threshold(image,127,255, cv2.THRESH_TOZERO_INV)
#    plt.imshow(thresh,'gray'),plt.show()

     #   fancyFeatureExtractor("fast", image)       

     #to combine with featurizePixelList
    if combo is True:
        features.update(featurizePixelList(image1d, e1x, e1y, e1w, e1h, e2x, e2y, e2w, e2h, mx, my, mw, mh))
    return features


def fancyFeatureExtractor(extractor, image):
    '''
    Function Purpose:
        takes in the name of the extractor "sift", "surf", or "fast" and a 2-d pixel array
        and returns list of sift features in the form:
            ([list of key points, array(list of descriptor lists)]
    '''

    drawImage = False
    spoints = {}
    if extractor == "sift":
        sift = cv2.SIFT()
        spoints = sift.detectAndCompute(np.uint8(np.array(image)), None)

    elif extractor == "surf":
        surf = cv2.SURF(2000)   
        spoints = surf.detectAndCompute(np.uint8(np.array(image)), None)
    elif extractor == "fast":
        image = np.array(image, dtype=np.uint8)
        fast = cv2.FastFeatureDetector()
        kp = fast.detect(image)
        freak = cv2.DescriptorExtractor_create('SURF')
        spoints = freak.compute(image,kp)

    if drawImage:
        img2 = cv2.drawKeypoints(np.uint8(np.array(image)),spoints[0],None,(0,153,255),4)
        plt.imshow(img2),plt.show()

    return spoints

def map_point_to_section(point):
    x, y = point
    if x <= 23:
        if y <= 23: return "eye1"
        else: return "eye2"
    else: return "mouth"

def getPartitionedFeatures(spoints):
    eye1 = None
    eye2 = None
    mouth = None

    keypoints, featureVectors = spoints
    for i in range(0, len(keypoints)):
        keypoint = keypoints[i]
        center = keypoint.pt
        faceSection = map_point_to_section(center)
        if faceSection == "eye1" and eye1 == None: eye1 = featureVectors[i]
        elif faceSection == "eye2" and eye2 == None: eye2 = featureVectors[i]
        elif faceSection == "mouth" and mouth == None: mouth = featureVectors[i]

    return eye1, eye2, mouth

def runFancyKMeans(training_data, testing_data, extractor):
   # print "starting surf"
    
    #///////////////////// flags ///////////////////
    normalize = False
    kmeanstype = "independant" #"concat" # or "first" or "independant" # use this flag to determine how to handle features for kmeans
   # kmeanstype = "partitioned"
   #////////////////////////////////////////////////

    data = testing_data
    pixelList = [pixels for pixels, emotion in data]
    
    featureToImageMap = []
    
    surfFeaturesList = []
    if kmeanstype == "concat":
        surfFeaturesList = [[]]*len(pixelList)

    eye1FeatureList = []
    eye2FeatureList = []
    mouthFeatureList = []

    #for x in range(1):
    for x in range(len(pixelList)):
        twoDArray = get2dImage(pixelList[x])
        spoints = fancyFeatureExtractor(extractor, twoDArray)

        #only add 1st feature for simplicity with kmeans:
        if kmeanstype == "first":
            if spoints is not None and spoints[1] is not None:
                surfFeaturesList.append(list(spoints[1][0]))
            else:
                surfFeaturesList.append([])

        #add all features as independant points to kmeans:
        if kmeanstype == "independant":
            if spoints is not None and spoints[1] is not None:
                for point in spoints[1]:
                    surfFeaturesList.append(list(point))
                    featureToImageMap.append(x) #specifys that this feature maps to this image

        #add concatenate all features to a giant feature     
        if kmeanstype == "concat":
            if spoints is not None and spoints[1] is not None:
                for point in spoints[1]:
                    for i in point:
                        surfFeaturesList[x].append(i)
            # else: 
            #     surfFeaturesList[x] = [1]

        #parition 3 image keypoints into: eye1, eye2, mouth. Run kmeans 3 separate times
        if kmeanstype == "partitioned":
            eye1Feature, eye2Feature, mouthFeature = getPartitionedFeatures(spoints)
            eye1FeatureList.append(eye1Feature)
            eye2FeatureList.append(eye2Feature)
            mouthFeatureList.append(mouthFeature)

    #normalize features list before kmeans
    if normalize:
        np.linalg.norm(surfFeaturesList)
        surfFeaturesList = scipy.cluster.vq.whiten(surfFeaturesList)

    k = 7
    maxIter = 10
    if kmeanstype != "partitioned":        
        #print cv2.BFMatcher().match(surfFeaturesList[0], surfFeaturesList[1])
        #clusters = cv2.kmeans(np.array(surfFeaturesList), k, (cv2.TERM_CRITERIA_MAX_ITER, 10, .1), 1, cv2.KMEANS_RANDOM_CENTERS)
        #clusters, centroids = kmeansFeatures(surfFeaturesList, k, maxIter)
        #evaluateClusters(clusters, training_data, k)
        

        clusters, centroids = kmeans(surfFeaturesList, k, maxIter)

        if "independant": 
            clusters = getActualClusters(clusters, featureToImageMap, pixelList)

        evaluateClusters(clusters, data, k)
    
    else:
        eye1Clusters, eye1Centroids = kmeans(eye1FeatureList, k, maxIter)
        eye2Clusters, eye2Centroids = kmeans(eye2FeatureList, k, maxIter)
        mouthClusters, mouthCentroids = kmeans(mouthFeatureList, k, maxIter)

        evaluatePartionedClusters(eye1Clusters, eye2Clusters, mouthClusters, data, k)


def runNearestNeighbours(training_data, testing_data, extractor):
    numCorrect = 0.0
    totalNum = 0.0
    pixelList = [pixels for pixels, emotion in testing_data]
    for x in range(len(pixelList)):
        twoDArray = get2dImage(pixelList[x])
        spoints = fancyFeatureExtractor(extractor, twoDArray)
        assignment = nearestNeighbour(twoDArray, spoints, training_data, extractor)
        totalNum += 1
        if assignment == training_data[x][1]:
            numCorrect +=1
    print "accuracy: ", numCorrect/totalNum
    return

def nearestNeighbour(image1, features, training_data, extractor):
    if features[1] is not None:
        minDistance = float("inf")
        bestEmotion= -1
        for pixels,emotion in training_data:
            row = []
            twoDArray = []
            twoDArray = get2dImage(pixels)

            spoints = None
            if extractor == "sift":
                sift = cv2.SIFT()
                spoints = sift.detectAndCompute(np.uint8(np.array(twoDArray)), None)
            elif extractor == "surf":
                surf = cv2.SURF(4000)   
                spoints = surf.detectAndCompute(np.uint8(np.array(twoDArray)), None)
            elif extractor == "fast":
                image = np.array(twoDArray, dtype=np.uint8)
                fast = cv2.FastFeatureDetector()
                kp = fast.detect(image)
                freak = cv2.DescriptorExtractor_create('SURF')
                spoints = freak.compute(image,kp)   
      

            match = cv2.BFMatcher(cv2.NORM_L1).match(spoints[1], features[1])
            distances = [m.distance for m in match]
            d = sum(distances)
            if d < minDistance and len(distances) > 0:
                minDistance = d
                bestEmotion = emotion
               # drawMatches(np.uint8(np.array(image1)), features[0], np.uint8(np.array(twoDArray)), spoints[0], match)
        return bestEmotion 
    else:
        return random.randrange(0,7)

def getActualClusters(clusters, featureToImageMap, pixelList):
    '''
    takes in a the cluster assignments for independant features,
    determines which images those features correspond to, 
    assigns the image to the cluster to which most of its features are assigned,
    returns cluster list in the expected form of a dict declaring which cluster each image is assigned to
    '''
    actualClusters = [0] * len(pixelList)
    prevImage = -1
    imageAssignments = [] 
    for i in range(len(clusters)):
        image = featureToImageMap[i]
        if image == prevImage:
            imageAssignments.append(clusters[i])
        else:
            if prevImage != (-1):
                if imageAssignments == []:
                    actualClusters[prevImage] = random.randrange(0,7)
                else:    
#                 print imageAssignments
#                 print max(set(imageAssignments), key=imageAssignments.count)
                    actualClusters[prevImage] = max(set(imageAssignments), key=imageAssignments.count)
            imageAssignments = []
        prevImage = image
    return actualClusters



# def returnClosetCentroidFeatures(point, centroidsPrev):
#     '''
#     attempt to reqwrite the return closest centroid features to work with sift/surf features. currently does nothing/not used
#     ----
#     '''
#     runningMin = None
#     closetCentroidIndex = 0 #default to being the centroid at index 0
#     nCentroids = len(centroidsPrev)
#     for i in range(nCentroids):
#         centroid = centroidsPrev[i]
#         covar = np.cov(point, rowvar=0)
#         invcovar = np.linalg.inv(covar)
#        # distance = scipy.spatial.distance.mahalanobis(centroid, point, invcovar)
#         distance = len(cv2.BFMatcher().match(np.array(centroid), np.array(point)))
#         if (runningMin == None) or ((distance < runningMin)):
#             runningMin = distance
#             closetCentroidIndex = i

#         if((distance == runningMin)): closetCentroidIndex = random.choice([closetCentroidIndex, i])
#     return closetCentroidIndex


### Found on stack overflow http://stackoverflow.com/questions/20259025/module-object-has-no-attribute-drawmatches-opencv-python
# credit to rayryeng
def drawMatches(img1, kp1, img2, kp2, matches):
    """
    My own implementation of cv2.drawMatches as OpenCV 2.4.9
    does not have this function available but it's supported in
    OpenCV 3.0.0

    This function takes in two images with their associated 
    keypoints, as well as a list of DMatch data structure (matches) 
    that contains which keypoints matched in which images.

    An image will be produced where a montage is shown with
    the first image followed by the second image beside it.

    Keypoints are delineated with circles, while lines are connected
    between matching keypoints.

    img1,img2 - Grayscale images
    kp1,kp2 - Detected list of keypoints through any of the OpenCV keypoint 
              detection algorithms
    matches - A list of matches of corresponding keypoints through any
              OpenCV keypoint matching algorithm
    """


    # Create a new output image that concatenates the two images together
    # (a.k.a) a montage
    rows1 = img1.shape[0]
    cols1 = img1.shape[1]
    rows2 = img2.shape[0]
    cols2 = img2.shape[1]


    out = np.zeros((max([rows1,rows2]),cols1+cols2,3), dtype='uint8')

    # Place the first image to the left
    out[:rows1,:cols1,:] = np.dstack([img1, img1, img1])

    # Place the next image to the right of it
    out[:rows2,cols1:cols1+cols2,:] = np.dstack([img2, img2, img2])

    # For each pair of points we have between both images
    # draw circles, then connect a line between them
    for mat in matches:

        # Get the matching keypoints for each of the images
        img1_idx = mat.queryIdx
        img2_idx = mat.trainIdx

        if img1_idx < len(kp1) and img2_idx < len(kp2):

            # x - columns
            # y - rows
            (x1,y1) = kp1[img1_idx].pt
            (x2,y2) = kp2[img2_idx].pt

            # Draw a small circle at both co-ordinates
            # radius 4
            # colour blue
            # thickness = 1
            cv2.circle(out, (int(x1),int(y1)), 4, (255, 0, 0), 1)   
            cv2.circle(out, (int(x2)+cols1,int(y2)), 4, (255, 0, 0), 1)

            # Draw a line in between the two points
            # thickness = 1
            # colour blue
            cv2.line(out, (int(x1),int(y1)), (int(x2)+cols1,int(y2)), (255, 0, 0), 1)


    # Show the image
    plt.imshow(out),plt.show()




def runSGD(training_data, testing_data, featureExtractor):
    '''
    This function holds code to run stochastic gradient descent
    '''
    learnPredictor(training_data, testing_data, featureExtractor)

def runKmeans(training_data, testing_data, kmeansType):
    '''
    Function Purpose:
        This function holds code to run kmeans clustering. It sets up the data
        based on the format specified by the 'kmeansType' argument, runs kmeans, 
        then evaluates the calculated centroid's ability to accurately predict 
        the emotion of an image
    '''

    '''some functions might want data points represented as dictionaries'''
    #dataAsDictionaries = convertDataPointsToDictionaries(training_data):


    '''Code to convert data from list of tuples (pixels, emotion) to just list of pixels 
    (required for kmeans) '''

    trainingPixelList = None
    testingPixelList = None

    if kmeansType == "pixel list":
        trainingPixelList = [pixels for pixels, emotion in training_data]
        testingPixelList = [pixels for pixels, emotion in testing_data]

    elif kmeansType == "featurize pixel list":
        trainingPixelList = []
        testingPixelList = []

        #For each image, must create a list of the pixels corresonding only to the eye1, eye2, 
            #and mouth sections of the image
        #For each image, these pixels must be listed in a standardized order
            #ex: image1 = [eye1_pixel1, eye1_pixel 2, ..., eye2_pixel1, eye2_pixel2..., mouth1, mouth2, ...]; 
            #   image2 = [eye1_pixel1, eye1_pixel 2, ..., eye2_pixel1, eye2_pixel2..., mouth1, mouth2, ...]; 
        
        trainingPixelDicts = [featurizePixelList(pixels)for pixels, emotion in training_data]
        
        for pixelDict in trainingPixelDicts:
            #enter pixel values into the pixel list in a standarized order
            sortedKeys = sorted(pixelDict.keys())
            pixelList = []
            for i in range(0, len(sortedKeys)):
                key = sortedKeys[i]
                pixelList.append(pixelDict[key])
            trainingPixelList.append(pixelList)

        testingPixelDicts = [featurizePixelList(pixels)for pixels, emotion in testing_data]
        
        for pixelDict in testingPixelDicts:
            #enter pixel values into the pixel list in a standarized order
            sortedKeys = sorted(pixelDict.keys())
            pixelList = []
            for i in range(0, len(sortedKeys)):
                key = sortedKeys[i]
                pixelList.append(pixelDict[key])
            testingPixelList.append(pixelList)
    
    '''kmeans clustering'''

    k = 7
    maxIter = 50
    clusters, centroids = kmeans(trainingPixelList, k, maxIter)
    evaluateClusters(clusters, training_data, k)

    '''use centroids to cluster test data'''
    clusters = clusterData(testingPixelList, centroids)
    evaluateClusters(clusters, testing_data, k)


def testInputData(training_data, testing_data1, testing_data2):
    '''
    Function Purpose: 
        This function takes in parsed training and testing data and prints out
        examples from each data set to make sure they are formatted correctly
    '''

    print "---- TRAINING DATA ----"
    print "# data points: ", len(training_data)
    print "----1st data point: ---"
    print "Emotion: ", training_data[0][1]
    print "Pixels: ", training_data[0][0]
    print "----last data point: ----"
    print "Emotion: ", training_data[-1][1]
    print "Pixels: ", training_data[-1][0]
    print "---- TESTING DATA1 ----"
    print "# data points: ", len(testing_data1)
    print "-----1st data point: ----"
    print "Emotion: ", testing_data1[0][1]
    print "Pixels: ", testing_data1[0][0]
    print "----last data point: ----"
    print "Emotion: ", testing_data1[-1][1]
    print "Pixels: ", testing_data1[-1][0]
    
    if testing_data2 != None:
        print "---- TESTING DATA2 ----"
        print "# data points: ", len(testing_data2)
        print "1st data point: "
        print "Emotion: ", testing_data2[0][1]
        print "Pixels: ", testing_data2[0][0]
        print "---- TESTING DATA2 ----"
        print "# data points: ", len(testing_data2)
        print "last data point: "
        print "Emotion: ", testing_data2[-1][1]
        print "Pixels: ", testing_data2[-1][0]

def combinedExtractor(x):
    features = faceFeatureExtractor(x, combo = True)
    return features

#def featurizePixelList(pixelsOneImage, e1x=10, e1y=10, e1w=10, e1h=10, e2x=30, e2y=10, e2w=10, e2h=10, mx=15, my=33, mw=18, mh=10 ):
def featurizePixelList(pixelList, e1x=80, e1y=90, e1w=40, e1h=65, e2x=140, e2y=90, e2w=40, e2h=65, mx=95, my=175, mw=60, mh=30 ):
    '''
    Function Purpose:
        Takes in the entire list of pixels for one image, returns a list of lists 
        (each corresponds to pixels for one feature) 
    '''
    eye1LM = e1x
    eyeSeparation = max(e2x-e1x+e1w, e1x-20)
    eye2LM = e2x
    eyesTY = e1y
    eyeH = e1h
    eyeW = e1w
    mouthTY = my
    mouthH = mh
    mouthW = mw
    mouthLM = mx
    eyeSeparation = 37#10 #separation between two eyes


    features = {}
    lenPixels = len(pixelList)
    numCols = 256
    if source == 'kaggle': numCols = 48 

    if useBW:
        image = get2dImage(pixelList)
        image =  np.uint8(np.array(image))
        bwPixelList = []
        ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
        for i in range(0,len(thresh)):
            for j in range(0,len(thresh[i])):
                bwPixelList.append(thresh[i][j])
        pixelList = bwPixelList
    #cv2.rectangle(image,(eye1LM,eyesTY),(eye1LM+eyeW,eyesTY+eyeH),(255,0,0),1)
    #cv2.rectangle(image,(eye2LM,eyesTY),(eye2LM+eyeW,eyesTY+eyeH),(255,0,0),1)
    #cv2.rectangle(image,(mouthLM,mouthTY),(mouthLM+mouthW,mouthTY+mouthH),(255,0,0),1)
    #plt.imshow(image,'gray'),plt.show()


    
    for i in range(eyesTY-1, eyesTY+eyeH-1): #rows of the face the eyes are located in
        features.update({str(oldIndex):pixelList[oldIndex] for oldIndex in range(numCols*i + eye1LM,((i*numCols)+eye1LM+eyeW))}) 
        features.update({str(oldIndex):pixelList[oldIndex] for oldIndex in range(((i*numCols)+eye2LM),(i*numCols)+eye2LM+eyeW)})
    for j in range(mouthTY-1, mouthTY+mouthH-1): #rows of the face the mouth is located in
       features.update({str(oldIndex):pixelList[oldIndex] for oldIndex in range((j*numCols) + mouthLM, (j*numCols)+mouthLM+mouthW)})
    
    return features 
        


def contoursFeatureExtractor(image):
    features={}
    image = get2dImage(image)

    image =  np.uint8(np.array(image))
    #imgray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh,cv2.cv.CV_RETR_LIST,cv2.CHAIN_APPROX_NONE)
    contours.sort(key=lambda x: cv2.contourArea(x), reverse = True)
    #cv2.drawContours(image,contours[2:],-1,(0,0,255),2)
    #plt.imshow(thresh, "gray"),plt.show()
    plt.imshow(image, "gray"),plt.show()
    features["numContours"] = len(contours)
    if len(contours) >= 1:
        features["c1area"] = cv2.contourArea(contours[0])
        x,y,w,h = cv2.boundingRect(contours[0])
        features["c1aspectratio"] = float(w)/h
        area = cv2.contourArea(contours[0])
        features["c1extent"] = float(area)/(w*h)
        features["ed1"] = np.sqrt(4*area/np.pi)
        # (x,y),(MA,ma),angle = cv2.fitEllipse(contours[0])
        # features["orientation1"] = angle
    if len(contours) >= 2:
        features["c2area"] = cv2.contourArea(contours[1])
        x,y,w,h = cv2.boundingRect(contours[1])
        features["c2aspectratio"] = float(w)/h
        area = cv2.contourArea(contours[1])
        features["c2extent"] = float(area)/(w*h)
        features["ed2"] = np.sqrt(4*area/np.pi)
    
    if len(contours) >= 3:
        features["c3area"] = cv2.contourArea(contours[2])
        x,y,w,h = cv2.boundingRect(contours[2])
        features["c3aspectratio"] = float(w)/h
        area = cv2.contourArea(contours[2])
        features["c3extent"] = float(area)/(w*h)
        features["ed3"] = np.sqrt(4*area/np.pi)
    
 
    # (x,y),(MA,ma),angle = cv2.fitEllipse(contours[1])
    # features["orientation2"] = angle
    # (x,y),(MA,ma),angle = cv2.fitEllipse(contours[2])
    # features["orientation3"] = angle
    #print contours[0]
    return features

def randomizeTrainingData(all_data, seed):
    '''
    Function Purpose: 
    Takes in a data set and randomly divies it up into training and testing data. Note, the 
    number of examples put into the training set is given by: jaffe_training_set_size (global variable)

    Arguments:
        -all_data: list of tuples of form (pixels, emotion) for every image in the data set
    Return Value:
        -tuple of form: (training examples, testing exampless)
    '''
    if seed != None: random.seed(seed)
    numSamples = 213
    trainIndices = random.sample(range(numSamples), jaffe_training_set_size)
    j_train_data = [all_data[index] for index in trainIndices]
    j_test_data = [all_data[i] for i in range(numSamples) if i not in trainIndices]

    return j_train_data, j_test_data

def main():
    '''
    Program takes 4 parameters: <data file name> <data type> <linear classifier> <feature extractor>
        -data file name is either: fer2013.csv or jaffePixelData.txt
        -data type is either: "kaggle" or "jaffe"
        -linear classifier is either: 'kmeans', 'sgd', 'knn'
        -feature extractor is either: 'pl', 'grid', 'sift', 'surf', 'fast', 'cascade'
    '''

    if len(sys.argv) < 5: raise Exception("Not enough arguments given. EXPECTED FORMAT: python baseline.py <input file name> <data type (either \"kaggle\" or \"jaffe\")> <liner classifier> <feature extractor>")
    
    testing_data = None
    training_data = None

    data_type = str(sys.argv[2])
    linear_classifier = str(sys.argv[3])
    feature_extractor = str(sys.argv[4])

    if data_type == 'kaggle':
        training_data, testing_data1, testing_data2 = parseKaggleData(sys.argv[1])
        '''** Note: if smallKaggleDataSet = true, the value of testing_data2 will be None **'''
        testing_data = testing_data1
        source = "kaggle"
    if data_type == 'jaffe':
        training_data, testing_data, all_data = parseJaffeData(sys.argv[1])
        source = "jaffe"
        seed = 3 #either set a value or set to None
        if randomize_jaffe_data: training_data, testing_data = randomizeTrainingData(all_data, seed)

    
    if linear_classifier == 'sgd':
        if feature_extractor == 'pl':
            runSGD(training_data, testing_data, pixelIndexFeatureExtractor)
        elif feature_extractor == 'grid':
            runSGD(training_data, testing_data, featurizePixelList)
        elif feature_extractor == "combo":
            runSGD(training_data, testing_data, combinedExtractor)
        elif feature_extractor == "contour":
            runSGD(training_data, testing_data, contoursFeatureExtractor)
        elif feature_extractor == "plbw":
            useBW = True
            runSGD(training_data, testing_data, pixelIndexFeatureExtractor)
        elif featureExtractor == "gridbw":
            useBW = True
            runSGD(training_data, testing_data, featurizePixelList)
        elif feature_extractor == "combobw":
            runSGD(training_data, testing_data, combinedExtractor)
        else: 
            raise Exception("Invalid linear classifier & feature extractor combination")

    elif linear_classifier == 'kmeans':
        if feature_extractor == 'pl':
            runKmeans(training_data, testing_data, 'pixel list')
        elif feature_extractor == 'grid':
            runKmeans(training_data, testing_data, 'featurize pixel list')
        elif feature_extractor == 'sift':
            runFancyKMeans(training_data, testing_data, "sift")
        elif feature_extractor == 'surf':
            runFancyKMeans(training_data, testing_data, "surf")
        elif feature_extractor == 'fast':
            runFancyKMeans(training_data, testing_data, "fast")
        else: 
            raise Exception("Invalid linear classifier & feature extractor combination")

    elif linear_classifier == 'knn':
        if feature_extractor == 'sift':
            runNearestNeighbours(training_data, testing_data, "sift")
        elif feature_extractor == 'surf':
            runNearestNeighbours(training_data, testing_data, "surf")
        elif feature_extractor == 'fast':
            runNearestNeighbours(training_data, testing_data, "fast")
        else: 
            raise Exception("Invalid linear classifier & feature extractor combination")
   
    else:
        raise Exception("Invalid linear classifier & feature extractor combination")


if __name__ == '__main__':
  main()
