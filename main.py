import cv2
import DroneFilters
import threading
'''
class Handler:
    def apply(self):
        pass
    pass
    
class PrintHandler(Handler):
    pass

class DBWriteHandler(Handler):
    pass

class Config:
    def add_handler(self, handler:Handler):
        pass

class DroneFilters1:
    def run:
        while True:
            if (detect=True):
                for(h in handlers):
                    h.apply()
'''

if __name__ == '__main__':
    #cap = cv2.VideoCapture(r"C:\Users\vwork\PycharmProjects\droneDetector_V1\dataset_1XD (online-video-cutter.com).mp4")
    cap = cv2.VideoCapture(0)
    runner = DroneFilters.Runner(cap)
    #runner.config.addhandler(PrintHandler())
    #runner.config.addhandler(DBWriteHandler())
    runner.run()
    while True:
        print(runner.tracker.cooords)