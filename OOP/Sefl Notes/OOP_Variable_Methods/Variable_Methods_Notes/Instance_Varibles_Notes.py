'''
INSTANCE VARIABLE
-----------------

1 If the value to variable is varied from object to object, then such type of variables is called as Instance variable

WHERE WE CAN DECLARE THE INSTANCE VARIABLE
------------------------------------------

1 Inside constructor by using self variable
2 Inside Instance Method by using self variable
3 outside of the class by using reference variable

1 INSIDE CONSTRUCTOR BY USING SELF VARIABLES
------------------------------------------
we can declare the instance variable inside a constructor by using self keyword. once we can create the object
automatically these variables will be added to the object

Example:

def Normal:
    def__init__(self):
        self.no = 10
        self.name = 'john'
        self.age = 12
n = Normal()
print(n.__dict__)

2 INSIDE INSTANCE METHOD BY USING SELF VARIABLE:
------------------------------------------------
we can declare the instance variable inside a instance method by using self variable. If declare the instance
variable inside instance method that instance variable will be added once we can the method

Example:
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
    def fn(self):
        self.c = 30
t = Test()
t.fn()
print(t.__dict__)

3 OUTSIDE OF THE CLASS BY USING OBJECT REFERENCE VARIABLE
---------------------------------------------------------
We can also add the instance variable outside of the class by using paricular object

Example:
class Marks:
    def __init__(self):
        self.english = 50
        self.maths = 60
        self.social = 70
    def sci(self):
        self.science = 35
m = Marks()
m.sci()
m.telugu = 80
print(m.__dict__)

HOW TO ACCESS INSTANCE VARIABLE
-------------------------------
We can access the instance variable inside the class by using self variable and outside of the class by
using the reference variable

Example:

class Game:
    def __init__(self):
        self.cricket = cricket
        self.football = football
    def print(self):
        print(self.cricket)
        print(self.football)
g = Game()
g.print()
print(g.cricket,g.football)
'''

'''
STATIC VARIABLE OR CLASS VARIABLE
--------------------------------

If the value of variable is not varied from object to object such type of variable is called as class variable
For total class only one copy of class variable will be created 

Example:
class Test:
    x = 52
    def __init__(self):
        self.y = 35
    def eng_test(self):
        print(Test.x)
        print(self.y)
t  = Test()
t1 = Test()
t.eng_test()
Test.x = 85
t.y = 65
print("===================After Change the value call the function==================")
t.eng_test()
print("============create the second object==============")
t1.eng_test()

VARIOUS PLACES TO DECLARE THE STATIC OR CLASS VARIABLE:
------------------------------------------------------

In general we can declare the class variable inside class directly but outside of any method
Inside constructor we declare the class variable by using class name
Inside instance method we can declare the class variable by using class name
Inside class method we can declare the class variable by using class name or class variable
Inside Static Method we can declare the class variable by using class name

HOW TO ACCESS CLASS OR STATIC VARIABLE:
--------------------------------------
1 Inside constructor: by using either self or classname
2 Inside Instance Method: by using either self or classname
3 Inside class Method: by using either cls variable or class name
4 Inside static Method: by using class name
5 outside Class: by using either cls name or object reference

Example:
class Marks:
    a = 10
    def __init__(self):
        print(self.a)
        print(Marks.a)
    def en(self):
        print(self.a)
        print(Marks.a)
    @classmethod
    def sci(cls):
        print(cls.a)
        print(Marks.a)
m = Marks()
m.en()
m.sci()

LOCAL VARIABLE:
---------------
we can decalre the local variables inside a method directly such type a variables is called as local variable
or temporary variable
local variable will be created at time of method excution and terminate the once method complete
we can not declare the local variable outside of the class

Example:
-------

class Math:
    def m1(self):
        a = 10
        print(a)
    def m2(self):
        b = 20
        print(b)
m = Math()
m.m1()
m.m2()


'''