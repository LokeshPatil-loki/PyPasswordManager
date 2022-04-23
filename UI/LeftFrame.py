from tkinter import *

import UI.LoginUI
import UI.RightFrame
from UI.Shared import Shared
from UI.consts import *
import UI.MiddleFrame
class LeftFrame(Frame):

    def __init__(self,master):
        super().__init__(master,width=left_width,height=left_height,bg=left_background)
        lblMenu = Label(self,text="Menu",font="nunito 30 bold",bg=left_background,fg=left_boldTextColor)
        lblMenu.pack(side=TOP,anchor=CENTER,padx=10,pady=10)

        btnPassword = Button(self,command=self.switchToPasswords,text="Password",font="nunito 21",bg=left_background,fg=left_boldTextColor,width=left_width,relief=FLAT,highlightthickness=0)
        btnPassword.pack(side=TOP,anchor=CENTER,pady=10)
        btnPassword.configure(activebackground=left_accentColor,activeforeground=left_boldTextColor)

        btnNotes = Button(self, text="Notes",command=self.switchToNotes, font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        btnNotes.pack(side=TOP, anchor=CENTER, pady=10)
        btnNotes.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        btnImport = Button(self, text="Import", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        # btnImport.pack(side=TOP, anchor=CENTER, pady=10)
        btnImport.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        btnExport = Button(self, text="Export", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        # btnExport.pack(side=TOP, anchor=CENTER, pady=10)
        btnExport.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        btnLogout = Button(self,command=self.logout,text="Logout", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        btnLogout.pack(side=TOP, anchor=CENTER, pady=10)
        btnLogout.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        self.buttons = [btnPassword,btnNotes,btnImport,btnExport,btnLogout]

    def logout(self):
        self.master.destroy()
        UI.LoginUI.LoginUI(Shared.getDB())

    def switchToNotes(self,):
        self.buttons[0].configure(bg=left_background)
        self.buttons[1].configure(bg=left_accentColor)
        Shared.getFrameMiddle().destroy()
        frame_middle = UI.MiddleFrame.MiddleFrame(self.master,Shared.getDB().getAllNotes(),False)
        Shared.setFrameMiddle(frame_middle)
        frame_middle.pack(side=LEFT,anchor=W,expand=Y)
        frame_middle.pack_propagate(0)

        Shared.getFrameRight().destroy()
        frame_right = UI.RightFrame.RightFrame(self.master,Shared.getDB(),False)
        Shared.setFrameRight(frame_right)
        frame_right.pack(side=LEFT,anchor=W,expand=Y)
        frame_right.pack_propagate(0)

    def switchToPasswords(self):
        self.buttons[1].configure(bg=left_background)
        self.buttons[0].configure(bg=left_accentColor)
        Shared.getFrameMiddle().destroy()
        frame_middle = UI.MiddleFrame.MiddleFrame(self.master,Shared.getDB().getAllAccounts(),True)
        Shared.setFrameMiddle(frame_middle)
        frame_middle.pack(side=LEFT,anchor=W,expand=Y)
        frame_middle.pack_propagate(0)

        Shared.getFrameRight().destroy()
        frame_right = UI.RightFrame.RightFrame(self.master,Shared.getDB(),True)
        Shared.setFrameRight(frame_right)
        frame_right.pack(side=LEFT,anchor=W,expand=Y)
        frame_right.pack_propagate(0)



