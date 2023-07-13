from tkinter import*
import random
import time

merry = Tk()
merry.geometry("1600*800+0=0")
merry.title("Resturante Management System")

Tops = Frame(root, width = 1600, bg = "powder blue", relief = SUNKEN)
Tops.pack(side = Top)

f1= Frame(root, width = 800, height = 700, bg = "powder blue", relief = SUNKEN)
f1.pack(side = LEFT)

f2= Frame(root, width = 300, height = 700, bg = "powder blue", relief = SUNKEN)
f2.pack(side = RIGHT)

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops, font = ('arial', 50, 'bold'), text = "Resturante Management System", fg = "steel Blue", bd = 10, anchor = 'w')
lblInfo.grid(row = 0, column =0)

lblInfo = Label(Tops, font = ('arial', 10, 'bold'), text = "Resturante Management System", fg = "steel Blue", bd = 10, anchor = 'w')
lblInfo.grid(row = 1, column =0)

merry.mainloop()