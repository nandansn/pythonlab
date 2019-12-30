import tkinter as tk

def createLabels():
    windowWidget = tk.Tk()

    for label in ['name:','age','phone']:
        tk.Label(windowWidget,text=label).pack()
    

    windowWidget.mainloop()

createLabels()