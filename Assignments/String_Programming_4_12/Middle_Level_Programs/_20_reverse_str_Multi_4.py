#  reverses a string if it's length is a multiple of 4
class Revers_str:
    def __init__(self):
        pass
    def legth_Multiple_four(self):
        if len(txt) % 4 == 0:
            print("Reverses a string if it's length is a multiple of 4",''.join(reversed(txt)))
        else:
            print("Original string:",txt)

txt = input("Enter your string:")
r = Revers_str()
r.legth_Multiple_four()