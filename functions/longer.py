# Write a function `longer` that accepts two strings.
# Return the string that is longer.
# If both strings have the same length, return the first string.


def longer(word1,word2):
    if len(word1) >= len(word2):
        return word1
    else:
        return word2

print(longer("hello","world"))
print(longer("Bryan","Unarine"))
print(longer("Smart","Goal"))
print(longer("flannel", "sustainable"))
