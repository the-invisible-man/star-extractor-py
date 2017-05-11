from recordtype import recordtype

FrameData = recordtype("FrameData", "triads totalStars", default=None)
Point = recordtype("Point", "x y", default=None)


class StarTriad(object):

    def __init__(self):
        self.a = Point()
        self.b = Point()
        self.c = Point()