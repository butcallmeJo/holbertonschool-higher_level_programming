import Tkinter as tk

class TaskView(tk.Toplevel):
    """docstring for TaskView"""
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        if not master or not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        self.master = master

        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(master, textvariable = self.__title_var)
        self.__title_label.pack(side = tk.RIGHT)

        toggle_button = tk.Button(master, text="Reverse")
        toggle_button.pack(side = tk.LEFT)

    def update_title(self, title):
        if not title or not isinstance(title, str):
            raise Exception("title is not a string")
        self.__title_var = title
