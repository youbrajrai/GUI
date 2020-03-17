from tkinter import *
import math
root=Tk()
root.title("Calculator")
#Creating a Label Widget
#Grid Function
e=Entry(root,width=50, borderwidth=5)
e.grid(row=0 ,column=0, columnspan=3, padx=10, pady=10)

def clear():
	e.delete(0, END)
def sum():
	global first
	global math
	math="add"
	first=int(e.get())
	e.delete(0,END)
def sub():
	global first
	global math	
	math="sub"
	first=int(e.get())
	e.delete(0,END)
def mul():
	global first
	global math
	math="mul"	
	first=int(e.get())
	e.delete(0,END)
def div():
	global first
	global math	
	math="div"
	first=int(e.get())
	e.delete(0,END)		
def button_click(num):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(num))
def result(sec):
	second=int(sec)
	if math=="add":
		total=first+second
		e.delete(0, END)
		e.insert(0, str(total))
	if math=="sub":
		total=first-second
		e.delete(0, END)
		e.insert(0, str(total))
	if math=="mul":
		total=first*second
		e.delete(0, END)
		e.insert(0, str(total))
	if math=="div":
		total=first/second
		e.delete(0, END)
		e.insert(0, str(total))				


#Button Function
Button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1)) 
Button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2)) 
Button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3)) 
Button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4)) 
Button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5)) 
Button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6)) 
Button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7)) 
Button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8)) 
Button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9)) 
Button_0 = Button(root, text="0", padx=40, pady=19, command=lambda:button_click(0))
Button_plus = Button(root, text="+", padx=40, pady=20, command=sum)
Button_sub = Button(root, text="-", padx=40, pady=20, command=sub)
Button_mul = Button(root, text="*", padx=40, pady=20, command=mul)
Button_div = Button(root, text="/", padx=40, pady=20, command=div)
Button_equal = Button(root, text="=", padx=95, pady=21, command=lambda:result(e.get()))
Button_clr = Button(root, text="Clear", padx=88, pady=19, command=clear)
#displaying button 
Button_1.grid(row=3, column=0)
Button_2.grid(row=3, column=1)
Button_3.grid(row=3, column=2)

Button_4.grid(row=2, column=0)
Button_5.grid(row=2, column=1)
Button_6.grid(row=2, column=2)

Button_7.grid(row=1, column=0)
Button_8.grid(row=1, column=1)
Button_9.grid(row=1, column=2)

Button_0.grid(row=4, column=0)
Button_plus.grid(row=5, column=0)
Button_sub.grid(row=6, column=0)
Button_mul.grid(row=6, column=1)
Button_div.grid(row=6, column=2)
Button_equal.grid(row=5, column=1, columnspan=2)
Button_clr.grid(row=4, column=1, columnspan=2) 

#infinite Loop
root.mainloop()

