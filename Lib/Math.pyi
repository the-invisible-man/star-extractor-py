from Structs import *
import typing

class Math(object):

    def dot(self, a: FrameData, b: FrameData) -> int:
        """

        :param a:
        :param b:
        :return int:
        """
        return (a.x * b.x + a.y * b.y)