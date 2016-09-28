#!/usr/bin/env python2

"""
Face detection helper using OpenCV and it's Python bindings.

Adpated from https://github.com/shantnu/FaceDetect/
"""


import cv2
import sys
import glob


def main():
    """Entry point - check each arg for faces and show."""
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    fnlist = set()
    display = False
    for a in sys.argv[1:]:
        if a == "--display":
            display = True
        else:
            fnlist.update(glob.glob(a))

    print("Processing %d files" % len(fnlist))
    if display:
        print("Will display images")

    for fn in sorted(fnlist):
        image = cv2.imread(fn)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = classifier.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(29, 29),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        print("%s => Found %d faces" % (fn, len(faces)))

        if display:
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("Faces found", image)
            cv2.waitKey(0)


if __name__ == "__main__":
    main()
