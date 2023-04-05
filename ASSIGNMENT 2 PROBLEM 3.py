# Kristine Joy Barrina # BSCPE 1-5 # April 5, 2023
# Creating a program that encrypts a plaintext and key

# PSEUDOCODE

# Import modules
import tkinter as tk
from tkinter import *
from pyfiglet import Figlet
from termcolor import colored
from colorama import Style, Back

# Initialize the variables
loop_ctrl_plaintext = 0
loop_ctrl_key = 0
key_char_value = []
plaintext_char_value = []

# Use while loop for error input
while loop_ctrl_plaintext == 0:
    
#   Let the user input a message
    plaintext = str (input ( Style.RESET_ALL + "Enter the message: " ))
    plaintext_length = len (plaintext)

#   Display an error message when there's a space in message
    def has_space (plaintext):
        return " " in plaintext
    
    plaintext_space = (has_space(plaintext))

    if plaintext_space == False:
        loop_ctrl_plaintext += 1
 
 #      Display an error message when there's a lowercase in message
        if plaintext.isupper () == True:
            loop_ctrl_plaintext += 1
            
        else:
            print ("\033[1;31m" + "Input the message in uppercase!\n")
            loop_ctrl_plaintext = 0
            
    else:
        print ("\033[1;31m" + "Input the message with no spaces!\n")
        loop_ctrl_plaintext = 0
        
# Let the user input the key
while loop_ctrl_key == 0:
    
    key = str (input (Style.RESET_ALL + "Enter the key: "))
    key_length = len (key)
 
 #   Display an error message when there's a space in key   
    def has_space (key):
        return " " in key
    
    key_space = (has_space(key))

    if key_space == False:
        loop_ctrl_key += 1
        
        if key.isupper() == True:
            loop_ctrl_key += 1

#    Display an error message when there's a lowercase in key
        else:
            print ("\033[1;31m" + "Input the key in uppercase!\n") 
            loop_ctrl_key = 0
    else:
        print ("\033[1;31m" + "Input the key with no spaces!\n")
        loop_ctrl_key = 0
        
# Convert the character of plaintext to its integer equivalent using ord
for i in range (plaintext_length):
    plaintext_char_value.append (ord (plaintext [i]))
 
# Convert the character of key to its integer equivalent using ord
for i in range (key_length):
    key_char_value. append (ord (key [i]))

# Define a function called "encrypt"
def encrypt (plaintext, key):
    
#   Create a variable with empty strings
    ciphertext = ""
    for i in range (len(plaintext_char_value)):
        
#       Add numbers then take the result of mod 26
        character_value = (plaintext_char_value [i] + key_char_value [i % key_length]) % 26
        
#       Add 65 to get the ciphertext
        ciphertext += chr (character_value + 65)
        
#   Return the value
    return ciphertext

# Call the function and display the output
encrypted_code = (encrypt(plaintext, key))

# Displaying a notice message that the user got the code
notice_message = Figlet (font = "standard")
print (colored (notice_message.renderText("YOU GOT THE CIPHERTEXT"), "yellow"))

# Designing the output through tkinter
# Create an instance tkinter window or frame
root = Tk ()

# Create the dimension of window
root. geometry ("400x250")
root.title ("Encrypted Code")

# Create a widget, label, and button
text_window = Text (root, height = 10, width = 50, bg = "black", foreground = "white")
label_window = Label (root, text = "SHHHH! Keep it as a secret!", foreground = "red", justify = CENTER, font = ("Arial", 14, "bold"))
button_window = Button (root, text = "CLOSE", command = root.destroy)

# Let the pack method declares the position attributes
text_window.pack()
label_window.pack ()
button_window.pack ()

# Insert the encrypted code to the window
text_window.insert (tk.END, encrypted_code)

tk.mainloop()