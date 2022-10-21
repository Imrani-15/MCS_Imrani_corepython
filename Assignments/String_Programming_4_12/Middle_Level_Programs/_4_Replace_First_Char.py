# Replace first occurance character
class Rel_First_Char:
        def __init__(self):
                pass
        def occ_first(self):
                test_str = 'replace first occurance character'

                # printing original string
                print("The original string is : " + str(test_str))

                # initializing K
                K = '$'

                # replacing using replace()
                res = test_str[0] + test_str[1:].replace(test_str[0], K)

                # printing result
                print("Replaced String : " + str(res))
r = Rel_First_Char()
r.occ_first()