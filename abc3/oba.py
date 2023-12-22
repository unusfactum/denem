def manipulate_string(string):
    # Reverses the string
    reversed_string = string[::-1]
    
    # Converts string to uppercase
    uppercase_string = string.upper()
    
    # Splits the string into a list of words
    words_list = string.split()
    
    return reversed_string, uppercase_string, words_list

input_string = "Hello, this is a random code snippet!"
reversed_result, uppercase_result, words_list_result = manipulate_string(input_string)

print("Reversed string:", reversed_result)
print("Uppercase string:", uppercase_result)
print("List of words:", words_list_result)
