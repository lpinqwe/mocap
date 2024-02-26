import time

import cv2
import numpy as np
class Detector:
    coords = None
    Roi = None
    State = None
    Image = None
    ifStatic = None  # if image is static ifStatic=False, if movement ifStatic=True

    def getRoi(self, frame):
        if (self.ifStatic == True):
            # _, frame = imageFlow.read()
            x, y, w, h = self.coords
            self.Roi = frame[y:y + h, x:x + w]
            # cv2.imshow("ROI",self.Roi)
            # cv2.imshow("frame", frame)
        else:
            print("not ROI")
            self.Roi = None

    def ifStaticImg(self, img):
        if np.any(img != None):
            if (cv2.countNonZero(img) > 10):
                self.ifStatic = True
            else:
                self.ifStatic = False

    def findContours(self, image):
        if (self.ifStatic == True and np.any(image != None)):

            image = cv2.threshold(image, 50, 255, cv2.THRESH_BINARY)[1]
            buf = image
            contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for contour in contours:
                # Вычисляем ограничивающий прямоугольник для контура
                self.coords = x, y, w, h = cv2.boundingRect(contour)
                # self.coords = cv2.boundingRect(contour)
                # print(f"coords = {self.coords}")
                # Рисуем квадрат вокруг контура
                frame = cv2.cvtColor(buf, cv2.COLOR_GRAY2BGR)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.imshow("box", frame)
                # cv2.waitKey(0)

        return

    def multiplication(self, a, b, c):
        b = cv2.resize(b, (200, 200))
        c = cv2.resize(c, (200, 200))
        QBUF = cv2.hconcat([c, b])

        c = cv2.threshold(c, 50, 255, cv2.THRESH_BINARY)[1]
        b = cv2.threshold(b, 50, 255, cv2.THRESH_BINARY)[1]
        self.Image = cv2.multiply(c, b)
        QBUF2 = cv2.hconcat([c, b])
        ABUF = cv2.vconcat([QBUF, QBUF2])
        FBUF = cv2.vconcat([ABUF, cv2.resize(self.Image, (400, 400))])
        # ABUF=cv2.vconcat(QBUF, QBUF2)
        # ABUF = cv2.vconcat([QBUF, self.Image])
        cv2.imshow("name00", FBUF)