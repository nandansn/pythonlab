import tkinter as tk

count = 0
def createDynamicLabels(label):
    
    def counter():
        global count

        count += 1
        label.config(text=str(count))
        label.after(1000, counter)
    counter()

def createUI():
    windowWidget = tk.Tk()
    
    label = tk.Label(windowWidget,fg='red')
    label.pack()
    createDynamicLabels(label)
    

    stopButton = tk.Button(windowWidget,text='Stop',command=windowWidget.destroy)
    stopButton.pack()
    windowWidget.title('GUI Learning')
    windowWidget.mainloop()


    

createUI()