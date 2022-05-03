import tkinter as tk #this is where you tell python what packages you need to use
from random import randrange  #this is where you tell python what packages you need to use
from PIL import ImageTk, Image  #this is where you tell python what packages you need to use

root = tk.Tk() #we are identifying what root is

#this is where I added an image to the GUI
img = tk.PhotoImage(file= "candy jar.png") #this is where I defined my image that I wanted to use
label = tk.Label(root, image=img,width=350, height=200) #this is for the sizing of the image
label.place(x=1, y=20) #the placement of the image I'm using


root.title("How Many Candies In The Jar? ") #the tittle of the image I'm using
root.config(bg="light blue") #I added color to the background
root.geometry('350x260') #this give us width and size
root.resizable(0, 0) #allows users not to change the sizing of the screen

lblInst = tk.Label(root, text = "Guess the number of candies in the jar from 0 to 9", fg="purple")
lblLine0 = tk.Label(root, text = "🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭🍭", fg= "red")
lblNoGuess = tk.Label(root, text = " # of Guesses: 0 ", fg="purple")
lblMaxGuess = tk.Label(root, text = " Max Guess: 3 ", fg= "purple")

# where we create the buttons for the game
buttons = [] #defining the buttons
for number in range(0, 10): # giving the buttons a range
    button = tk.Button(root, text=number, command=lambda index=number : process(number), state=tk.DISABLED) # giving the command to label the buttons properly
    buttons.append(button) # closing the button code

#text is what we want the buttons to show
#command gives the operation required in the button code
#state allows the buttons to change according to the command given by the computer/user
#index creates the list of numbers

btnStartGameList = [] # giving the buttons a range
for index in range(0, 1):
    btnStartGame = tk.Button(root, text="Let's play!", fg="purple", command=lambda : startgame(index))
    btnStartGameList.append(btnStartGame)  # closing the button code

#text is what we want the buttons to show
#command gives the operation required in the button code
#state allows the buttons to change according to the command given by the computer/user
#index creates the list of numbers

# creating the grid
lblInst.grid(row=0, column=1, columnspan=5) #positiong the label
lblLine0.grid(row=1, column=1, columnspan=5) #positiong the label
lblNoGuess.grid(row=2, column=0, columnspan=3) #positiong the label
lblMaxGuess.grid(row=2, column=4, columnspan=2) ##positiong the label

#row is for the horizontal alignment
#column is for the vertical alignment
#columnspan is for the telling python how many cloumns the label should be appeared on

for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col  # convert 2d index to 1d. 5= total number of columns
        buttons[i].grid(row=row+10, column=col) #positioning of the button grid
# "i =" is creating the condition that need to be followed
btnStartGameList[0].grid(row=13, column=0, columnspan=5) #positiong the list

#the game

guess = 0 #identifying a condition
totalNumberOfGuesses = 0 #identifying a condition
secretNumber = randrange(10) #identifying a condition
print(secretNumber) #prints the secert number
lblLogs = [] #condition for label
guess_row = 4 #setting a rule

# reseting all variables for the game
def init(): #defining a function
    global buttons, guess, totalNumberOfGuesses, secretNumber, lblNoGuess, lblLogs, guess_row #gobal allows us to modify these variables
    guess = 0 #setting a rule
    totalNumberOfGuesses = 0 #setting a rule
    secretNumber = randrange(10) #identifying what secert number is
    print(secretNumber) #will display the secert number on the GUI
    lblNoGuess["text"] = "Number of Guesses: 0" #what the text will say in the GUI
    guess_row = 4 #setting a rule

# deleting all trys on init
    for lblLog in lblLogs: #allowing the function
        lblLog.grid_forget() #forget is deleting everything from the first attempt
    lblLogs = [] #making lblLogs euqal blank


def process(i): #defining the function
    global totalNumberOfGuesses, buttons, guess_row #Gobal allows us to modify these variables
    guess = i #identifying the guess

    totalNumberOfGuesses += 1 # adds one to everytime an attempt is entered
    lblNoGuess["text"] = "Number of Guesses: " + str(totalNumberOfGuesses) #what will be displayed if lost

    # checking if guess match secret number
    if guess == secretNumber: #if guess secert number is matched
        lbl = tk.Label(root, text="Your guess is correct. You won! ", fg="green") #prints text and makes the text green
        lbl.grid(row=guess_row, column=0, columnspan=5) #positiong of the label
        lblLogs.append(lbl) #closes the function
        guess_row += 1 #adds one to the guess attempt

        for b in buttons:
            b["state"] = tk.DISABLED #gives the ability not to be changed
    else:
        # give player some hints
        if guess > secretNumber:
            lbl = tk.Label(root, text="The number is less than your current guess", fg="red") #prints the text with color
            lbl.grid(row=guess_row, column=0, columnspan=5) #position of the label on the grid
            lblLogs.append(lbl) #closes the label out

            guess_row += 1 #adds one to hint given
        else:
            lbl = tk.Label(root, text="The number is greater than your current guess", fg="red") #prints the text with color
            lbl.grid(row=guess_row, column=0, columnspan=5) #positoning of the label
            lblLogs.append(lbl) #closes label
            guess_row += 1 #adds 1 to the hint given

    # game is over when max no of guesses is reached
    if totalNumberOfGuesses == 3: #if guesses if 3 then python will do the following
        if guess != secretNumber: #what guess ! equals
            lbl = tk.Label(root, text=" Incorrect Guesses! Please try again.", fg="red")  #prints the text with color
            lbl.grid(row=guess_row, column=0, columnspan=5) #positioning of the label
            lblLogs.append(lbl) #closes label
            guess_row += 1 #adds one to the hint given

        for b in buttons:
            b["state"] = tk.DISABLED #gives the ability not to be changed

    buttons[i]["state"] = tk.DISABLED # gives the ability not to be changed


status = "none" #give the status during the game


def startgame(i): #defining a function
    global status #goabl allows the variable to get modified
    for b in buttons:
        b["state"] = tk.NORMAL #allows the button to be changed

    if status == "none": #prompts what to do if the if statment is true
        status = "started" #the action it will perform
        btnStartGameList[i]["text"] = "Can I play again?" #prints the tect
    else:
        status = "restarted" #restarts the game
        init() #integar
    print("Game started") #prints the text

root.mainloop() #closes the GUI/allows it to play

# Sources used https://www.plus2net.com/python/tkinter-button-dynamic.php
#https://levelup.gitconnected.com/learn-python-by-building-a-gui-guessing-game-with-tkinter-9f82291db6
#https://www.codegrepper.com/code-examples/python/how+to+add+grid+in+python+tkinter