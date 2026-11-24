# Write a function `is_div_by_4` that accepts a number as an argument.
# The function should return a boolean indicating whether or not
# the number is divisible by 4.

def is_div_by_4(num):
    if num % 4 == 0:
        return True
    else:
        return False

print(is_div_by_4(8))  # Should print True
print(is_div_by_4(16))
print(is_div_by_4(20))
print(is_div_by_4(25))
print(is_div_by_4(32))
