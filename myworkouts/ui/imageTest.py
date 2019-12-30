import tkinter as tK

from PIL import Image, ImageTk

def createImage():
    windowWidget = tK.Tk()
    imageObject = Image.open('db.jpg')
    imageWidget = ImageTk.PhotoImage(imageObject)

    tK.Label(windowWidget,image=imageWidget).grid(row=20,column=100)

    #tK.Label(windowWidget, justify=tK.LEFT, padx=10, text='''nanda is great man,
    #he acheieved lot in life''').pack(side='left')

    windowWidget.mainloop()

createImage()