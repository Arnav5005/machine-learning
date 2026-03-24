# The input() function pauses your program and waits for the user to enter some text.Once Python receives the user’s
# input, it stores it in a variable to make it convenient for you to work with.
    
message = input('tell me something and i will repeat it back to you :')
print (message) # this is the most basic use of input fucntion

per_info = 'user experience gets better if we know them so please tell us .'
per_info += "\nwhat's your name ?" # the operator += takes the string that was stored in prompt and adds the new 
# string onto the end.
name = input(per_info)
print ('hello,'+name)

age = input("How old are you? ") # whatever input we will give python will save it as a string under age variable so
# if we want to save it as an integers so that we can later use it for comparing with other integers we have to use 
# int function

age = input('how old are you.')
age = int(age)
age >= 18 

age = input('how old are you.')
age = int(age)
if age >= 18 :
    print ('You are eligible to vote.')
else :
    print ('You are not eligible to vote , please vote as soon as you turn 18.')

age = input('how old are you.')
age = int(age)
age >= 18 

# modulo operator (%) - A useful tool for working with numerical information is the modulo operator (%), which 
# divides one number by another number and returns the remainder
# example - 4 % 3 the output would be 1
 
number = input("Enter a number and i will tell you whether it's odd or even.")
number = int(number)
if number % 2 == 0 :
    print('The number entered is even.') 
else :
    print('The number entered is odd.')

car = input('What kind of rental car would you like ?')
print ('Let me see if i can arrange you a',car)

number = input('How many people are there in your dinner group ?')
number = int(number)
if number>8 :
    print("You'll have to wait for the table.")
else :
    print('Your table for '+str(number)+' is ready.') # print function only takes string so we have to convert the 
# number in string first in order to print the message
    
# 1.while loop

# difference in for and while loop

for i in range(3) :
    print (i)
print('done with the loop')

# Method 1

i = 0
while i<3 :
    print (i)
    i=i+1 # due t this line when i is printed then for next value of i , i+1 is looped as it is in while loop 
#(indentation) note - here i also could have used i+=1
print ('done with the loop')

# Method 2

i = int(input('Please enter a number :'))
while i<3 :
    print (i)
print ('done with the loop')

n = int(input('Enter a number'))
i = 1 
while i<=10 :
    print (i*n)
    i += 1

# Method 1 (if we know about the series)

l = [1,4,9,16,25,36,49,64,81,100]
i = 1
while i<=10 :
    print (i**2)
    i += 1

# Method 2 (if we don't know about the series)

# since we don't know about the series so we will print every element of the list
l = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i<len(l) : # here <= was not used because length of list was 10 and for i = 10 l[i] was not defined 
    print (l[i])
    i += 1

# Method 1

i = "Tell me something and i'll repeat after you"
i += '\nHit quit if you want the programme to stop'
x = ""
while x != 'quit' :
    x = input(i)
    print(x)
else :
    print('programme is stopped')
# This program works well, except that it prints the word 'quit' as if it were an actual message. A simple if test 
# fixes this:

i = "Tell me something and i'll repeat it after you :"
i += '\nHit quit if you want the programme to stop'
x = ""
while x != 'quit' :
    x = input(i)
    if x != 'quit' :
        print (x)
print ('The programme is stopped')

# Method 2

i = "Tell me something and i'll repeat after you :"
i += '\nEnter quit if you want the programme to stop'
i = input(i)
if i == 'quit' :
    print('programme is stopped')
else :
    print (i)

# 2.searching 

x = (1,4,9,16,25,36,49,64,81,100,36)
y = 36
i = 0
while i<len(x):
    if x[i]==y :
        print (y,'Found at index',i)
    else :
        print ('Searching...')
    i += 1

# 3.break and continue keyword

# You can use the break statement in any of Python’s loops. For example, you could use,break to quit a for loop 
# that’s working through a list or a dictionary.

# Rather than breaking out of a loop entirely without executing the rest of its code, you can use the continue 
# statement to return to the beginning of the loop based on the result of a conditional test.

i = 0
while i<=5 :
    print(i)
    if i==3 :
        break
    i += 1 

x = (1,4,9,16,25,36,49,64,81,100,36)
y = 36
i = 0
while i<len(x):
    if x[i]==y :
        print (y,'Found at index',i)
        break # here when the loop will break as soon as it finds 36 for the first time
    else :
        print ('Searching...')
    i += 1
print('End of loop')

i = 0 
while i<=5:
    if i==3:
        i+=1
        continue # with this keyword as soon as i becomes 3 this keyword will not print 3 and make it 4(3+1)
    else:
        print (i)

string ="arnav pratap singh"
for char in string :
    if char == 'p' :
        print('p found')
        break
    print (char)
else :
    print ('END') # here END won't be printed as function was break in order to print end we need to remove else and
# also we won't indent it under if because break was under if so break will be overruled.

# 4.flags

# For a program that should run only as long as many conditions are true, you can define one variable that determines 
# whether or not the entire program is active. This variable, called a flag, acts as a signal to the program. We can 
# write our programs so they run while the flag is set to True and stop running when any of several events sets the 
# value of the flag to False. As a result, our overall while statement needs to check only one condition: whether or 
# not the flag is currently True. Then, all our other tests (to see if an event has occurred that should set the 
# flag to False) can be neatly organized in the rest of the program.

command = "Tell me something and i'llrepeat it after you :"
command += ('\nEnter quit if you want the program to stop')
command = input (command)
active = True
while active :
    message = command
    if message == 'quit' :
        active = False
        print ('END')
    else :
        print(message)

city = 'Enter city you wish to visit :'
city += '\nEnter quit if you want the program to end'
while True :
    city = input(city)
    if city == 'quit' :
        print ('END')
        break # if this break wasn't present then quit would also be printed 
    else :
        print ('i would love to go',city)
        
topping = 'Please enter your desired toppings :'
topping += "\nEnter quit if that's all the toppings you want ."
while True :
    topping = input(topping)
    if topping!='quit':
        print ('Adding',topping,'to your pizza')
    else :
        print ('Toppings selected')
        break

    ticket_fair = 'Please enter your age :'
while True :
    age = int(input(ticket_fair)) # here int was necessary because we wan to compare age string with integers for 
# that we need to convert input of age variable to integer .
    if age < 3 :
        print ('Your ticket is free')
    elif age > 12 :
        print('Your ticket fair is $15')
    else :
        print('Your ticket fair is $10')
        break

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []  
while unconfirmed_users:
    new_users=unconfirmed_users.pop() 
    print ('verifying :'+new_users) 
    confirmed_users.append(new_users)
print ('The followingusers have been verified :')
for user in confirmed_users :
    print (user.title())

n = ['Anirudh','Pragyan','Vansh','Anirudh']
while 'Anirudh' in n :
    n.remove('Anirudh')
    print (n) # note this will print list every time on removing Anirudh each time so to avoid this take print 
#outside the while loop

responses = {}
while True :
    name = input('What is your name')
    response = input('Which mountain would you like to climb someday?')
    responses[name]=response # name is key mountain is value 
    # for another person taking the poll
    repeat = input('Do you want anyone else to respond?(Yes/No)')
    if repeat == 'Yes' :
        continue
    else :
        break
print (responses)
print (name,'would like to climb',response)