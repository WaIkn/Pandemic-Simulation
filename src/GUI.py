import tkinter as tk

class MainGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        SimulationFrame(self)
        UtilityFrame(self)
        self.master = master
        self.pack()

class SimulationFrame(tk.Canvas):
    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf=cnf, height=600, width=800, borderwidth = 2, relief = "groove")
        self.pack(side = tk.LEFT)

class UtilityFrame(tk.Frame):
    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf=cnf, height = 600, borderwidth = 2, relief = "groove")
        Button_StartSimulation(self)
        Frame_NbIndividual(self)
        Frame_ConfinedRatio(self)
        self.pack(side = tk.RIGHT)

class Button_StartSimulation(tk.Button):
    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf=cnf,height = 5, width = 20, text = "Start simulation")
        self.pack(side = tk.BOTTOM)
    
class Entry_Int(tk.Entry):
    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf={},  validate = "key", validatecommand = (master.register(self.isNumber), '%S'))
        self.pack(side = tk.TOP)

    def isNumber(self,s):
        try:
            int(s)
        except Exception as e:
            return False

        return True

class Entry_float(tk.Entry):
    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf={},  validate = "key", validatecommand = (master.register(self.isNumber), '%P'))
        self.pack(side = tk.TOP)

    def isNumber(self,s):
        try:
            float(s)
        except Exception as e:
            return False

        return True 

class Frame_NbIndividual(tk.Frame):

    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf=cnf)
        lab = tk.Label(self, text = "Nb Invdividual")
        lab.pack(side=tk.LEFT)
        et = Entry_Int(self)
        et.pack(side=tk.RIGHT)
        self.pack(side=tk.TOP)

class Frame_ConfinedRatio(tk.Frame):

    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf=cnf)
        et = Entry_float(self)
        et.pack(side=tk.RIGHT)
        lab = tk.Label(self, text="Confined Ratio")
        lab.pack(side=tk.LEFT)
        self.pack(side=tk.BOTTOM)

class Frame_SimulationDuration(tk.Frame):
    
    def __init__(self, master=None, cnf={}):
        super().__init__(master=master, cnf=cnf)


root = tk.Tk()
app = MainGUI(master=root)
app.mainloop()