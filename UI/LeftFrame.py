from tkinter import *

from UI.consts import *
class LeftFrame(Frame):

    def __init__(self,master):
        super().__init__(master,width=left_width,height=left_height,bg=left_background)
        lblMenu = Label(self,text="Menu",font="nunito 30 bold",bg=left_background,fg=left_boldTextColor)
        lblMenu.pack(side=TOP,anchor=CENTER,padx=10,pady=10)

        btnPassword = Button(self,text="Password",font="nunito 21",bg=left_background,fg=left_boldTextColor,width=left_width,relief=FLAT,highlightthickness=0)
        btnPassword.pack(side=TOP,anchor=CENTER,pady=10)
        btnPassword.configure(activebackground=left_accentColor,activeforeground=left_boldTextColor)

        btnNotes = Button(self, text="Notes", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        btnNotes.pack(side=TOP, anchor=CENTER, pady=10)
        btnNotes.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        btnImport = Button(self, text="Import", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        btnImport.pack(side=TOP, anchor=CENTER, pady=10)
        btnImport.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        btnExport = Button(self, text="Export", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        btnExport.pack(side=TOP, anchor=CENTER, pady=10)
        btnExport.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        btnLogout = Button(self, text="Logout", font="nunito 21", bg=left_background, fg=left_boldTextColor, width=left_width, relief=FLAT, highlightthickness=0)
        btnLogout.pack(side=TOP, anchor=CENTER, pady=10)
        btnLogout.configure(activebackground=left_accentColor, activeforeground=left_boldTextColor)

        self.buttons = [btnPassword,btnNotes,btnImport,btnExport,btnLogout]