# Append a list to second list
class lst_to_seclst:
    def __init__(self):
        print("constructor body")
    def app_lst_sec_lst(self):
        lst1.extend(lst2)
        print(lst1)
lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]
l = lst_to_seclst()
l.app_lst_sec_lst()