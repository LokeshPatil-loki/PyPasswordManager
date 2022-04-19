from tkinter import *
# from UI.MiddleFrame import MiddleFrame
# from UI.LeftFrame import LeftFrame
# from UI.RightFrame import RightFrame
from UI.LoginUI import LoginUI
from UI.MainUI import *
from Database import *
import random
db = DBPassMan()
# LoginUI(db)

loggedInUser = db.login("loki","loki")
if loggedInUser:
    MainUI(db)
#     print(loggedInUser.username)
#     tk = Tk()
#     tk.geometry("1300x700")
#     # tk.configure(background="#FFFFFF")
#
#     frame_left = LeftFrame(tk)
#     frame_left.pack(side=LEFT,anchor=NW,expand=Y)
#     frame_left.pack_propagate(0)
#
#     frame_middle = MiddleFrame(tk,db)
#     frame_middle.pack(side=LEFT,anchor=W,expand=Y)
#     frame_middle.pack_propagate(0)
#
#     frame_right = RightFrame(tk,db)
#     frame_right.pack(side=LEFT,anchor=W,expand=Y)
#     frame_right.pack_propagate(0)
#
#
#     tk.mainloop()

