from Lib.StarVision import StarVision

star_vision = StarVision()
star_vision.load_file("/Users/cgranados/Code/startracker/media/summertriangle.jpg")
data = star_vision.capture()
counter = 1

for triad in data.triads:

    print "Triad " + str(counter) + "\n"

    print "a = (" + str(triad.a.x) + ", " + str(triad.a.y) + ")"
    print "b = (" + str(triad.b.x) + ", " + str(triad.b.y) + ")"
    print "c = (" + str(triad.c.x) + ", " + str(triad.c.y) + ")\n"

    counter += 1

print "Found " + str(len(data.triads)) + " triads in current view\n"
print "Identified " + str(data.totalStars) + " stars in this frame\n"
