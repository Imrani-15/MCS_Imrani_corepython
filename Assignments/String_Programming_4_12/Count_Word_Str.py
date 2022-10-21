def count_str(string,word1):
    for ele in string.split():
        if ele == word1:
            pass
    print(string.count(word1))
string = input("Enter your string:")
word1 = input("Enter your word:")
count_str(string,word1)
