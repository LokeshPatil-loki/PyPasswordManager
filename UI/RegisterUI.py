import tkinter
from tkinter import *

import UI.LoginUI
from UI.Shared import Shared


class RegisterUI:
    def __init__(self,db):
        self.db = db
        self.tk = Tk()
        self.tk.geometry("979x578")
        self.addTitleFrame()
        self.addMainFrame()
        Shared.setRegisterUI(self)
        self.tk.mainloop()


    def addTitleFrame(self):
        self.titleFrame = Frame(self.tk,width=396,height=578,bg="#404040")
        self.titleFrame.pack(side=LEFT,anchor=NW)
        self.titleFrame.pack_propagate(0)
        lblTitle = Label(self.titleFrame,text="Register",font="nunito 70",width=50,height=50,bg="#404040",justify=CENTER,fg="#ffffff")
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

        self.txtUsername = Entry(self.containerFrame,font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtUsername.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.lblPassword = Label(self.containerFrame, text="Password",font=font2,bg="#404040",fg="#ffffff")
        self.lblPassword.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

        self.txtPassword = Entry(self.containerFrame,font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtPassword.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.btnSave = Button(self.containerFrame,command=self.__register,fg="#ffffff",text="Register",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnSave.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

        self.btnGoToLogin = Button(self.containerFrame,command=self.goToLogin,fg="#ffffff",text="Already have an account",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnGoToLogin.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

    def __register(self):
        loggedInUser = self.db.register(self.txtUsername.get(),self.txtPassword.get())
        if loggedInUser:
            self.tk.destroy()
            UI.MainUI.MainUI(self.db)
        else:
            tkinter.messagebox.showerror(title="Registration Error",message="Username alrady exists, Try different username")
        # self.containerFrame.grid(row=1,column=1)
    def mainloop(self):
        self.tk.mainloop()

    def goToLogin(self):
        self.tk.destroy()
        UI.LoginUI.LoginUI(self.db)
