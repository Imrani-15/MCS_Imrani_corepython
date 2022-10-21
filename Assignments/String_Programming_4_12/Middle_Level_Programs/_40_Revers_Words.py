# reverse words in a string
def rev_sentence(sen):
    words = sen.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence
sen = input("Enter your sentence")
print(rev_sentence(sen))