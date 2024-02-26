import logging
import threading

import cv2
import numpy as np

import Detector
import Filters
import Tracker
import Writer

logging.basicConfig(
    filename='HISTORYlistener.log',
    level=logging.DEBUG,
    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


class Runner:
    cap = ''
    defaultFrame = None

    def __init__(self, cap):
        logging.debug('init runner')
        self.cap = cap

    def function(self, imageFLow, filter, detecor):
        logging.debug('init function')
        writer=Writer.Writer()
        ret, frame = imageFLow.read()
        self.defaultFrame = frame
        logging.debug('retina')

        retina = cv2.bioinspired.Retina.create((frame.shape[1], frame.shape[0]))
        logging.debug('retina started')
        while True:
            ret, frame = imageFLow.read()
            self.defaultFrame = frame

            logging.debug('filters')
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            filter.retinaFilter(frame, retina)
            filter.dynamicBackground(frame)
            filter.staticBackground(frame)
            logging.debug('filters end')
            logging.debug('tracker')

            if (self.tracker == None):
                logging.debug('tracker init')
                self.tracker = Tracker.Tracker(self.defaultFrame, detecor.coords)
            else:
                if (not (self.tracker.status)):
                    logging.debug('tracker changestatus')
                    self.tracker = Tracker.Tracker(self.defaultFrame, detecor.coords)
                else:
                    logging.debug('tracker update')
                    self.tracker.update_tracker(self.defaultFrame)
                    logging.debug('tracker update end')
            writer.write(self.tracker.bbox,self.tracker.imgBuf)

    frame = None
    bbox = None
    status = False
    coords = None
    tracker = None

    def run(self):

        _, self.defaultFrame = self.cap.read()

        filters = Filters.Filter(self.cap)
        detection = Detector.Detector()

        # filters.background(self.cap)
        t1 = threading.Thread(target=self.function, args=(self.cap, filters, detection))
        # print("data1")
        t1.start()

        while True:
            detection.multiplication(filters.maskStaticBackground, filters.maskDynamicBackground, filters.magno)
            detection.ifStaticImg(detection.Image)
            detection.findContours(filters.magno)
            # detection.findContours(detection.Image)
            detection.getRoi(self.defaultFrame)

            if (np.all(detection.Roi != None)):
                None
                # cv2.imshow("ROI_1", detection.Roi)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
