# find the first repeated character of a given string where the index of first occurrence is smallest
def first_repeated(str1):
  temp = {}
  for ch in str1:
    if ch in temp:
      return ch, str1.index(ch)
    else:
      temp[ch] = 0
  return 'None'

str1 = input("Enter your string: ")
print("First repeated charater of a given string: ",first_repeated(str1))
