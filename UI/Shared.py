class Shared:
    __frame_left = None
    __frame_right = None
    __frame_middle = None

    @classmethod
    def setFrameLeft(cls,value):
        Shared.__frame_left = value

    @classmethod
    def setFrameMiddle(cls,value):
        Shared.__frame_middle = value

    @classmethod
    def setFrameRight(cls,value):
        Shared.__frame_right = value

    @classmethod
    def getFrameLeft(cls):
        return Shared.__frame_left

    @classmethod
    def getFrameMiddle(cls):
        return Shared.__frame_middle

    @classmethod
    def getFrameRight(cls):
        return Shared.__frame_right