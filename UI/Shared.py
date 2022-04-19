import string
import random

class Shared:
    __frame_left = None
    __frame_right = None
    __frame_middle = None
    __db = None
    __loginUI = None
    __RegisterUI = None


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
    def setLoginUI(cls,value):
        Shared.__loginUI = value

    @classmethod
    def setRegisterUI(cls,value):
        Shared.__RegisterUI = value

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
    def getLoginUI(cls):
        return Shared.__loginUI

    @classmethod
    def getRegisterUI(cls):
        return Shared.__RegisterUI

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
