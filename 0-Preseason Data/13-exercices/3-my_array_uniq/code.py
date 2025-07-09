#Create an array without any duplicates.

#Create a function my_array_uniq that receives an integer array 
#as a parameter and returns an array with those integers 
#but without any duplicates.

def my_array_uniq(param_1):
    #check if the input is a list
    if not isinstance(param_1, list):
        return []
    #check if the input is empty
    if len(param_1) == 0:
        return []
    #create a new list to store unique elements
    unique_list = []
    #iterate through the input list
    for item in param_1:
        #check if the item is not already in the unique list
        if item not in unique_list:
            #add the item to the unique list
            unique_list.append(item)
    #return the unique list
    return unique_list  


# Example usage:
print(my_array_uniq([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# print(my_array_uniq([]))  # Output: []
# print(my_array_uniq([1, 1, 1, 1]))  # Output: [1]
# print(my_array_uniq([1, 2, 3, 4, 5]))  # Output: [1, 2, 3, 4, 5]
# print(my_array_uniq("not a list"))  # Output: []
# print(my_array_uniq([1, 2, 3, 2, 1, 4, 5, 5]))  # Output: [1, 2, 3, 4, 5]
# print(my_array_uniq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_array_uniq([1, 2, 3, 4, 5, 5, 4, 3, 2, 1]))  # Output: [1, 2, 3, 4, 5]

