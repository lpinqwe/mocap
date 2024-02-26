import logging
import time

import cv2


class Tracker:

    tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
    imgBuf=None
    my_tracker=None
    reserve_bbox=None
    status=False
    bbox=None
    #recommend: KCF,MEDIANFLOW,MOSSE
    def __init__(self,frame,bbox,tracker="MOSSE",):
        self.imgBuf = frame
        print(time.time())
        self.my_tracker=self.create_tracker_by_name(tracker)
        self.my_tracker.init(frame, bbox)
        self.status=True
        print(time.time())
    def update_tracker(self,frame):
        self.imgBuf=frame.copy()
        logging.debug('tracker.update_tracker')
        status, bbox = self.my_tracker.update(frame)

        logging.debug('tracker.update_tracker updated')
        self.status=status
        self.bbox=bbox
        if self.status:
            bbox = tuple(map(int, bbox))
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)
        else:
            cv2.putText(self.imgBuf, "err", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        logging.debug('tracker.update_tracker draw fin')
        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return
        logging.debug('tracker.update_tracker END')
    def create_tracker_by_name(self, tracker_type):

        if tracker_type == self.tracker_types[0]:
            tracker = cv2.legacy.TrackerBoosting.create()
        elif tracker_type == self.tracker_types[1]:
            tracker = cv2.legacy.TrackerMIL.create()
        elif tracker_type == self.tracker_types[2]:
            tracker = cv2.legacy.TrackerKCF.create()
        elif tracker_type == self.tracker_types[3]:
            tracker = cv2.legacy.TrackerTLD.create()
        elif tracker_type == self.tracker_types[4]:
            tracker = cv2.legacy.TrackerMedianFlow.create()
        elif tracker_type == self.tracker_types[5]:
            tracker = cv2.legacy.TrackerMOSSE.create()
        elif tracker_type == self.tracker_types[6]:
            tracker = cv2.legacy.TrackerCSRT.create()
        else:
            tracker = None
            print('[ERROR] Invalid selection! Available tracker: ')
            for t in self.tracker_types:
                print(t.lower())
        print(tracker)
        return tracker