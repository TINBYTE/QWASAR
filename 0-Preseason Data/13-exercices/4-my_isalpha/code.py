#Description
#Create a my_isalpha function.

#Reproduce the behavior of isalpha() function. 
#It returns 1 if the character sent as argument is a letter (A to Z or a to z). It returns 0 otherwise.


def my_isalpha(param_1):
    # Check if the input is a single character
    if len(param_1) != 1:
        return 0
    
    # Check if the character is an alphabet letter
    if ('a' <= param_1 <= 'z') or ('A' <= param_1 <= 'Z'):
        return 1
    
    return 0