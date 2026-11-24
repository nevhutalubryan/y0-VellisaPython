# Write a function `parity` that accepts a number.
# Return the string "even" if the number is even.
# Return the string "odd" if the number is odd.

def parity(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(parity(4))
print(parity(5))
print(parity(7))
print(parity(10))
