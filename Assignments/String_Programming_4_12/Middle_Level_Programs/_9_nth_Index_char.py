# nth index character from string
class Ind_char:
    def __init__(self):
        pass
    def n_index_char(self):
        res = ""
        for char in range(0,len(test_str)):
            if char!=n:
                res = res+test_str[char]
        print(res)
test_str = input("enter your string:")
n = int(input("enter your index number:"))
i = Ind_char()
i.n_index_char()

