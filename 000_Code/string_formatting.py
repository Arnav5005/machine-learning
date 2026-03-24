# Traditional way

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars." # A modifier is included by adding a colon : 
# followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
print(myorder.format(quantity, itemno, price))  

# if you want to refer to the same value more than once, use the index number:

age = 36
name = "John"
txt = "His name is {0}. {0} is {1} years old." # note -  {} these curley braces are called placeholders .
print(txt.format(age, name))

car = "i own a {carname} , it is a {model}"
print(car.format(carname = "Nissan" , model = "Kicks"))

# New way

fruit = "latinas"
txt = f"I love {fruit.title()}"
print(txt)

price = 6000
txt = f"one russian is worth {price} ruppees"
print(txt) # this is called formatting a string 

# if else statement in placeholders

a = int(input("Enter price :"))
txt = f"The article is {'Expensive' if (a)>1000 else 'Cheap'}"
print(txt)

a = (input("Enter the number :"))
print (f"multiplication table of {a} is :") # here f is used to create an f string or formatted string
for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")
