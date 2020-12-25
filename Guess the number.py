import random
from tkinter import *
import getpass

user_folder_name=getpass.getuser()
row = 0

root = Tk()
root.title("Launcher")
try:
    root.iconbitmap('c:/Users/' + str(user_folder_name) +'/OneDrive/Desktop/db/icon.ico')
except:
    pass
#root.geometry("500x350")

def game():
    global row
    row = int(row)+ 1
    
    user_num = int(num_entry.get())
    
    if user_num == comp_num:
        win_lbl = Label(root, text="You Win!!!").grid(row=row, column=0)
        ButtonQ = Button(root, text="Exit", padx=10, pady=3, bg="#ff0000", fg="black", command=root.destroy).grid(row=row, column=2)
        
    elif user_num < comp_num:
        low_lbl = Label(root, text="Your number is lower!").grid(row=row, column=0)

    else:
        high_lbl = Label(root, text="Your number is higher!").grid(row=row, column=0)    

guess_lbl = Label(root, text="Guess the number: ").grid(row=0, column=0)
num_entry = Entry(root, width=20, bg="white", fg="black", borderwidth=1)
num_entry.grid(row=0, column=1)
Buttona = Button(root, text="Go!", padx=10, pady=3, bg="#ADD8E6", fg="black", command=game).grid(row=0, column=2)

comp_num = random.randint(1, 100)

'''
while True:
    user_num = int(input("Guess the number: "))

    if user_num == comp_num:
        print("You Win!!!")
        choise = input("Do you Want to restart?(y/n)")
        if choise == "y":
            comp_num = random.randint(1, 100)
        elif choise == "n":
            break
    elif user_num < comp_num:
        print("Your number is lower!")
    else:
        print("Your number is higher!")
'''
