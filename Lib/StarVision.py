import numpy
import cv2
import itertools
import json
from Structs import FrameData, StarTriad


class StarVision(object):

    def __init__(self):
        self.fileLocation = ''
        self.max_combinations = 100
        self.config = ''

    def load_file(self, file_location):
        self.fileLocation = file_location

    def find_stars(self):
        im = cv2.imread(self.fileLocation, cv2.IMREAD_GRAYSCALE)
        (thresh, im_binary) = cv2.threshold(im, 100, 255, cv2.THRESH_BINARY)
        params = cv2.SimpleBlobDetector_Params()

        params.filterByArea = True
        params.minArea = 0.01
        params.maxArea = 1000
        params.filterByColor = True
        params.blobColor = 255

        detector = cv2.SimpleBlobDetector_create(params)

        return detector.detect(im_binary)

    def capture(self):
        stars = self.find_stars()
        output = FrameData()

        output.totalStars = len(stars)
        output.triads = self.build_triads(stars)
        return output

    def build_triads(self, keypoints):
        total_keypoints = len(keypoints)
        total_combinations = total_keypoints if total_keypoints < self.max_combinations else self.max_combinations
        keys = range(0, total_combinations)
        out = []

        for combo in list(itertools.combinations(keys, 3)):
            star_triad = StarTriad()
            star_triad.a.x = keypoints[combo[0]].pt[1]
            star_triad.a.y = keypoints[combo[0]].pt[0]

            star_triad.b.x = keypoints[combo[1]].pt[1]
            star_triad.b.y = keypoints[combo[1]].pt[0]

            star_triad.c.x = keypoints[combo[2]].pt[1]
            star_triad.c.y = keypoints[combo[2]].pt[0]

            out.append(star_triad)

        return out
