granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("user_details.txt","r")
    for i in file:
        a,b = i.split(",")
        b = b.strip()
        if(a==name and b==password):
            success=True
            break
    file.close()
    if (success):
        print("Login succesfully.....Thank you so much spend the time with our company website {}".format(name))
        grant()
    else:
        print("Wrong username or password")
def register(name,password):
    file = open("user_details.txt","a")
    file.write("\n"+name+","+password)
    file.close()
    print("Thank you for Registration Please login {}".format(name))
    grant()
    # print("### User Details ###")
    # print("Username: ",name)
def access(option):
    global name
    if (option == 'login'):
        print("Enter the username and password to login")
        name = input("Enter the username: ")
        password = input("Enter the password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter the username: ")
        password = input("Enter the password: ")
        register(name,password)
def begin():
    global option
    print(5*'$',"Welcome to MCS Pvt Ltd",5*'$')
    option = input("Login or Register (login,reg): ")
    if (option != 'login') and  (option != 'reg'):
        begin()

begin()
access(option)
if granted:
    print(5 * '$', "Welcome to MCS Pvt Ltd", 5 * '$')
    print("### Username Details ### ")
    print("Username: ", name)