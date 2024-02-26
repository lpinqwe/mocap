import cv2


class Filter:
    defaultFrame = None
    backgroundImage = ''  # staticBackgroundImage
    buferDynamicBackground = ''
    maskDynamicBackground = ''  # image frame from dynamic background
    maskStaticBackground = ''
    magno = ''
    parvo = ''

    def __init__(self, imageFlow):
        ret, frame = imageFlow.read()
        self.defaultFrame = frame
        self.background(frame)

    def showOnce(self, image='', name='default'):
        while True:
            # time.sleep(0.1)
            # print(type(self.maskStaticBackground))
            cv2.imshow('magno', self.magno)
            cv2.imshow('parvo', self.parvo)
            cv2.imshow('backgroundImage', self.backgroundImage)
            cv2.imshow('maskStaticBackground', self.maskStaticBackground)
            cv2.imshow('maskDynamicBackground', self.maskDynamicBackground)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        return

    def background(self, frame):
        self.defaultFrame = frame
        # ret, frame = imageFlow.read()
        mask = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # a,mask=cv2.threshold(mask)

        self.backgroundImage = mask
        self.maskDynamicBackground = self.backgroundImage
        self.maskStaticBackground = self.backgroundImage
        self.magno = self.parvo = self.backgroundImage
        self.buferDynamicBackground = self.backgroundImage
        return mask

    def dynamicBackground(self, frame):
        # frameBuf = self.backgroundImage
        # while True:
        # print('here')
        # time.sleep(1 / delta)
        # ret, frame = imageFlow.read()
        self.maskDynamicBackground = cv2.absdiff(frame, self.buferDynamicBackground)  # то что нам нужно
        self.buferDynamicBackground = frame

    def staticBackground(self, frame):
        # ret, frame = imageFlow.read()
        self.maskStaticBackground = cv2.absdiff(frame, self.backgroundImage)

    def retinaFilter(self, frame, retina):
        # ret, image = imageFlow.read()

        # ret, frame = imageFlow.read()
        retina.run(frame)
        self.magno = retina.getMagno()
        self.parvo = retina.getParvo()
