from tkinter import *

from UI.MiddleFrame import MiddleFrame
from UI.LeftFrame import LeftFrame
from UI.RightFrame import RightFrame
import UI.consts as consts
from Database import *
from UI.Shared import Shared


class MainUI():
    def __init__(self,db):
        self.db = db
        self.tk = Tk()
        self.tk.geometry("1300x700")
        # tk.configure(background="#FFFFFF")
        Shared.setDB(self.db)

        self.frame_left = LeftFrame(self.tk)
        self.frame_left.pack(side=LEFT,anchor=NW,expand=Y)
        self.frame_left.pack_propagate(0)
        # consts.frame_left = self.frame_left
        consts.setLeftFame(self.frame_left)

        accountlist = db.getAllAccounts()
        self.frame_middle = MiddleFrame(self.tk,accountlist)
        self.frame_middle.pack(side=LEFT,anchor=W,expand=Y)
        self.frame_middle.pack_propagate(0)
        # consts.frame_middle = self.frame_middle
        consts.setMiddleFrame(self.frame_middle)

        self.frame_right = RightFrame(self.tk,self.db,False)
        self.frame_right.pack(side=LEFT,anchor=W,expand=Y)
        self.frame_right.pack_propagate(0)
        # consts.frame_right = self.frame_right
        consts.setRightFrame(self.frame_right)

        print("Main Left:",id(self.frame_left))
        print("Main Middle:", id(self.frame_middle))
        print("Main Right:", id(self.frame_right))

        Shared.setFrameLeft(self.frame_left)
        Shared.setFrameRight(self.frame_right)
        Shared.setFrameMiddle(self.frame_middle)


        self.tk.mainloop()
