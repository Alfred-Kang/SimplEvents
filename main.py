from tkinter import *
import tkinter as tk

from calendarscreen import calendarScreen

root = Tk()
root.geometry('2304x1440')
root.title('SimplEvents')
root.grid_columnconfigure(0, weight = 1)
root.grid_rowconfigure(0, weight = 1)
root.attributes('-fullscreen', True)

root.mainFrame = Frame(root) # A new frame to 'govern' and contain all other frames
root.mainFrame.pack()
root.uiFrame = Frame(root.mainFrame, bg = 'red')
root.uiFrame.pack(expand = True, fill = BOTH)

def switchtocalendarframe(root):
    root.uiFrame.pack_forget()
    calendarScreen(root) # Calls the Function in CalendarScreen.py

root.uiFrame.grid_rowconfigure(0, weight=0) # For row 0
root.uiFrame.grid_rowconfigure(1, weight=2) # For row 1
root.uiFrame.grid_columnconfigure(0, weight=1) # For column 0
root.uiFrame.grid_columnconfigure(1, weight=1) # For column 1 

#image declaring
calendarimg = PhotoImage(file = "./pictures/calenderbuttonpic.png")
neweventimg = PhotoImage(file = "./pictures/neweventbuttonpic.png")
aboutusimg = PhotoImage(file = "./pictures/aboutusbuttonpic.png")
 
calendarbutton = Button(root.uiFrame, text = "Calendar", width = 965, height = 1135, borderwidth=0, image = calendarimg, bg = 'white', command = lambda: switchtocalendarframe(root))
calendarbutton.grid(row = 0, column = 0, rowspan = 2)

neweventbutton = Button(root.uiFrame, text = "New Event", width = 960, height = 575, borderwidth=0, image = neweventimg, bg = 'white')
neweventbutton.grid(row = 0, column = 1)

aboutusbutton = Button(root.uiFrame, text = 'About Us', width = 957, height = 560, borderwidth=0, image = aboutusimg, bg = 'white')
aboutusbutton.grid(row = 1, column = 1)

root.mainloop()
