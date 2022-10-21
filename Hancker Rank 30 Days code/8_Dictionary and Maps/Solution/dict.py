# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phoneBook = {}
for i in range(n):
    text = input().split()
    phoneBook[text[0]] = text[1]

while True:
    try:
        inpt = input()
        if inpt in phoneBook:
            print(inpt + "=" + phoneBook[inpt])
        else:
            print("Not found")
    except EOFError:
        break

