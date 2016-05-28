

class TaskController():
    """docstring for TaskController"""
    def __init__(self, master, model):
        if not master or not isinstance(master, tk.Tk):
            raise Exception("master is not a tk.Tk()")
        self.master = master
