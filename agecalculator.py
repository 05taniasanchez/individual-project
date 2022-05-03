
#tkinter
from tkinter import *
from datetime import date
root = Tk()
root.title("Otters Club")
root.geometry('430x300') #it give us width and size
root.resizable(0, 0)

#create an image background for your gui
img = PhotoImage(file="csumbtransparent.png")
label =Label(root, image=img)
label.grid(row=1, column=2, padx=20)


Datebox = Entry(root)
Datebox.grid(row=2, column=2)

Namebox = Entry(root)
Namebox.grid(row=3, column=2)

def submit():
   today= date.today()
   age = today.year - int(Datebox.get())
   label3.configure(text= Namebox.get() + " your age is " + str(age) )


#create a button and link it with out DEF function
#command function allows button to be connected or to recall the DEF function
button1= Button(root, text ="Submit your answer", fg='Green', command=submit)
button1.grid(rows=3, column=1)

#we created a label that asks question
label1 = Label(root, text = "Put your year of birth")
label1.grid(row=2, column=1)

#we are creatin a new label that shows output (instead of replacing Are you an otter)
label2 = Label(root, text = "What is your name?")
label2.grid(row=3, column=1)

#label 3 to show the statement output
label3 = Label(root, text = "     ")
label3.grid(row=5, column=2)
root.mainloop()

