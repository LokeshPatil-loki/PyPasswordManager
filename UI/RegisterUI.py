import tkinter
from tkinter import *
from tkinter import messagebox

import PIL

import UI.LoginUI
from UI.Shared import Shared
from UI.consts import resizeImage, right_container_input_background


class RegisterUI:
    def __init__(self,db):
        self.db = db
        self.tk = Tk()
        self.tk.geometry("979x650")
        self.isShowPassword = False
        self.addTitleFrame()
        self.addMainFrame()
        Shared.setRegisterUI(self)
        self.tk.mainloop()


    def addTitleFrame(self):
        self.titleFrame = Frame(self.tk,width=396,height=650,bg="#404040")
        self.titleFrame.pack(side=LEFT,anchor=NW)
        self.titleFrame.pack_propagate(0)
        lblTitle = Label(self.titleFrame,text="Register",font="nunito 70",width=50,height=50,bg="#404040",justify=CENTER,fg="#ffffff")
        lblTitle.pack(side=TOP)
        lblTitle.pack_propagate(0)

    def addMainFrame(self):
        self.mainFrame = Frame(self.tk, width=583, height=650, bg="#282828")
        self.mainFrame.pack(side=LEFT, anchor=NW)
        self.mainFrame.pack_propagate(0)
        # self.mainFrame.grid_rowconfigure(1,weight=1)
        # self.mainFrame.grid_columnconfigure(1,weight=1)
        self.addContainerFrame()

    def addContainerFrame(self):
        font1 = "nunito 20"
        font2 = "nunito 20 bold"
        bg = "#3B3B3B"
        self.containerFrame = Frame(self.mainFrame,width=501,height=570,bg="#404040")
        self.containerFrame.pack(side=LEFT,anchor=CENTER,padx=40)
        self.containerFrame.pack_propagate(0)

        self.lblName = Label(self.containerFrame, text="Full Name",font=font2,bg="#404040",fg="#ffffff")
        self.lblName.pack(side=TOP, anchor=NW, padx=38,pady=(48-10,0))

        self.txtName = Entry(self.containerFrame,fg="#ffffff",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtName.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.lblUsername = Label(self.containerFrame, text="Username",font=font2,bg="#404040",fg="#ffffff")
        self.lblUsername.pack(side=TOP, anchor=NW, padx=38,pady=(48-10,0))

        self.txtUsername = Entry(self.containerFrame,fg="#ffffff",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtUsername.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.lblPassword = Label(self.containerFrame, text="Password",font=font2,bg="#404040",fg="#ffffff")
        self.lblPassword.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

        self.txtPassword = Entry(self.containerFrame,show="*",fg="#ffffff",font=font1,width=23,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.txtPassword.pack(side=TOP, anchor=NW, padx=38,pady=(4,0))

        self.imgShow = resizeImage(PIL.Image.open("UI/show.png"))
        self.btnShowHidePassword = Label(self.containerFrame,image = self.imgShow,bg=right_container_input_background,width=39,height=39,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnShowHidePassword.place(x=420,y=325)
        self.btnShowHidePassword.bind("<Button-1>", self.__showHidePassword)

        self.btnSave = Button(self.containerFrame,command=self.__register,fg="#ffffff",text="Register",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnSave.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

        self.btnGoToLogin = Button(self.containerFrame,command=self.goToLogin,fg="#ffffff",text="Already have an account",font=font1,width=426,bg=bg,highlightthickness=1,relief=FLAT,highlightbackground="#5C5C5C",highlightcolor="#5C5C5C")
        self.btnGoToLogin.pack(side=TOP, anchor=NW, padx=38,pady=(28,0))

    def __register(self):
        name = self.txtName.get()
        username = self.txtUsername.get()
        password = self.txtPassword.get()
        if not name.strip():
            tkinter.messagebox.showerror("Validation Error", "Please Enter you Full Name")
            return False
        elif not username.strip():
            tkinter.messagebox.showerror("Validation Error", "Please Enter username")
            return False
        elif not password.strip():
            tkinter.messagebox.showerror("Validation Error", "Please Enter password")
            return False
        else:
            success = self.db.register(name,username,password)
            if success:
                tkinter.messagebox.showinfo(title="Success",message=f"{name} is registered with username {username}")
            else:
                tkinter.messagebox.showerror(title="Registration Error",message="Username already exists, Try different username")
        # self.containerFrame.grid(row=1,column=1)
    def mainloop(self):
        self.tk.mainloop()

    def goToLogin(self):
        self.tk.destroy()
        UI.LoginUI.LoginUI(self.db)

    def __showHidePassword(self,event):
        # pass
        if self.isShowPassword:
            self.txtPassword.configure(show="*")
            # print(self.inputList[2]["image"])
            # TODO Change image of Show / Hide Password Button
            # self.inputList[2].configure(image=self.show)
            self.isShowPassword = False
        else:
            self.txtPassword.configure(show="")
            # self.inputList[2].configure(image=self.imgHide)
            self.isShowPassword = True
