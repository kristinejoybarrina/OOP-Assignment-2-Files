# Kristine Joy Barrina # BSCPE 1-5 # April 5, 2023

# PSEUDOCODE


# Initialize the variables

loop_ctrl_plaintext = 0
loop_ctrl_key = 0
key_char_value = []
plaintext_char_value = []

# Use while loop for error input

while loop_ctrl_plaintext == 0:
    
#   Let the user input a message

    plaintext = str (input ("Enter the message: "))

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
            print ("Input the message in uppercase!")
            loop_ctrl_plaintext = 0
            
    else:
        print ("Input the message with no spaces!")
        loop_ctrl_plaintext = 0
        
# Let the user input the key

while loop_ctrl_key == 0:
    
    key = str (input ("Enter the key: "))
 
 #   Display an error message when there's a space in key   
 
    def has_space (key):
        return " " in key
    
    key_space = (has_space(key))

    if key_space == False:
        loop_ctrl_key += 1
        
        if key.isupper() == True:
            loop_ctrl_key += 1
            
        else:
            print ("Input the key in uppercase!") 
            loop_ctrl_key = 0
    else:
        print ("Input the key with no spaces!")
        loop_ctrl_key = 0
        
# Display an error message when there's a lowercase in key
# Convert the character of plaintext to its integer equivalent using ord 
# Convert the character of key to its integer equivalent using ord
# Define a function called "encrypt"
# Create a variable with empty strings
# Add numbers then take the result of mod 26
# Add 65 to get the ciphertext
# Call the function and display the output


