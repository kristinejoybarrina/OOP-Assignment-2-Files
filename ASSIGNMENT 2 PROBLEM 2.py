#Kristine Joy Barrina #BSCPE 1-5 #April 2, 2023
#Creating a program that decrypts a code

# PSEUDOCODE

from pyfiglet import Figlet
from termcolor import colored
from colorama import Style, Back
from tkinter import *

# Print a notice message that the program will decrypt a code
# Style the texts using pyfiglet
notice_message = Figlet (font = "standard")

# Style the texts using colorama
print (colored (notice_message.renderText("DECRYPT IT!"), "yellow"))

# Let the user input a string then the program will decrypt using character substitutes "a" = *, "e" = &, "i" = #, "o" = +, "u" = !
user_input = str (input ( Back.WHITE + "\033[1m" + "Input a string:" + Style.RESET_ALL + " "))

# Create a variable that has empty strings
output_str = ""

# Create a for loop with range of user's length input
for i in range (len(user_input)):
    
#   Use if-elif-else to check each character written by the user
    if user_input [i] == "*":
        
#       Replace the string punctuation with the equivalent vowels and add each character using +=
        output_str += "a"
        
    elif user_input [i] == "&":
        output_str += "e"

    elif user_input [i] == "#":
        output_str += "i"
        
    elif user_input [i] == "+":
        output_str += "o"
    
    elif user_input [i] == "!":
        output_str += "u"
    
#   If the character is not a punction then proceed to else
    else:
        output_str += user_input [i]

# Display the output using tkinter that generates a window
decrypt_code = output_str

# Create the winder using tkinter instance
win = Tk ()

# Create a title for window
win.title ("Decrypted Code")
win.geometry ("800x250")

# Style the window
decrypt_window = Entry (win, justify = "center", width = 50, bg = "yellow", font = ("Arial", 15, "bold"))
decrypt_window.insert (0, decrypt_code)
decrypt_window.pack (padx = 100, pady = 100)

win.mainloop ()