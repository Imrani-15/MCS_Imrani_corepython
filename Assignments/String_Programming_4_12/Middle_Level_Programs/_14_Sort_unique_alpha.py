# Sort unique words alphanumerically
def words_alphan():
    for i in text.split():
        print(",".join(sorted(list(set(i)))))
text = input("enter your string:")
words_alphan()