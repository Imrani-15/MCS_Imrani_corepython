import string
def ispan(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True

str = 'aaaaaaaaaaaaaaaaaaaaaaaaaa' # The quick brown fox jumps over the lazy dog
print(len(str))
if(ispan(str) == True):
    print("yes")
else:
    print("No")
