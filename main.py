import pyautogui
import tkinter as tk 
from tkinter.filedialog import *

root=tk.Tk()

canvas1=tk.Canvas(root,width=300,height=300)
canvas1.pack()

def ScreenShot():
    myScreenShot=pyautogui.screenshot()
    save_path=asksaveasfilename()
    myScreenShot.save(save_path+"_screenshot.png")






mybutton=tk.Button(text="Take ScreenShot", command=ScreenShot,font=10)
canvas1.create_window(100,100,window=mybutton)


root.mainloop()