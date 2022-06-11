from tkinter.ttk import * # For 2.x use Tkinter instead of tkinter 
from tkinter import END,Text,Tk # Same here
from tkinter.messagebox import * # and here
import os

def exit():
	ab=askyesno('PySens','Are you sure you want to quit?')
	if ab==True:
		quit()
	else:
		pass
def info():
	showinfo('About PySens','Version: 1.1')
win=Tk()
win.minsize(220,220)
win.resizable(False,False)
win.title("PySens - GUI")
lb=Text(win,bg='black', fg='lime', font='Monospace 12',height=10,width=29,state='normal')
lb.grid(row=0,column=0)

def ins():
	sn=os.popen('sensors')
	sno=sn.read()
	lb.delete('1.0',END)
	lb.insert(END,sno)
ins()
Button(win,text=">>REFRESH<<",command=ins).grid(row=1,column=0)
Button(win,text="INFO",command=info).grid(row=1,column=1)
Button(win,text=">EXIT<",command=exit).grid(row=1,column=2)
win.mainloop()
