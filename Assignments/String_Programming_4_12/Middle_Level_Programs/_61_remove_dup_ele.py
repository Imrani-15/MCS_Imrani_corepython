# remove duplicate characters of a given string
def remove_dupplicate(txt):
    result = ''
    for i in txt:
        if i not in result:
            result = result+i
    print("Remove the duplicates characters of a given string:",result)
txt = input("Enter the string: ")
remove_dupplicate(txt)
