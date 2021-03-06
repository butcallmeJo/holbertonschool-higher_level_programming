import Tkinter as tk

class TaskView(tk.Toplevel):
    """docstring for TaskView"""
    def __init__(self, master):
        # basic init stuff
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        if not master or not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        self.master = master

        # setting up the string to be reversed
        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(self, textvariable = self.__title_var)
        self.__title_label.pack(side = 'right')
        # setting up the button to do the reversing
        self.toggle_button = tk.Button(self, text="Reverse")
        self.toggle_button.pack(side = 'left')

    def update_title(self, title):
        if not title or not isinstance(title, str):
            raise Exception("title is not a string")
        self.__title_var.set(title)
