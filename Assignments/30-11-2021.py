class Dict_a:
    def __init__(self,dict1):
        self.id = dict1[1]['id']
        self.name = dict1[1]['name']
        self.salary = dict1[1]['salary']
        for key in dict1:
            if key%2==0:
                print("even number:",dict1[key])
    def emp_details(self):
        return dict1.values()
    def emp_salary(self):

        net = 0
        for i in self.salary.values():
#            print(i)
            net = net+i
        return net


dict1= {1:{'id':101,'name':'john','salary':{'BS':100,'SA':1000,'HR':5000}},2:{'id':102,'name':'kevin','salary':{'BS':200,'SA':2000,'HR':6000}}}
result = Dict_a(dict1)
print("Employee Details:", result.emp_details())
result.emp_salary()
print("=====================CLASS B===================================")
class Dict_b:
    def __init__(self,dict2):
        self.dict2 = dict2
        self.salary = dict2[1]['salary']
        n = 0
        for i in self.salary.values():
            n = n+i
        if n>10000:
            print("salary is above 10k===>",n)
        else:
            print("salary is below 10000")
    def b_emp_details(self):
        return dict2.values()
    def b_emp_salary(self):
        n1 = 0
        for j in self.salary.values():
            n1 = n1+j
        return n1

dict2= {1:{'id':101,'name':'john','location':'Bangulore','salary':{'BS':1000,'SA':10000,'HR':5000}}}
result1 = Dict_b(dict2)
print(result1.b_emp_details())
print(result1.b_emp_salary())