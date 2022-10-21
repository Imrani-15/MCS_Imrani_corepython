# Flatten a shallow
class Flat:
   def __init__(self):
      print("Constructor body")
   def flastlst(self):
         flatlst = []
         for sublst in lst:
            for item in sublst:
               flatlst.append(item)
         print(flatlst)
lst = [[10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]]
f = Flat()
f.flastlst()