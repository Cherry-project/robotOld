import numpy as np
import cv2

# Cascade XML files that help track faces, eyes, and mouths
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouthCascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')

# Helper function that finds a face, set of eyes, and a mouth


def findFacialFeatures(frame):
    face = findFace(frame)
    eyes = findEyes(frame, face)
    mouth = 0, 0, 0, 0

    # To filter out mouth outliers, eyes must be present to detect the mouth
    if len(eyes) > 0:
        mouth = findMouth(frame, eyes, face)

    return face, eyes, mouth

# Tracks face and returns the first one detected


def findFace(frame):
    faces = faceCascade.detectMultiScale(
        frame,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(50, 50),
        flags = cv2.CASCADE_SCALE_IMAGE)

    if len(faces) > 0:
        return faces[0]

    return 0, 0, 0, 0

# Tracks eyes and returns the first two detected


def findEyes(frame, face):
    # Tracks eyes
    eyes = eyeCascade.detectMultiScale(
        frame,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(50, 50),
        flags = cv2.CASCADE_SCALE_IMAGE)

    if len(eyes) > 2:
        eyes = eyes[:2]

    return eyes

# Track mouth and returns the first one detected


def findMouth(frame, eyes, face):
    mouths = mouthCascade.detectMultiScale(
        frame,
        scaleFactor=1.2,
        minNeighbors=8,
        minSize=(30, 20),
        flags = cv2.CASCADE_SCALE_IMAGE)

    if len(mouths) <= 0:
        return 0, 0, 0, 0

    # To detect mouth, the mouth points must be below the eyes and within the
    # face
    eyeBottom = 0

    for eye in eyes:
        eyeX, eyeY, eyeW, eyeH = eye
        if (eyeY + eyeH) > eyeBottom:
            eyeBottom = eyeY + eyeH

    faceX, faceY, faceW, faceH = face
    faceBottom = faceY + faceH

    for mouth in mouths:
        mouthX, mouthY, mouthW, mouthH = mouth
        if mouthY > (eyeBottom + 50) and (mouthY + mouthH) < faceBottom:
            return (mouthX - 20, mouthY, mouthW + 40, mouthH)

    return 0, 0, 0, 0

# Draws a rectangle on the features detected


def drawFacialFeatureBounds(vis, face, eyes, mouth):
    x, y, w, h = face
    cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 255, 0), 1)

    for (x, y, w, h) in eyes:
        cv2.rectangle(vis, (x, y), (x + w, y + h), (255, 0, 0), 1)

    x, y, w, h = mouth
    cv2.rectangle(vis, (x, y), (x + w, y + h), (0, 0, 255), 1)

# Reshapes the optical flow


def reshape(img, flow, step=8):
    h, w = img.shape[:2]
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1)
    fx, fy = flow[y, x].T
    lines = np.vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    return lines, vis

# Draws the optical flow of tracked features


def draw_flow(vis, lines, eyes, mouth):
    # Rectangle for each feature
    rectangle_eye1 = [0, 0, 0, 0]
    rectangle_eye2 = [0, 0, 0, 0]
    rectangle_mouth = [0, 0, 0, 0]

    # new_lines_face = []
    opt_lines_eye1 = []
    opt_lines_eye2 = []
    opt_lines_mouth = []
    opt_lines_mouth_up = []

    # G ets the coordinates for each feature
    if (len(eyes) == 2):
        x, y, w, h = eyes[0]
        rectangle_eye1 = [x, y, x + w, y + h]
        x, y, w, h = eyes[1]
        rectangle_eye2 = [x, y, x + w, y + h]
        x, y, w, h = mouth
        rectangle_mouth = [x, y, x + w, y + h]

    # Number of lines moving/Optical Flow for Face
    for (x1, y1), (x2, y2) in lines:
        if rectangle_eye1[0] < x1 < rectangle_eye1[2] and rectangle_eye1[1] \
                < y1 < rectangle_eye1[3]:
            opt_lines_eye1.append([[x1, y1], [x2, y2]])
        if rectangle_eye2[0] < x1 < rectangle_eye2[2] and rectangle_eye2[1] \
                < y1 < rectangle_eye2[3]:
            opt_lines_eye2.append([[x1, y1], [x2, y2]])

        if rectangle_mouth[0] < x1 < rectangle_mouth[2] and \
                rectangle_mouth[1] < y1 < rectangle_mouth[3]:
            opt_lines_mouth.append([[x1, y1], [x2, y2]])
            if (y1 - y2) > 1:
                opt_lines_mouth_up.append([[x1, y1], [x2, y2]])

    # Puts all the points into a nice numpy array
    opt_lines_eye1 = np.array(opt_lines_eye1)
    opt_lines_eye2 = np.array(opt_lines_eye2)
    opt_lines_mouth = np.array(opt_lines_mouth)
    opt_lines_mouth_up = np.array(opt_lines_mouth_up)

    # Draws optical flow lines
    # lines are consist of such information => [ original_x, original_y ,
    # later_x, later_y ]
    cv2.polylines(vis, opt_lines_mouth_up, 0, (0, 255, 255))

    return opt_lines_eye1, opt_lines_eye2, opt_lines_mouth, \
        opt_lines_mouth_up, rectangle_mouth

