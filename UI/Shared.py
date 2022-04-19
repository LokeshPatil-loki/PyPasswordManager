import string
import random

class Shared:
    __frame_left = None
    __frame_right = None
    __frame_middle = None
    __db = None

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
    def setDB(cls,value):
        Shared.__db = value

    @classmethod
    def getFrameLeft(cls):
        return Shared.__frame_left

    @classmethod
    def getFrameMiddle(cls):
        return Shared.__frame_middle

    @classmethod
    def getFrameRight(cls):
        return Shared.__frame_right

    @classmethod
    def getDB(cls):
        return Shared.__db

    @classmethod
    def generatePassword(cls):
        specialChars = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        upperCaseLetter = string.ascii_uppercase
        lowerCaseLetters = string.ascii_lowercase
        numbers = "0123456789"
        charset = [specialChars, upperCaseLetter, numbers, lowerCaseLetters]
        password = ""
        for x in range(0, 28):
            index = random.randint(0, 3)
            selectedSet = charset[index]
            index = random.randint(0, 3)
            password += selectedSet[index]
        return password
