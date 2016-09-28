#!/usr/bin/env python2

"""
Face detection helper using OpenCV and it's Python bindings.

Adpated from https://github.com/shantnu/FaceDetect/
"""

import numpy
import cv2
import sys
import glob
import time
import os.path as pth


def get_face_detect():
    """Return a function that finds faces."""
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def detect(image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return classifier.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(29, 29),
            flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
    return detect


def get_face_recog(detector, fnlist):
    """Return a function that recognizes faces using the filesname given."""
    print("Training Eigenfaces recognizer")
    images, labels = [], []
    label_names = dict()
    max_w, max_h = 0, 0

    for fn in fnlist:
        raw = cv2.imread(fn)
        faces = detector(raw)
        for (x, y, w, h) in faces:
            image = cv2.cvtColor(raw[y: y + h, x: x + w], cv2.COLOR_BGR2GRAY)
            images.append(image)

            label_name = pth.split(fn)[-1]
            label = label_names.get(label_name, -1)
            if label < 0:
                label = len(images)
                label_names[label] = pth.split(fn)[-1]
            labels.append(label)

            w, h = image.shape
            max_w = max(max_w, w)
            max_h = max(max_h, h)

    # Images must all be the same size for training
    for idx, img in enumerate(images):
        images[idx] = cv2.resize(img, (max_w, max_h))

    detector = cv2.createEigenFaceRecognizer()
    detector.train(images, numpy.array(labels))

    def recog(found):
        scaled = cv2.resize(found, (max_w, max_h))
        bw = cv2.cvtColor(scaled, cv2.COLOR_BGR2GRAY)
        label, conf = detector.predict(bw)
        return label, conf, label_names.get(label, "")

    return recog


def camera_detect(fnlist):
    """Detect faces from the webcam."""
    detector = get_face_detect()
    recognizer = get_face_recog(detector, fnlist)

    print("Grabbing web cam")
    vid_cap = cv2.VideoCapture(0)
    try:
        while True:
            ret, frame = vid_cap.read()
            if not ret:
                print("Oops")
                time.sleep(2)
                continue

            faces = detector(frame)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                lab, conf, lab_name = recognizer(frame[y: y + h, x: x + w])
                print("Detection: %d(%s) at %.4f" % (lab, lab_name, conf))

            cv2.imshow("Current Frame", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(1)
    finally:
        vid_cap.release()


def file_check(fnlist, display):
    """For given list of files, check for faces and optionally display."""
    print("Processing %d files" % len(fnlist))
    if display:
        print("Will display images")

    classifier = get_face_detect()

    for fn in sorted(fnlist):
        image = cv2.imread(fn)
        faces = classifier(image)
        print("%s => Found %d faces" % (fn, len(faces)))

        if display:
            for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow("Faces found", image)
            cv2.waitKey(0)


def main():
    """Entry point - check each arg for faces and show."""
    fnlist = set()
    display = False
    do_capture = False

    for a in sys.argv[1:]:
        if a == "--display":
            display = True
        elif a == "--capture":
            do_capture = True
        else:
            fnlist.update(glob.glob(a))

    if do_capture:
        camera_detect(fnlist)
    else:
        file_check(fnlist, display)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
