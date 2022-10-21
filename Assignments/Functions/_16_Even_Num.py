# print the even numbers from a given list
class Even_Num:
    def __init__(self):
        pass
    def display_even(self):
        for even_no in lst:
            if even_no%2==0:
                print("Even Numbers is:",even_no)
lst = [1,2,3,4,5,6,7,8,9,10,11,12]
e = Even_Num()
e.display_even()