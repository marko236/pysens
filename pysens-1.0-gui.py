from tkinter.ttk import * # For 2.x use Tkinter instead of tkinter 
from tkinter import END,Text,Tk # Same here
from tkinter.messagebox import * # and here
import os
import time

def exit():
	ab=askyesno('PySens','Are you sure you want to quit?')
	if ab==True:
		quit()
	else:
		pass

win=Tk()
win.minsize(220,220)
win.resizable(False,False)
win.title("PySens - GUI")
lb=Text(win,bg='black', fg='lime', font='Monospace 10',height=10,width=29)
lb.configure(state='normal')
lb.pack()

def ins():
	sn=os.popen('sensors')
	sno=sn.read()
	lb.delete('1.0',END)
	lb.insert(END,sno)
ins()
Button(win,text=">REFRESH<",command=ins).pack()
Button(win,text=">>EXIT<<",command=exit).pack()
win.mainloop()
