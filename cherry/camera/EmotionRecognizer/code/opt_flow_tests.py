import cv2
import numpy
import unittest

from opt_flow import findFacialFeatures, count_lines, calculate_emotion


def loadImages():
    return [cv2.imread("test_files/face1.png"),
            cv2.imread("test_files/face2.jpeg"),
            cv2.imread("test_files/face3.jpeg")]


class TestEmotionRecognition(unittest.TestCase):

    def test_find_facial_features(self):
        images = loadImages()

        # ground truth information
        face_coords = [[158, 48, 346, 346],
                       [380, 91, 428, 428],
                       [344, 191, 410, 410]]
        eye_coords = [[[230, 144, 74, 74], [358, 144, 67, 67]],
                      [[453, 213, 90, 90], [616, 208, 91, 91]],
                      [[438, 310, 83, 83], [565, 306, 90, 90]]]
        mouth_coords = [(497, 328, 84, 26),
                        (510, 405, 158, 71),
                        (468, 502, 163, 74)]

        index = 0
        for image in images:
            face, eyes, mouth = findFacialFeatures(image)
            assert(numpy.array_equal(face, face_coords[index]))
            assert(numpy.array_equal(eyes[0], eye_coords[index][0]))
            assert(numpy.array_equal(eyes[1], eye_coords[index][1]))
            assert(numpy.array_equal(mouth, mouth_coords[index]))
            index += 1

    def test_count_lines(self):
        sample_mouth = [500, 400, 650, 450]
        sample_lines = [[(500, 445), (505, 430)],
                        [(600, 425), (610, 400)]]
        outward, inward = count_lines(sample_lines, sample_mouth)
        assert(inward == 1 and outward == 1)

    def test_calculate_emotion(self):
        emotion1 = calculate_emotion(1, 1, 0)
        assert(emotion1 == 0)
        emotion2 = calculate_emotion(10, 5, 0)
        assert(emotion2 == 1)
        emotion3 = calculate_emotion(5, 10, 0)
        assert(emotion3 == -1)
        emotion4 = calculate_emotion(10, 5, -1)
        assert(emotion4 == 0)

if __name__ == '__main__':
    unittest.main()
