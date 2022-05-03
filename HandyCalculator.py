from tkinter import *  #we are letting python know which library we want to use
from PIL import Image, ImageTk #we are letting python know which functions we want to use from a specfiic library

#win are the codes connected to what the computer (python) is told to do such as add/subtract the numbers given to them
#self is the code for the user, which allows them to be able to type in numnbers & click buttons on the wedget

class MyWindow:

    def __init__(self, win): #defining a function we plan to create/use
        self.lbl1=Label(win, text= "Enter the first number.") #creating the label for the 1st input required
        self.lbl2=Label(win, text="Enter the second number.") #creating the label for the 2nd input required
        self.lbl3=Label(win, text= "Give me the Answer!") #creating a label for the results generated
        self.t1=Entry(bd=4, bg= "light gray") #add depth and color to the entry box
        self.t2=Entry(bd=4, bg = "light gray")  #add depth and color to the entry box
        self.t3=Entry(bd=4, bg = "yellow")  #add depth and color to the entry box
        self.btn1 = Button(win, text='Add') #creation of button for the add function
        self.btn2=Button(win, text='Subtract') #creation of button for the subtract funtion
        self.lbl1.place(x=100, y=50) #position the placement of 1st label
        self.t1.place(x=245, y=50) #position of the entry box

        self.lbl2.place(x=100, y=100) #position of the 2nd label
        self.t2.place(x=260, y=100) #position of the 2nd entry box
        self.b1=Button(win, text='Add', command=self.add) #gives the command to be a clickable button
        self.b2=Button(win, text='Subtract') #gives the command to be a clickable button
        self.b2.bind('<Button-1>', self.sub) #gives the command to be a clickable button
        self.b1.place(x=100, y=150) #position of the button
        self.b2.place(x=240, y=150) #position of the button
        self.lbl3.place(x=100, y=200) #position of the result label
        self.t3.place(x=245, y=200) #position of the result box
    def add(self): #this whole section is creating the code to make python get the numbers that the user puts into the box
        #when it comes to the add them together
        self.t3.delete(0, 'end') #where the user puts in the numbers they want to add
        num1=int(self.t1.get()) # 1st number the user put
        num2=int(self.t2.get()) #2nd number the user put
        result=num1+num2 #adds the numbers
        self.t3.insert(END, str(result)) #allows the results for adding to appear in the box
    def sub(self, event): #tbis whole section is the code for python to get the numbers the user puts into the box
        #when it comes to subtracting them for each other
        self.t3.delete(0, 'end') #where the user puts in the numbers they wanna subtract
        num1=int(self.t1.get()) # 1st number the user put
        num2=int(self.t2.get()) # 2nd number the user put
        result=num1-num2 #subtract the numbers entered
        self.t3.insert(END, str(result)) #allows the results for subtracting to appear

root =Tk()
img = ImageTk.PhotoImage(Image.open("lyndaemunoz/csumb.png")) #image I want to use
#the code below is what I used to customize the image into the background of the wedget
canvas = Canvas(root, width = 300, height = 300) #size of the image
canvas.pack()
canvas.create_image(40, 40, anchor=NW, image=img) #position of the picture as a whole

mywin=MyWindow(root)
root.title("Handy Small Calculator") # I changed all window. to root since we used root more in class & changed the tittle
root.config(bg="pink") # I added color to the calculator
root.geometry("500x300") # changed the size to display smaller
root.resizable(0,0) #this allows the user not be able to expand it

root.mainloop()

#codes came from the following websites : https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
#https://www.c-sharpcorner.com/blogs/basics-for-displaying-image-in-tkinter-python