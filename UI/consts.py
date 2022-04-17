from PIL import ImageTk
import random
import string

frame_left = None
frame_right = None
frame_middle = None

left_background = "#282828"
left_accentColor = "#165DDB"
left_regularTextColor = "#EFEFEF"
left_boldTextColor = "#FFFFFF"
left_width = 238
left_height = 768

middle_background = "#1E1E1E"
middle_boldTextColor = "#FFFFFF"
middle_regularTextColor = "#EEEEEE"
middle_accentColor = left_accentColor
middle_strokeColor = "#000000"
middle_searchBgBoxColor = "#404040"
middle_width = 446
middle_height = 768

right_width = 636
right_height = 768
right_background = "#1E1E1E"
right_container_background = "#292929"
right_container_width = 549
right_container_height = 566
right_container_label_font = "nunito 16 bold"
right_container_entry_font = "nunito 16"
right_container_label_padding = (30,5)
right_container_Entry_padding = (30,0)
right_container_input_background = "#3B3B3B"


def resizeImage(image):
    fixed_width = 20
    height_percent = (float(fixed_width) / float(image.size[0]))
    w_size = int((float(image.size[1]) * float(height_percent)))
    image = image.resize((fixed_width, w_size))
    image = ImageTk.PhotoImage(image)
    return image

def setLeftFame(value):
    frame_left = value

def setMiddleFrame(value):
    frame_middle = value

def setRightFrame(value):
    frame_right = value


def generatePassword():
    specialChars = """ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    lowerCaseAlphabates = string.ascii_lowercase
    upperCaseAlphabates = string.ascii_uppercase
    numbers = "0123456789"
