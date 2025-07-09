"""
my_iterative_factorial
Description
2! => 2 x 1 => 2
3! => 3 x 2 x 1 => 6
4! => 4 x 3 x 2 x 1 => 24

Let's create a function to calculate the factorial of a number!

Create an iterated function that returns a number. This number is the result of a factorial operation based on the number given as a parameter.

If there's an error, the function should return 0.
You have to use a loop (for/while/...) to perform this exercise

Function prototype (c)
/*
**
** QWASAR.IO -- my_iterative_factorial
**
** @param {int} param_1
**
** @return {int}
**
*/

int my_iterative_factorial(int param_1)
{

}
Example 00

Input: 2
Output: 
Return Value: 2
Example 01

Input: 3
Output: 
Return Value: 6
Example 02

Input: 4
Output: 
Return Value: 24
"""

def my_iterative_factorial(param_1):
    #check if the input is a non-negative integer
    if not isinstance(param_1, int) or param_1 < 0:
        return 0
    # Initialize the result to 1 (0! = 1)
    result = 1
    # Use a loop to calculate the factorial
    for i in range(1, param_1 + 1):
        result *= i
    return result  


# Example usage:
print(my_iterative_factorial(4))  # Output: 2