from  tkinter import *
root = Tk()
root.geometry("500x300")
def getvals():
    print("Accept the Application")
# Heading
Label(root,text="Student login Form", font="ar 15 bold").grid(row=0,column=3)
# Field Name
name = Label(root, text="Name")
phone_number = Label(root, text="Phone Number")
gender = Label(root, text="Gender")
address = Label(root, text="Address")
# Packing Fields
name.grid(row=1,column=2)
phone_number.grid(row=2,column=2)
gender.grid(row=3,column=2)
address.grid(row=4,column=2)


# Variable for storing data
namevalue = StringVar
phone_numbervalue = StringVar
gendervalue = StringVar
addressvalue = StringVar
checkvalue = IntVar

# Creating entry field
nameentry = Entry(root, textvariable = namevalue)
phone_numberentry = Entry(root, textvariable = phone_numbervalue)
genderentry = Entry(root, textvariable = gendervalue)
addressentry = Entry(root, textvariable = addressvalue)

# Packing Entry Fields
nameentry.grid(row=1,column=3)
phone_numberentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
addressentry.grid(row=4,column=3)

# Creating Checkbox
checkbtn = Checkbutton(text="remember me?", variable = checkvalue)
checkbtn.grid(row=5,column=3)

#submit button
Button(text = "Submit",command = getvals).grid(row=6,column=3)
root.mainloop()