try:
  def match_words(words):
    ctr = 0
    for word in words:
      if len(word) > 1 and word[0] == word[-1]:
        ctr += 1
    return ctr
  print(match_words()) # ['abc','xyz','abc','12231']

except TypeError as ece :
  print("AN EXCEPTION OCCURED:",ece)
finally:
  print("it is excuted")






