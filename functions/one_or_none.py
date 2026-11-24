# Write a function `one_or_none` that accepts two boolean values.
# Return True if EXACTLY ONE of them is True.
# Return False if both are True OR both are False.

def one_or_none(value1,value2):
    if value1 == True and value2 == False:
        return True
    elif value1 == False and value2 == True:
        return True
    else:
        return False

print(one_or_none(True,False))
print(one_or_none(False,False))
print(one_or_none(True,True))
print(one_or_none(False,True))
