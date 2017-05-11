from Structs import *
import typing


class Math(object):

    def dot(self, a, b):
        """

        :type a: Point
        :type b: Point
        :return int:
        """
        return a.x * b.x + a.y * b.y

    def lengthcross(self, a, b):
        """

        :type a: Point
        :type b: Point
        :type:
        """
        return abs(a.x*b.x - a.y*b.x)

