# Write a function `ends_with_t` that accepts a string as an argument.
# The function should return a boolean indicating whether the string
# ends with the character "t".

def ends_with_t(word):

    if word[-1] == "t":
        return True
    else:
        return False
print(ends_with_t("cat"))  
print(ends_with_t("dog")) 
print(ends_with_t("smart"))
print(ends_with_t("boomerang"))    