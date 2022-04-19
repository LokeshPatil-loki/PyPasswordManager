import tkinter.messagebox
from tkinter import *

import UI.RegisterUI
from UI.RegisterUI import RegisterUI
from UI.Shared import Shared


class LoginUI:
    def __init__(self,db):
        self.db = db
        self.tk = Tk()
        self.tk.geometry("979x578")
        self.addTitleFrame()
        self.addMainFrame()
        Shared.setLoginUI(self)
        self.tk.mainloop()

    def addTitleFrame(self):
        self.titleFrame = Frame(self.tk,width=396,height=578,bg="#404040")
        self.titleFrame.pack(side=LEFT,anchor=NW)
        self.titleFrame.pack_propagate(0)
        lblTitle = Label(self.titleFrame,text="Login",font="nunito 70",width=50,height=50,bg="#404040",justify=CENTER,fg="#ffffff")
        lblTitle.pack(side=TOP)
        lblTitle.pack_propagate(0)

    def addMainFrame(self):
        self.mainFrame = Frame(self.tk, width=583, height=578, bg="#282828")
        self.mainFrame.pack(side=LEFT, anchor=NW)
        self.mainFrame.pack_propagate(0)
        # self.mainFrame.grid_rowconfigure(1,weight=1)
        # self.mainFrame.grid_columnconfigure(1,weight=1)
        self.addContainerFrame()

    def addContainerFrame(self):
        font1 = "nunito 20"
        font2 = "nunito 20 bold"
        bg = "#3B3B3B"
        self.containerFrame = Frame(self.mainFrame,width=501,height=474,bg="#404040")
        self.containerFrame.pack(side=LEFT,anchor=CENTER,padx=40)
        self.containerFrame.pack_propagate(0)

        self.lblUsername = Label(self.containerFrame, text="Username",font=font2,bg="#404040",fg="#ffffff")
        self.lblUsername.pack(side=TOP, anchor=NW, padx=38,pady=(48,0))

        self.txtUsername = Entry(self.containerFrame,fg="#ffffff",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtUsername.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.lblPassword = Label(self.containerFrame, text="Password",font=font2,bg="#404040",fg="#ffffff")
        self.lblPassword.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

        self.txtPassword = Entry(self.containerFrame,fg="#ffffff",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtPassword.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.btnLogin = Button(self.containerFrame,command=self.__login,fg="#ffffff",text="Login",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnLogin.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

        self.btnGoToRegister = Button(self.containerFrame,command=self.goToRegister,fg="#ffffff",text="Don't have an account",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnGoToRegister.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

    def mainloop(self):
        self.tk.mainloop()

    def __login(self):
        loggedInUser = self.db.login(self.txtUsername.get(),self.txtPassword.get())
        if loggedInUser:
            self.tk.destroy()
            UI.MainUI.MainUI(self.db)
        else:
            tkinter.messagebox.showerror(title="Login Error",message="Invalid Username / Password")

    def goToRegister(self):
        self.tk.destroy()
        UI.RegisterUI.RegisterUI(self.db)



