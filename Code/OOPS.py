# OOPS in Python 
# object oriented programming (It improves readability)

# class and object

# creating class
class student :
    name = "Arnav Pratap Singh"

# creating object (instance)
s1 = student()
print(s1)
print(s1.name)
s2 = student()
print(s2.name) # the output will be same as before because there's only one name in the class

class Person :
    name = "Arnav"
    occupation = "Student"
    networth = "0"
a = Person()
print(a.name , a.occupation) 

class Person :
    name = "XYZ"
    occupation = "Student"
    networth = "0"
    def info(self) :
        print(f"{self.name} is a {self.occupation}")

a = Person()
a.name = "Arnav"
a.occupation = "Web Developer"
a.info()

class car :
    colour = "Blue"
    model = "EQS"

car1 = car()
print(car1.colour)
print(car1.model)

# __init__ function (invoked during object creation) note - it is a constructor and if we don't create it then  
# python itself will create it but we won't be able to see that.
# all classes have a function called __init__(), which is always executed when the object is initiated . It always 
# taked two parameters and those represents object first parameter is generally called self

# __init__(self) is a default constructors

class student :
    def __init__(self,second,age): # we could've also used some other word instead of self
        self.name = second # here name is a variable and since we did't inform about it therefore it will be 
# created automatically.
        self.age = age # note - self.name is an object refrence called instance attribute in that self means that 
# every object have have different name similarly self.age represents that every object will have different age.
        print("adding new student in Database...")
s1 = student("Arnav","17") # as soon as we created s1 = student it runs throuh self parameter of init 
print(s1.name,s1.age)
s2 = student("Abigail","17")
print(s2.name,s2.age)
s3 = student("17","Chris") # here 17 is stored in name and  chris in age
print(s3.name,s3.age)

# class and instance attributed

class student:
    college_name = "XXX College" # class attribute
    def __init__(self,name):
        self.name = name
        print("Adding new student to Database")
s1 = student("Arnav")
print(s1.name)
print(student.college_name)

