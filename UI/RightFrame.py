from tkinter import *

from UI.Shared import Shared
from UI.consts import *
from PIL import Image
from Model.Account import *
from Database import DBPassMan
import time
class RightFrame(Frame):
    """
        __var_accountname
        __var_username
        __var_confirmPassword
        containerFrame()
        container_password_frame
        btnSave
        inputList
        labelList
    """

    def __init__(self,master,db=DBPassMan()):
        super().__init__(master,width=right_width,height=right_height,bg=right_background,highlightbackground="#000000",highlightcolor="#000000",highlightthickness=2)
        self.db = db
        self.__var_accountname = ""
        self.__var_username = ""
        self.__var_password = ""
        self.__var_confirmPassword = ""
        self.isEditable = True
        self.btnDelete = Button(self,text="Delete",font="nunito 14 bold",fg="#ffffff",bg=right_container_input_background)
        # self.btnDelete.place(x=510,y=50,width=70,height=40)
        self.btnEdit = Button(self,text="Edit",font="nunito 14 bold",fg="#ffffff",bg=right_container_input_background)
        # self.btnEdit.place(x=430,y=50,width=70,height=40)
        self.btnEdit.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor,command=self.toggleEditing)
        self.containerFrame()

    def toggleEditing(self):
        if self.isEditable:
            self.btnEdit.configure(bg=right_container_input_background)
            self.isEditable = False
            for x in self.inputList:
                x.configure(state=DISABLED)
        else:
            self.btnEdit.configure(bg=left_accentColor)
            self.isEditable = True
            for x in self.inputList:
                x.configure(state="normal")



    def containerFrame(self):
        container_password_frame = Frame(self, width=right_container_width, height=right_container_height,
                                         bg=right_container_background)
        container_password_frame.pack(anchor=CENTER, pady=106)
        container_password_frame.pack_propagate(0)

        lblAccountName = Label(container_password_frame, text="Account Name")
        lblAccountName.pack(side=TOP, anchor=NW, padx=right_container_label_padding, pady=right_container_label_padding)

        txtAccountName = Entry(container_password_frame, textvariable=self.__var_accountname)
        txtAccountName.pack(side=TOP, anchor=NW, padx=right_container_Entry_padding)

        lblUsername = Label(container_password_frame, text="Username")
        lblUsername.pack(side=TOP, anchor=NW, padx=right_container_label_padding, pady=right_container_label_padding)

        txtUsername = Entry(container_password_frame, textvariable=self.__var_username)
        txtUsername.pack(side=TOP, anchor=NW, padx=right_container_Entry_padding)

        lblPassword = Label(container_password_frame, text="Password")
        lblPassword.pack(side=TOP, anchor=NW, padx=right_container_label_padding, pady=right_container_label_padding)

        txtPassword = Entry(container_password_frame, textvariable=self.__var_password, show="*")
        txtPassword.pack(side=LEFT, anchor=NW, padx=right_container_Entry_padding)

        self.container_password_frame = container_password_frame

        self.imgShow = resizeImage(Image.open("UI/show.png"))
        self.imgHide = resizeImage(Image.open("UI/hide.png"))
        self.imgGenerate = resizeImage(Image.open("UI/generate.png"))

        self.isShowPassword = False
        btnShowHidePassword = Label(self.container_password_frame,image = self.imgShow,bg=right_container_input_background,width=35,height=30)
        btnShowHidePassword.pack(side=LEFT,anchor=NW,expand=0,padx=(10,0))
        btnShowHidePassword.propagate(0)

        btnShowHidePassword.bind("<Button-1>",self.__showHidePassword)

        btnGeneratePassword = Button(self.container_password_frame,image = self.imgGenerate,bg=right_container_input_background,width=35,height=30)
        btnGeneratePassword.pack(side=TOP,anchor=NW,expand=0,padx=(10,0))
        btnGeneratePassword.propagate(0)

        self.__addSaveButton()
        self.btnUpdate = None





        self.inputList = [txtAccountName, txtUsername, txtPassword]
        self.labelList = [lblAccountName, lblUsername, lblPassword]
        for x, y in zip(self.inputList, self.labelList):
            x.configure(bg=right_container_input_background, font=right_container_entry_font, fg="#ffffff",
                        relief=FLAT, highlightthickness=0)
            if id(x) != id(txtPassword):
                x.configure(width=37)
            else:
                x.configure(width=29)
            y.configure(font=right_container_label_font, fg="#ffffff", bg=right_container_background)

    def __addSaveButton(self):
        btnSave = Button(self.container_password_frame, text="Save", font=right_container_entry_font, fg="#ffffff",
                         bg=right_container_input_background, width=35, command=self.__save)

        btnSave.pack(side=TOP, anchor=NW,pady=right_container_label_padding,fill="x")
        self.btnSave = btnSave

    def __removeSaveButton(self):
        # self.btnSave.destroy()
        if self.btnSave != None:
            self.btnSave.pack_forget()

    def __addUpdateButton(self):
        btnUpdate = Button(self.container_password_frame, text="Update", font=right_container_entry_font, fg="#ffffff",
                         bg=right_container_input_background, width=35, command=self.__update)

        btnUpdate.pack(side=TOP, anchor=CENTER, pady=right_container_label_padding)
        self.btnUpdate = btnUpdate

    def __removeUpdateButton(self):
        if self.btnUpdate != None:
            self.btnUpdate.pack_forget()

    def refresh(self,account):
        self.__var_password = account.password
        self.__var_username = account.username
        self.__var_accountname = account.account_name

        self.btnDelete.place(x=510, y=50, width=70, height=40)
        self.btnEdit.place(x=430, y=50, width=70, height=40)

        # Show Account Name on Right Frame
        self.inputList[0].delete(0,END)
        self.inputList[0].insert(0,account.account_name)

        # Show Username on Right Frame
        self.inputList[1].delete(0,END)
        self.inputList[1].insert(0,account.username)

        # Show Password on Right Frame
        self.inputList[2].delete(0,END)
        self.inputList[2].insert(0,account.password)

        self.isEditable = True
        self.toggleEditing()
        print(self.isEditable)
        # for x in self.inputList:
        #     x.configure(state=DISABLED)


        # Remove Save Button of Right Frame
        self.btnSave.pack_forget()
        # self.__removeSaveButton()

        # Remove Update Button
        if self.btnUpdate != None:
            self.btnUpdate.pack_forget()
        # self.__removeUpdateButton()

        # Add Update Button
        self.__addUpdateButton()

    def __save(self):
        status = self.db.saveAccount((self.inputList[0].get(),self.inputList[1].get(),self.inputList[2].get()))
        accountList = self.db.getAllAccounts()
        Shared.getFrameMiddle().refresh(accountList)
        # print("Left:",id(Shared.getFrameLeft()))
        # print("Middle:", id(Shared.getFrameMiddle()))
        # print("Right:", id(Shared.getFrameRight()))

    def __update(self):
        print("Updating Values......")

    def __showHidePassword(self,event):
        # pass
        if self.isShowPassword:
            self.inputList[2].configure(show="*")
            # print(self.inputList[2]["image"])
            # TODO Change image of Show / Hide Password Button
            # self.inputList[2].configure(image=self.show)
            self.isShowPassword = False
        else:
            self.inputList[2].configure(show="")
            # self.inputList[2].configure(image=self.imgHide)
            self.isShowPassword = True













