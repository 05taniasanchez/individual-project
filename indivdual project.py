from tkinter import * #imports packages needed for the application to run
import random #imports packages needed for the application to run
from PIL import Image, ImageDraw, ImageTk #imports packages needed for the application to run
import xlwt #imports packages needed for the application to run
import pandas as pd  #imports packages needed for the application to run
import openpyxl  #imports packages needed for the application to run
import xlrd  #imports packages needed for the application to run

#Setting the parameters for the GUI
root = Tk() #identifying what root = in our application
root.geometry("900x600") #this is for the sizing of screen that will appear for the interface
root.title("What should we eat?") #this is for the title that will be shown on the GUI
root.config(bg = "light green") #this is giving a background color to the GUI BG means background
root.resizable(0,0) #this enanbles users to make the GUI screen larger


# GUI Introduction to the users (first two labels on GUI)
label1= Label(text = " What should we eat today? ", bg = "light blue", font = ("Britannic", 20)).place(x=250, y = 20)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI

label2= Label(text = " Please allow 3 friends to fill out the following form to decide where or what to eat today ☺ ",
bg = "light blue", font = ("Britannic", 10)).place(x=170, y = 80)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

#Labels for GUI
label3= Label(text = " Friend 1 Choices", bg = "light pink", font = ("Britannic", 10)).place(x=40, y = 120)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label4= Label(text = " Friend 2 Choices", bg = "coral", font = ("Britannic", 10)).place(x=390, y = 120)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label5= Label(text = " Friend 3 Choices", bg = "violet", font = ("Britannic", 10)).place(x=730, y = 120)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

# friend 1 labels
label6= Label(text = "1st food Choice", bg = "light pink", font = ("Britannic", 10)).place(x=10, y = 170)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label7= Label(text = "2nd food Choice", bg = "light pink", font = ("Britannic", 10)).place(x=10, y = 220)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label8= Label(text = "3rd food Choice", bg = "light pink", font = ("Britannic", 10)).place(x=10, y = 270)

#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

#  friend 2 labels
label9= Label(text = "1st food Choice", bg = "coral", font = ("Britannic", 10)).place(x=310, y = 170)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label10= Label(text = "2nd food Choice", bg = "coral", font = ("Britannic", 10)).place(x=310, y = 220)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label11= Label(text = "3rd food Choice", bg = "coral", font = ("Britannic", 10)).place(x=310, y = 270)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

# friend 3 labels
label12= Label(text = "1st food Choice", bg = "violet", font = ("Britannic", 10)).place(x=620, y = 170)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label13= Label(text = "2nd food Choice", bg = "violet", font = ("Britannic", 10)).place(x=620, y = 220)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

label11= Label(text = "3rd food Choice", bg = "violet", font = ("Britannic", 10)).place(x=620, y = 270)
#this is a label created,bg = background, font enables us to change the text system, place helps position the text on the GUI
#text function allows us to insert a text

# bottom image
img = Image.open("foods.png") #this opens the image
rgba = img.convert("RGBA") #converts the image to RGBA
datas = rgba.getdata() #pulls RGBA from the orignal image

newData = [] #variable storing the data
for item in datas:
    if item[0:3] == (255, 255, 255): #pulls the white values from the image
        newData.append((255, 255, 255, 0)) #replacing the white with a transcparent background
    else:
        newData.append(item) #adding the changes to the image
rgba.putdata(newData) #allowing for changes to be applied, putdata = applies function above to the image
rgba.save("foods1.PNG", "PNG") #saves the image

Logo_Link = "foods1.PNG" #stores the new image in the logo_link variable
Logo = Image.open(Logo_Link) #opens the new image


img = PhotoImage(file="foods1.PNG") #display new place
label12 =Label(root, image=img, bg = "light green").place(x=45, y=380) #places the image on the GUI

# entry box for friend 1
choice1Variable = StringVar() #setting the accpeted paramenter for the varibale
choice2Variable = StringVar() #setting the accpeted paramenter for the varibale
choice3Variable = StringVar()#setting the accpeted paramenter for the varibale