# Calculates the emotion based on movement


def calculate_emotion(outward, inward, currentEmotion):
    # If there's enough motion that passes the threshold
    if outward + inward > 10:
        # If there's motion and the current emotion is neutral
        if currentEmotion == 0:
            # If there's more outward motion than inward
            if outward > inward:
                # Sets it to happiness
                currentEmotion = 1
            # If there's more inward motion than outward
            else:
                # Sets it to sad
                currentEmotion = -1
        # If the current emotion is sadness
        elif currentEmotion == -1:
            # If there's more outward motion than inward
            if outward > inward:
                # Sets it to neutral
                currentEmotion = 0
        # If the current emotion is sadness
        elif currentEmotion == 1:
            # If there's more inward motion than outward
            if outward < inward:
                # Sets it to neutral
                currentEmotion = 0

    return currentEmotion

# Counts the movement lines going up


def count_lines(opt_lines_mouth_up, rectangle_mouth):
    outward = 0
    inward = 0

    if len(opt_lines_mouth_up) > 0:
        for (x1, y1), (x2, y2) in opt_lines_mouth_up:
            if x1 < (rectangle_mouth[0] + rectangle_mouth[2]) / 2:
                if x2 > x1:
                    inward += 1
                else:
                    outward += 1
            else:
                if x2 > x1:
                    outward += 1
                else:
                    inward += 1

    return outward, inward


def outputEmotion(emotion):
    if emotion == 1:
        cv2.putText(showFrame, "Happy!", (20, 50), cv2.FONT_HERSHEY_PLAIN,
                    5.0, (255, 255, 0), thickness=1, lineType=cv2.CV_AA)
    elif emotion == -1:
        cv2.putText(showFrame, "Sad!", (20, 50), cv2.FONT_HERSHEY_PLAIN,
                    5.0, (0, 255, 0), thickness=1, lineType=cv2.CV_AA)
    else:
        cv2.putText(showFrame, "Neutral!", (20, 50), cv2.FONT_HERSHEY_PLAIN,
                    5.0, (0, 255, 255), thickness=1, lineType=cv2.CV_AA)


def emotion_recognition(img, flow, currentEmotion):
    # Detect facial features
    face, eyes, mouth = findFacialFeatures(img)

    # Reshapes optical flow
    lines, vis = reshape(img, flow)

    # Calculate optical flow for tracked features
    opt_lines_eye1, opt_lines_eye2, opt_lines_mouth, opt_lines_mouth_up,\
        rectangle_mouth = draw_flow(vis, lines, eyes, mouth)

    # Draws eye/s rectangle
    drawFacialFeatureBounds(vis, face, eyes, mouth)

    # Calculates total motion
    outward, inward = count_lines(opt_lines_mouth_up, rectangle_mouth)

    # Calculates emotion
    emotion = calculate_emotion(outward, inward, currentEmotion)

    return vis, emotion, [outward, inward]

if __name__ == '__main__':
    cam = cv2.VideoCapture(0)
    ret, prev = cam.read()
    prevgray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)

    # Current emotion state sad:-1, neutral: 0, happy:1
    currentEmotion = 0

    while True:
        # Reads the webcam and converts it to grayscale for opticalflow
        # calculation
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Calculates the apparent motion between two frames
        # based on brightness
        flow = cv2.calcOpticalFlowFarneback(
            prevgray, gray, 0, 5, 3, 2, 3, 5, 1, 0)
        prevgray = gray

        # Calculates the emotion and motion
        showFrame, currentEmotion, num = emotion_recognition(
            gray, flow, currentEmotion)

        # Outputs the emotion based on the variable returned by
        # emotion_recognition to the current frame
        string = str(num)
        cv2.putText(showFrame, string, (10, 100), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (0, 0, 200), thickness=1, lineType=cv2.CV_AA)
        outputEmotion(currentEmotion)

        cv2.imshow('flow', showFrame)
        ch = 0xFF & cv2.waitKey(1)
        if ch == 27:
            break

    cv2.destroyAllWindows()
