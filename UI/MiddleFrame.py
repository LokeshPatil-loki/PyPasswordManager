from tkinter import *
from tkinter import ttk

from Database import DBPassMan
from UI.Shared import Shared
from UI.consts import *
from PIL import Image
from Model.Account import *
import Model.Note
import Model.User

class MiddleFrame(Frame):

    def __init__(self,master,accountList,):
        super().__init__(master,width=middle_width,height=middle_height)
        super().configure(bg=middle_background)
        self.accountList = accountList
        self.__addTopFrame()
        self.__addBottomFrame()
        self.count = 1

    def __search(self,event):
        searchString = self.searchVar.get()+event.char
        print("Search String",len(searchString.strip()))
        if len(searchString.strip()) >= 1:
            self.refresh(Shared.getDB().searchAccount(searchString))
        elif len(searchString.strip()) == 0:
            print("less than 0")
            self.refresh(Shared.getDB().getAllAccounts())

    def __addTopFrame(self):
        self.searchVar = StringVar()
        top_frame = Frame(self,bg=middle_background,height=70)
        top_frame.pack(side=TOP,anchor=NW,fill="x")
        top_frame.pack_propagate(0)

        searchBox = Entry(top_frame,font="nunito 16",textvariable=self.searchVar,bg=middle_searchBgBoxColor,fg="#ffffff",relief=FLAT,justify=CENTER,width=26)
        searchBox.pack(side=LEFT,anchor=CENTER,expand=0,padx=(15,0),pady=15)
        searchBox.propagate(0)
        searchBox.bind("<Key>",self.__search)

        image = resizeImage(Image.open("UI/add.png"))
        self.addImage = image

        btnAddCancel = Button(top_frame,text="+",fg="#ffffff",font="nunito 25 bold",bg=middle_accentColor,width=30,height=30,command=self.addCancel)
        btnAddCancel.pack(side=LEFT,anchor=CENTER,expand=0,padx=(15,15),pady=15)
        btnAddCancel.propagate(0)
        self.btnAddCancel = btnAddCancel

    def __addBottomFrame(self,height=0):
        # Create main frame
        main_frame = Frame(self,bg=middle_background)
        main_frame.pack(fill=BOTH, expand=1)
        self.main_frame = main_frame
        # Create Canvas
        my_canvas = Canvas(main_frame,bg=middle_background,highlightcolor="#000000",highlightbackground="#000000",highlightthickness=2)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add scrollbar to canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        # my_scrollbar.configure()
        my_scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_scrollbar.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        self.my_canvas = my_canvas

        # Create Another Frame Inside canvas
        bottom_frame = Frame(my_canvas, bg=middle_background)
        self.bottom_frame = bottom_frame

        # Add frame to window in canvas
        if height == 0:
            my_canvas.create_window((0, 0), window=bottom_frame, anchor=NW)
        else:
            print(height)
            my_canvas.create_window((0, 0), window=bottom_frame, anchor=NW,height=height)

        for x in self.accountList:
            print(x.account_name)
            item1 = PasswordItem(self.bottom_frame, x)
            item1.pack(side=TOP, anchor=NW, expand=0, fill=BOTH)
        total_height = 0
        for x in self.bottom_frame.winfo_children():
            total_height += x["height"]
        self.bottom_frame_height = total_height


    def refresh(self,accountList):
        self.accountList = accountList
        for x in self.main_frame.winfo_children():
            x.destroy()
            x.pack_forget()
            del(x)
        self.main_frame.destroy()
        self.main_frame.pack_forget()
        del(self.main_frame)
        # self.__addBottomFrame(height=(self.bottom_frame_height+(800+200*self.count)))
        self.__addBottomFrame(height=self.bottom_frame_height)
        self.count += 1



    def addCancel(self):
        if self.btnAddCancel["text"] == "+":
            self.btnAddCancel.configure(text="x")
            Shared.getFrameRight().savePasswordMode()
        else:
            self.btnAddCancel.configure(text="+")
            Shared.getFrameRight().clearFields()

class PasswordItem(Frame):
    def __init__(self,master,account,width=446 - 40,height=83):
        super().__init__(master,width=width,height=height,relief=FLAT,bg=middle_background)
        self.account = account
        frame = Frame(self,width=width,height=height,bg=middle_background,bd=1,highlightthickness=1,highlightcolor=middle_strokeColor,highlightbackground=middle_strokeColor)
        frame.pack(side=TOP,anchor=NW,expand=FALSE,padx=10,pady=10)
        frame.pack_propagate(0)

        lblAccountName = Label(frame,text=account.account_name,font="nunito 20 bold",bg=middle_background,fg=middle_regularTextColor)
        lblAccountName.pack(side=TOP,anchor=NW,padx=5)

        lblUserName = Label(frame, text=account.username, font="nunito 18", bg=middle_background, fg=middle_regularTextColor)
        lblUserName.pack(side=TOP, anchor=NW,padx=5)

        self.frame = frame
        self.lblAccountName = lblAccountName
        self.lblUserName = lblUserName
        self.__addClickListener()
        # print("ITEM HEIGHT:",self["height"])

    def __onClick(self,event):
        # print(self.account.account_name)
        # print(self.account.username)
        # print(self.account.password)
        Shared.getFrameMiddle().btnAddCancel.configure(text="+")

        Shared.getFrameRight().refresh(self.account)

    def __addClickListener(self):
        self.frame.bind("<Button-1>",self.__onClick)
        self.lblAccountName.bind("<Button-1>", self.__onClick)
        self.lblUserName.bind("<Button-1>", self.__onClick)
        self.bind("<Button-1>",self.__onClick)