Entrychoice1 = Entry(root, textvariable= choice1Variable, bg = "light pink").place(x=140, y =170, height = 30, width=150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

Entrychoice2 = Entry(root, textvariable= choice2Variable, bg= "light pink").place(x=140, y =220, height = 30, width= 150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

Entrychoice3 = Entry(root, textvariable= choice3Variable, bg= "light pink").place(x=140, y =270, height = 30, width= 150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box


#entry box for friend 2
choice4Variable = StringVar() #setting the accpeted paramenter for the varibale
choice5Variable = StringVar() #setting the accpeted paramenter for the varibale
choice6Variable = StringVar() #setting the accpeted paramenter for the varibale

Entrychoice6 = Entry(root, textvariable= choice4Variable, bg = "coral").place(x=440, y =170, height = 30, width=150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

Entrychoice7 = Entry(root, textvariable= choice5Variable, bg= "coral").place(x=440, y =220, height = 30, width= 150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

Entrychoice8 = Entry(root, textvariable= choice6Variable, bg= "coral").place(x=440, y =270, height = 30, width= 150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

#entry boxes for friend 3
choice7Variable = StringVar() #setting the accpeted paramenter for the varibale
choice8Variable = StringVar() #setting the accpeted paramenter for the varibale
choice9Variable = StringVar() #setting the accpeted paramenter for the varibale

Entrychoice7 = Entry(root, textvariable= choice7Variable, bg = "violet").place(x=740, y =170, height = 30, width=150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

Entrychoice8 = Entry(root, textvariable= choice8Variable, bg = "violet").place(x=740, y =220, height = 30, width=150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

Entrychoice9 = Entry(root, textvariable= choice9Variable, bg = "violet").place(x=740, y =270, height = 30, width=150)
#creating entry box, textvariable allows us to know what is accepted in the entry box, place is for positiong of the entry
#heigh/width is for the sizing of the entry box

#getting the data into excel
def submitToExcel():
    choice1= choice1Variable.get() #inserts the data from choice 1 into the excel file
    choice2= choice2Variable.get() #inserts the data from choice 2 into the excel file
    choice3= choice3Variable.get() #inserts the data from choice 3 into the excel file
    choice4= choice4Variable.get() #inserts the data from choice 4 into the excel file
    choice5= choice5Variable.get() #inserts the data from choice 5 into the excel file
    choice6= choice6Variable.get() #inserts the data from choice 6 into the excel file
    choice7= choice7Variable.get() #inserts the data from choice 7 into the excel file
    choice8= choice8Variable.get() #inserts the data from choice 8 into the excel file
    choice9= choice9Variable.get() #inserts the data from choice 9 into the excel file
    workbook = xlwt.Workbook()

#naming the sheet in the excel
    sheet = workbook.add_sheet("Random food generator")
    sheet.write(0, 0,"winner") #placing the data into excel column
    sheet.write(1, 0, choice1) #placing the data into excel column
    sheet.write(2, 0, choice2) #placing the data into excel column
    sheet.write(3, 0, choice3) #placing the data into excel column
    sheet.write(4, 0, choice4) #placing the data into excel column
    sheet.write(5, 0, choice5) #placing the data into excel column
    sheet.write(6, 0, choice6) #placing the data into excel column
    sheet.write(7, 0, choice7) #placing the data into excel column
    sheet.write(8, 0, choice8) #placing the data into excel column
    sheet.write(9, 0, choice9) #placing the data into excel column

#saving the input
    workbook.save("hello.xlsx")

    choice1Variable.set(" ") #setting the data recieved
    choice2Variable.set(" ") #setting the data recieved
    choice3Variable.set(" ") #setting the data recieved
    choice4Variable.set(" ") #setting the data recieved
    choice5Variable.set(" ") #setting the data recieved
    choice6Variable.set(" ") #setting the data recieved
    choice7Variable.set(" ") #setting the data recieved
    choice8Variable.set(" ") #setting the data recieved
    choice9Variable.set(" ") #setting the data recieved

button1 = Button(root, text="Enter Results Here", command=submitToExcel, bg = "orange").place(x=310,y=320) #button to
#send the data into excel

data = pd.read_excel("hello.xlsx") #letting python know what file to use

#getting one food option to be the lucky winner
def winner():
    df = pd.DataFrame(data, columns=['winner']) #this grabs data from the winner cloumn
    selected_rows = df[~df['winner'].isnull()] #identifying the data frama for solumn needed
    random = selected_rows.sample() #getting the row
    lb.config(text=random) # creating label
    lb.place(x=420, y=350, width=150) #putting a place for the label
button4 = Button(root, text="Results", command=winner, bg = "orange", width=15).place(x=500, y=320) #creating the button
#for the winner function

lb= Label(root, text= " ", bg= "orange") #creating a label for the def winner function
lb.place(x=425, y=465) #placing the label on the GUI

root.mainloop()



