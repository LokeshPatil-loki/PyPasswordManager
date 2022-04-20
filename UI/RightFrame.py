import tkinter.messagebox
from tkinter import *

from UI.Shared import Shared
from UI.consts import *
from PIL import Image
from Model.Account import *
from Database import DBPassMan
class RightFrame(Frame):
    """
        __var_accountname
        __var_username
        __var_confirmPassword
        containerPasswordFrame()
        container_password_frame
        btnSave
        inputList
        labelList
    """

    def __init__(self,master,db=DBPassMan(),isPasswordMode=True):
        super().__init__(master,width=right_width,height=right_height,bg=right_background,highlightbackground="#000000",highlightcolor="#000000",highlightthickness=2)
        self.isPasswordMode = isPasswordMode
        self.UPDATE_MODE = 1
        self.SAVE_MODE = 0
        self.ACCOUNT_NAME_INDEX = 0
        self.USERNAME_INDEX = 1
        self.Password_INDEX = 2
        self.db = db
        self.__var_accountname = ""
        self.__var_username = ""
        self.__var_password = ""
        self.__var_confirmPassword = ""
        self.isEditable = True
        self.btnDelete = Button(self,text="Delete",font="nunito 14 bold",fg="#ffffff",bg=right_container_input_background,command=self.__delete)
        # self.btnDelete.place(x=510,y=50,width=70,height=40)
        self.btnEdit = Button(self,text="Edit",font="nunito 14 bold",fg="#ffffff",bg=right_container_input_background)
        # self.btnEdit.place(x=430,y=50,width=70,height=40)
        self.btnEdit.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor,command=self.toggleEditing)
        if self.isPasswordMode:
            self.containerPasswordFrame()
        else:
            self.containerNotesFrame()

    def toggleEditing(self,updateMode=True):
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
            if updateMode:
                self.inputList[0].configure(state=DISABLED)

    def containerPasswordFrame(self):
        container_password_frame = Frame(self, width=right_container_width, height=right_container_height,
                                         bg=right_container_background)
        self.container_password_frame = container_password_frame
        container_password_frame.pack(anchor=CENTER, pady=106)
        container_password_frame.pack_propagate(0)
        # self.showContainerFrame()

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



        self.imgShow = resizeImage(Image.open("UI/show.png"))
        self.imgHide = resizeImage(Image.open("UI/hide.png"))
        self.imgGenerate = resizeImage(Image.open("UI/generate.png"))

        self.isShowPassword = False
        btnShowHidePassword = Label(self.container_password_frame,image = self.imgShow,bg=right_container_input_background,width=35,height=30)
        btnShowHidePassword.pack(side=LEFT,anchor=NW,expand=0,padx=(10,0))
        btnShowHidePassword.propagate(0)

        btnShowHidePassword.bind("<Button-1>",self.__showHidePassword)

        btnGeneratePassword = Button(self.container_password_frame,image = self.imgGenerate,bg=right_container_input_background,width=35,height=30,command=self.generatePassword)
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
        self.isEditable = True
        self.toggleEditing()

    def containerNotesFrame(self):
        containerNotesFrame = Frame(self, width=right_container_width, height=right_container_height,
              bg=right_container_background)
        self.container_password_frame = containerNotesFrame
        containerNotesFrame.pack(anchor=CENTER, pady=106)
        containerNotesFrame.pack_propagate(0)

        lblTitle = Label(containerNotesFrame, text="Title")
        lblTitle.configure(font=right_container_label_font, fg="#ffffff", bg=right_container_background)
        lblTitle.pack(side=TOP, anchor=NW, padx=right_container_label_padding, pady=right_container_label_padding)

        txtTitle = Entry(containerNotesFrame)
        txtTitle.configure(bg=right_container_input_background, font=right_container_entry_font, fg="#ffffff",
                        relief=FLAT, highlightthickness=0,width=37)
        txtTitle.pack(side=TOP, anchor=NW, padx=right_container_Entry_padding)

        txtNote = Text(containerNotesFrame,bg=right_container_input_background, font=right_container_entry_font, fg="#ffffff",
                        relief=FLAT, highlightthickness=0,width=37,height=9)
        txtNote.pack(side=TOP, anchor=NW, padx=right_container_Entry_padding,pady=10)
        txtNote.propagate(0)

        self.__addSaveButton()


    def generatePassword(self):
        password = Shared.generatePassword()
        passwordInput = self.inputList[self.Password_INDEX]
        passwordInput.delete(0,END)
        passwordInput.insert(0,password)

    def __addSaveButton(self):
        if self.isPasswordMode:
            btnSave = Button(self.container_password_frame, text="Save", font=right_container_entry_font, fg="#ffffff",
                             bg=right_container_input_background, width=37, command=self.__save)

            btnSave.pack(side=TOP, anchor=NW,pady=right_container_label_padding,fill="x")
            self.btnSave = btnSave
        else:
            btnSave = Button(self.container_password_frame, text="Save", font=right_container_entry_font, fg="#ffffff",
                             bg=right_container_input_background, width=35, command=self.__save)

            btnSave.pack(side=TOP, anchor=NW, padx=right_container_Entry_padding,pady=(10,0))
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
        self.selectedAccount = account
        self.savePasswordMode()
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
        self.toggleEditing(False)
        print(self.isEditable)


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
        if self.isPasswordMode:
            if self.__validation(self.SAVE_MODE):
                status = self.db.saveAccount((self.inputList[0].get(),self.inputList[1].get(),self.inputList[2].get()))
                accountList = self.db.getAllAccounts()
                Shared.getFrameMiddle().refresh(accountList)
                for x in self.inputList:
                    x.delete(0,END)
        else:
            # TODO ADD Save Note Feature
            pass

    def __delete(self):
        if self.isPasswordMode:
            result = self.db.deleteAccount(self.selectedAccount)
            if result:
                self.savePasswordMode()
                Shared.getFrameMiddle().refresh(self.db.getAllAccounts())
        else:
            # TODO Add Delete Note Feature
            pass

    def __update(self):
        if self.isPasswordMode:
            if self.__validation(self.UPDATE_MODE):
                print("Updating Values......")
                self.selectedAccount.username = self.inputList[1].get()
                self.selectedAccount.password = self.inputList[2].get()
                self.db.updateAccount(self.selectedAccount)
                self.savePasswordMode()
                Shared.getFrameMiddle().refresh(self.db.getAllAccounts())
        else:
            # TODO Add Update Note feature
            pass

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

    def savePasswordMode(self):
        self.btnEdit.place_forget()
        self.btnDelete.place_forget()
        self.__removeUpdateButton()
        self.__removeSaveButton()
        self.__addSaveButton()
        self.isEditable = False
        self.clearFields()


    def clearFields(self):
        self.toggleEditing(False)
        for x in self.inputList:
            x.delete(0,END)

    def __validation(self,mode):
        if mode == self.SAVE_MODE:
            if not self.inputList[self.ACCOUNT_NAME_INDEX].get().strip():
                tkinter.messagebox.showerror("Validation Error","Account Name cannot be empty")
                return False
            elif not self.inputList[self.USERNAME_INDEX].get().strip():
                tkinter.messagebox.showerror("Validation Error", "Username cannot be empty")
                return False
            elif not self.inputList[self.Password_INDEX].get().strip():
                tkinter.messagebox.showerror("Validation Error", "Password cannot be empty")
                return False
            else:
                return True
        elif mode == self.UPDATE_MODE:
            if not self.inputList[self.USERNAME_INDEX].get().strip():
                tkinter.messagebox.showerror("Validation Error", "Username cannot be empty")
                return False
            elif not self.inputList[self.Password_INDEX].get().strip():
                tkinter.messagebox.showerror("Validation Error", "Password cannot be empty")
                return False
            else:
                return True
        return False















