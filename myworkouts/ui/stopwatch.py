import tkinter as tk

count = 0
def startWatch(label):
    def counter():
        global count
        count += 1
        label.config(text=str(count))
        label.after(1000,counter)
    counter()

def stopWatch(label):
    global count
    label.config(text=str(count))

def resetWatch(label):
    global count
    count = 0
    label.config(text=str(count))




def watchui():
    frame = tk.Tk()
    label = tk.Label(frame,fg='red', text=0)
    label.pack()
    startButton = tk.Button(frame,width=25, text='start')
    startButton.bind('<Button-1>',startWatch(label))
    startButton.pack()

    stopButton = tk.Button(frame,width=25, text='stop')
    stopButton.bind('<Button-1>',stopWatch(label))
    stopButton.pack()

    resetButton = tk.Button(frame,width=25, text='reset')
    resetButton.bind('<Button-1>',resetWatch(label))
    resetButton.pack()

    frame.mainloop()

watchui()

    