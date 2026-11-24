# Write a function `is_long` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# is longer than 5 characters.

def is_long(word):
    if(len(word) > 5):
        return True
    else:
        return False

print(is_long("Unarine"))        
print(is_long("Bryan"))
print(is_long("Babe"))
print(is_long("Nevhutalu"))