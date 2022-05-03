from tkinter import *
root = Tk()
root.title("CSUMB APP")
root.geometry("450x450")
root.config(bg = "pink")


def extract_data():
    print(textbox.get("1.0", "end"))



message = ''' 
My dog loves running around 
he's a good dog 
he is getting old 
but he is still going out
one 
two 
three
four 
five 
six 
My dog loves running around 
he's a good dog 
he is getting old 
but he is still going out
one 
two 
three
four 
five 
six 
'''
frame = Frame(root)

textbox = Text(frame, height =15, width =30, wrap = "word")
textbox.pack(side = LEFT, expand = True)
textbox.insert("end", message)

textbox.config(state = "disabled") #disabledtu does not allow editting


sb = Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

textbox.config(yscrollcommand=sb.set)
sb.config(command=textbox.yview)
frame.pack(expand = True)

root.mainloop()