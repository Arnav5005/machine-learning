# CHAPTER 1 (GETTING STARTED)


print ('hello world')


# CHAPTER 2 (VARIABLES , STRINGS , FLOAT)


# 1.variables


message = 'python is a proggraming language'
# note that while printing message i didn't use quotes because it was a variable and if o variable was assigned then quotes would've been used
print (message)

lOl = 'pawa'
print (lOl)

a = 'I told Anirudh , "I slept with his girlfriend"'
# note the example used above is of string i.e. we can use quotes within quotes
print (a)


# 2.title , upper , and lower case


a = "Ava adams"
print (a.title())
print (a.upper())
print (a.lower())
# note - title function is used to print like a title or a proper noun
# if you want to use title , upper and lower function on a list then a for loop is used like -
# l = ['a','B','C','d','e']
# for l_ in l :
#     l_.title()


# 3.strings


# Method 1

first_name = 'Arnav'
middle_name = 'Pratap'
last_name = 'Singh'
full_name = first_name + ' ' + middle_name + ' ' + last_name
# note : 1. python uses + to add strings 
#        2. if these inverted commas (single or double inverted doesn't matter) weren't used then there won't be any
#           space betwenn name and the output would look something like ArnavPratapSingh.
print (full_name)

# Method 2

print (first_name,middle_name,last_name)

# Method 1

first_name = 'Kanishka'
last_name = 'tiwari'
full_name = first_name.upper() + ' ' + last_name.upper() + " " + '!'
# In full_name function exclamatory mark was put under inverted commas because kanishka and tiwari both were a part of variable and so they don't need inverted commas to be defined that's why inverted commas were used on the mark
print (full_name)

# Method 2

print (first_name.upper(),last_name.upper(),"!")

# Method 3 (best way of string formatting)
# f-string

statement="Hey my name is {} and i am from {}"
country="India"
name="Arnav pratap singh"
print(statement.format(name,country))
print(f"Hey my name is {name} and i am from {country}") # Hey my name is Arnav pratap singh and i am from India
print(f"Hey my name is {{name}} and i am from {{country}}") # Hey my name is {name} and i am from {country}

price=42.125
print(f"for only ${price:.2f}") # for only $42.12

# docstring (string literals that we write after the definition of a function , class or module to specify what is happening in the function or code)

def square(n):
    # print(n) this is written before the function definition so this will act as a dosctring if we print(square__docstring__) it'll return none
    '''take in number n, return the square of n''' # this is a docstring and it is written just above the function definition
    print(n**2)
square(5)
print(square.__doc__) # to print the docstring

# python
# import this       this is a command line code it return the Zen of python which is a poem written by Tim Peters

# 4.blankspace , new line


print ('\t\tPython') # \t is used for tabspace and using it twice gives more space
print ('WebDev:\n\tPyhton\n\tC++\n\tJava\n\tHTML') # \n is used to add a new line 

a = "Albert Einstein once said ,"
b = '"A person who never made a mistake have never tried something new."'
print(f'{a} {b}')
print (a,b)

print (0.2+0.1) # the answer is little unappropriate there are ways to correct this innacuracy but will try it later

# Method 1

age = "seventeen" # if numeric 17 would hv been used then it'll generate an error because int. can't be converted to string implicitly that's why alphabetic seventeen is used and if you want to use numeric 17 then either use string function or put 17 in quotes 
message = "happy" + ' ' + age + "th birthday !"
print (message) 
age = "17" 
message = "happy" + ' ' + age + "th birthday !"
print (message) 
age = 17 
message = "happy" + ' ' + str(age) + "th birthday !"
print (message) 

# Method 2

print(f"nigga happy {age}th birthday!")

a = 69
message = "My faivourite number is :"
print (message,'\n',a)
# note the above sentence can be written in 2 more ways and that are
# 1. by putting 69 in quotes and using message = "My faivourite number is" + ' ' + a
# 2. if not putting 69 in quotes then message = "My faivourite number is" + ' ' + str(a)
a = 69
message = "My faivourite number is :"+' '+'\n'+str(a)
print (message)


# CHAPTER 3 (LISTS)

# list is - 

# 1.Ordered
# 2.Mutable
# 3.Heterogeneous
# 4.Index-based datatype

# functions on list - 

# 1.substitution                                                                                                Ex - l[0]='a'
# 2.append                      insert the element at the end of the list                                       Ex - l.append('a')
# 3.insert                      insert the element at a particular position                                     Ex - l.insert(1,'a')
# 4.del                         delete the element from a particular position                                   Ex - del l[1]
# 5.pop                         if you want to access the deleted element                                       Ex - poppedElement=l.pop(1)
# 6.remove                      if you want to remove an element but don't know it's index                      Ex - remove('a')
# 7.sort (irreversible)         used to arrange elements of list in forward/reverse alphabetical order          Ex - l.sort()
# 8.sorted (reversible)         same functionality the only difference is it's reversible                       Ex - print(sorted(l))
# 9.reverse                     used to reverse the list                                                        Ex - l.reverse()
# 10.len                        returnfs length of the list                                                      Ex - print(len(l))

l = ['every','girl','calls','me','daddy']
print (l[0].upper()) # EVERY
print (l[-1]) # daddy
print (l[-2]) # me

l = ['Arnav','aarav']
print (l[0],'says hello to',l[1].title())

# Method 1

l = ['macan','cayenne']
message = 'I would like to buy Porsche'+ ' ' +  l[-1] + ' ' + '!'
print (message)

# Method 2

message = 'I would like to buy Porsche'
print (message,l[0],'!')


# 1.substitution of an element in a list


l = ['Supra','jesco','Dbx']
l[0]='GTR'
print (l)


# 2.append (addition of an element in the end of the list)


l_ = ['Supra','jesco','Dbx'] # point to be noticed that here list name was changed because due to previous function the new list was       l = ['GTR','Jesco','Dbx']
l_.append('GTR') # Append function adds an element to the list at the last position but if you want your newly added element to be at a particular poaition withour replacing any other then use inert funtion
print (l_)
a = ['b','c','d']

print(a.append('a')) # apparantly we have to use nested list if we wish to use function inside a function as a.append('a') will append a at the end of the list but append function return none and print function displays the returned value so it'll print 'none'
print(a) # ['b','c','d','a','a']

a = ['b','c','d']
a.append('a')
print(a) #it will add 'a' but in the end as append always add element in the end of the list

a = ['e','b','c','d']
a[0] = 'a'
print(a) # this will add 'a' in the beginning but we had to manipulate the list


# 3.insert (addition of an element at a particular position)


l = ['Supra','Jesco','Dbx']
l.insert(0,'GTR')
print(l)


# 4.delete (deletion of an element from a particular position)


del l_[0] # delete function is used to delete an element from any position
print (l_)


# 5.pop (If you want to use the value of an item after you remove it from a list . Ex-you might want to remove a user from a list of active members and then add that user to a list of inactive members.) pop removes the last element from the list by default (i.e. if not specified)


l = ['samsung galaxy duos','poco f7','oneplus nord ce 3','redmi note 9']
popped_l = l.pop(1)
print (l)
print (popped_l)
print ('the current phone I own is',popped_l.title(),'and my previously owned phones were',l)


# 6.remove (if the position of an element which is to be removed is not known but it only removes it once i.e. if the same element is occuring twice so to remove that loop must be used) 


l = ['pragyan','anirudh','divya','anirudh']
print (l)
l.remove('anirudh')
print (l)
print ('anirudh is being a weed among the roses.')

l = ['pragyan','anirudh','divya','anirudh']
for a in l :
    l.remove('anirudh')
print (l)

l = ['Joshi','Bihari','Niggi']
message = "You have been invited for dinner at Mr. Arnav's home."
print (l[0],',',message)
print (l[1],',',message)
print (l[2],',',message)

# Method 2

l = ['Joshi','Bihari','Niggi']
message = "You have been invited for dinner at Mr. Arnav's home."
for name in l :
    print ('\n'+name,", You gave been invited for dinner at Mr. Arnav's house")


# 7.sort function (irreversible in nature / permanent , used to arrange elements of list either in forward or reverse alphabetical order)


l = ['mazda','gtr','cayaenne','dbx','veyron']
print(l)
l.sort()
print(l)
l.sort(reverse=True) # note here reverse=true is wrong and reverse=True is right
print(l)


# 8.sorted function (same function as sort but it is not permanent)


l = ['mazda','gtr','cayaenne','dbx','veyron']
print(l)
print(sorted(l))
print(l)


# 9.reverse function (simply reverse the order of list)


l = ['mazda','gtr','cayaenne','dbx','veyron']
l.reverse()
print(l)


# 10.len function (used to find length / number of elements in the list)


l = ['mazda','gtr','cayaenne','dbx','veyron']
print(len(l))


# CHAPTER 4 (WORKING WITH LISTS)


# 1.using for loop (print each elements of list collectively)


niggas = ['Anirudh','Pragyan','Vansh']
for nigga in niggas:
    print (nigga)
# sources of error - either colon is not used or indentation is not given

reptiles = ['rats','rabbits','small birds','insects']
for reptile in reptiles :
    print (reptile.title(),"are Snake's prey !")
    print (reptile.title(),"are weak that's why they become his prey .",'\n')
# here \n is used to leave a line for beautification i.e. it was not necessary

magicians = ['alice','david','caroline'] 
for magician in magicians :
    print (magician,'that was a great trick .','\n')
print ('Thank you everyone for the show') # note that this line wasn't intended that's why loop didn't applied on this line it was executed after the for loop was executed .


# 2.range function


for value in range(1,5):
    print (value) # note only numbers from 1-4 are printed because of off-by-one behaviour of programming languages 
    
numbers = list (range(1,4))
print (numbers) # range can alse be used to print a list of numbers

ev_number = list(range(5,51,5)) # this value of range means that it will print numbers from 5-50 skipping 5 numbers each time i.e. it will write a table of five
for number in ev_number :
    print(number)

# Method 1
    
squares = []
for value in range (1,11) :
    square = value**2 
    squares.append(square)
print (squares)
# we took squares list empty and then we squred all the numbers from 1-10 and gave it a variable square and then we added those values to the empty list we initially took by using append function

# Method 2

squares = []
for square in range (1,11) :
    squares.append(square**2)
print(squares) # note if here the print was intended then it would print accoring to for function 

l = [1,2,3,4,5,6,7,8,9,0]
print(max(l))
print(min(l))
print(sum(l))

squares = [value**2 for value in range (1,11)]
print (squares)


# 3.slicing operator ()


goats = ['Pele','Maradona','Messi','Ronaldo']
print (goats[0:3]) # 0 represents the first element , [0,3] means [0,3) so 3rd element won't be printed
print (goats[:3]) # if not specified the starting element it will choose the first one by default
print (goats[3:]) # if not specified the ending element then by default it will choose the last one 
print (goats[-3:]) # -3 means numerically third element from last

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]: 
    print(player.title())   

# Method 1
    
alan_choice= ['sarah','kylie','scarlett','bella']
my_choice = ['megan','keiani','alaxandra']
print ("\nThe girls i don't like :",'\n',alan_choice)
print ('\n','My Gals :','\n',my_choice) # notice that when \n is used seperately then the print is perfect but in previous line when \n was used with the line then an extra space is created

# Method 2

alan_choice= ['sarah','kylie','scarlett','bella']
my_choice = ['megan','keiani','alaxandra']
print ('\n',"The girls i don't like :",'\n'+str(alan_choice))
print ('\n',"The Gals i like :",'\n'+str(my_choice))


# 4.copying a list


# Method 3

alan_choice= ['sarah','kylie','scarlett','bella']
my_choice = ['megan','keiani','alaxandra']
print ('\n',"The girls i don't like :",'\n',alan_choice[:]) # list[:] copies a list
print ('\n',"The Gals i like :",'\n',my_choice[:])


l = ['1','2','3','4','5']
print ('\n','The first three elements in the list are :','\n',l[:3])
print ('\n','The three elements from the middle of the list are :','\n',l[1:4])
print ('\n','The last three elements in the list are :','\n',l[2:69])

my_pizzas = ['Farmhouse pizza','Margherita pizza','BBQ Chicken pizza']
girlfriend_pizzas = my_pizzas[:]
my_pizzas.append('Pepproni Pizza')
girlfriend_pizzas.append('Mexican pizza')
my_pizzas.sort()
girlfriend_pizzas.sort()
del my_pizzas[1]
print ('\n',"My faivourite pizzas are :")
for my_pizza in my_pizzas :
    print ('\n',my_pizza.upper())
print ('\n',"My girlfriend's favourite pizzas are :")
for girlfriend_pizza in girlfriend_pizzas :
    print ('\n',girlfriend_pizza.upper())

print ("\nWelcome to Domino's")
print ("\nHere's the menu :")
l = ['Italian Pizza','mexIcAn pIzza','pePprOni pizza','tomaTo PiZZa','Chicken tandoori','FarmHouse piZZa','pizza burrata','Parmesan cheese pizza']
today_special = ['Mexican pizza','pepproni pizza']
today_special.append('Farmhouse pizza')
l.remove('Chicken tandoori')
l.sort()
today_special.sort()
for x in l :
    print ('\n',x.upper())
print ("\nToday's special :")
for y in today_special :
    print ('\n',y.upper())
print ("\nYour order is :")
order = l[:]
order[0] = ('Farmhouse pizza')
order[3] = ('Mexican pizza')
order[4] = ('Pepproni pizza')
order.remove('Farmhouse pizza')
order.remove('Mexican pizza')
order.remove('Pepproni pizza')
order.sort()
for pizza in order :
    print ('\n',pizza.upper())
print ('\nThank you for your business .')



# 5.tuples 

# A tuple is -

# 1.Immutable
# 2.Ordered
# 3.Heterogeneous
# 4.Indexed
     

l = (200,69)
print ('\nThe original dimensions are :')
for dimension in l :
    print (dimension,end=" ")
m = (100,200)
print ('\nModified dimensions are :')
for dimension in m :
    print (dimension,end=" ")


# CHAPTER 5 (IF STATEMENTS) note : if function is case sensitive
    

car = 'BMW'
car == 'BMW'   # double == is use to check whether the statement is true or not 
car == "Ferrari"

card = 'GTR'
card.lower() == 'gtr' # note commands without print are executed by shift enter after selecting the line you want to execute

# 1.If function

l=('arnav','pratap','singh')
for name in l :
    if name == 'arnav' :
     print ('\n',name.title(),end=" ") # end=" " it'll give the space in the end of the output and restricts the creation of new line
    else :
     print ('\n',name,end=" ")
    
# 2.using or to check multiple conditions

# in python there is no &&(logical AND) dor Logican and in python we use 'and' and for Bitwise and we use '&'
    
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) # True

# 3.checking whether a value is in a list

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings :
    print ('Mushrooms are available')
else :
    print ('Mushrooms are not available')

l=[1,2,3]
if 1 not in l : 
    print ('1 is not available')
else :
    print ('1 is available')

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 4.if-elif-else statements
    
# it is used for more than one conditions 
person = 'Brown'
if 'Black' in person :
    print ('You are a motherfucking nigga')
elif 'White' in person :
    print ('Go home milky your stepsis is stuck in the washing machine')
else :
    print ('You are perfect')
    
# instead of else , elif can also be used which would have been more accurate because then it would have been operated in a particular condition
    
alien_colour = ['green','yellow','red']
if 'green' in alien_colour :
    print ('Player just earned 5 points')
alien_colour = 'red'
if alien_colour ==' green' :
    print ('Player just earned 5 points') # this won't give any output

person = 3
if person<2 :
    print ('person is a baby')
elif person<4 :
    print ('person is a toddler')
elif person<13 :
    print ('person is a kid')
elif person<20 :
    print ('person is a teenager')
elif person<65 :
    print ('person an adult')
else :
    print ('person is an elder')

requested_toppings = []
if requested_toppings :
    for requested_topping in requested_toppings:
     print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

list = ['joseph','patric','admin','lucipher','nathan']
for name in list :
    if name is 'admin' :
        print ('Hello admin , would you like to see the status report?')
    else :
        print ('hello',name,',','thank you for logging in again.') 

current_users = ['pablo','johnathan','VeGeta','krillin','THUNDERBOLT']
new_users = ['VEGETA','nont','david','thunderbolt','nyran']
current_users_lower = [string.lower() for string in current_users] # to lowecase string of a list
new_users_lower = [string.lower() for string in new_users]
for user in new_users_lower:
    if user in current_users_lower :
        print ('\nsorry',user,'username is already taken .')
    else :
        print ('\n'+ user,', username is available .')


# CHAPTER 6 (DICTIONARIES) - It has a key-value pair and dictionary is enclosed with {}

# Dictionary key - 

# (1) Keys must be immutable data types . This means they cannot be changed after creation . Valid key types include -
# 1.Numbers (integers, floats, complex numbers)
# 2.Strings
# 3.Tuples (provided all elements within the tuple are also immutable)
# 4.Booleans
# 5.Frozensets

# (2) Keys must be unique . If you assign a value to an existing key, the old value will be overwritten.

# Dictionary value -

# (1) Values can be of any data type . This includes mutable types like lists and other dictionaries , as well as immutable types.
# (2) Values can be duplicated . Multiple keys can point to the same value.

# functions - 

# 1.    .keys()
# 2.    .values()
# 3.    .items() - used in looping                            Ex - for key,value in d.items():

alien_0 = {'colour':'green','points':'5'} # colour is a key and each key is assosiated to a value
print (alien_0['colour']) # green
print (alien_0['points']) # 5

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")

# 1.adding a key-value pair to a dictionary

l = {'colour':'green','points':5}
l['species'] = 'nigga type'
print(l)

alien = {'x_coordinates':0,'y_coordinates':0,'speed':'fast'}
print ('speed of alien is',(alien['speed']))
if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
elif alien['speed'] == 'fast':
    x_increment = 3
alien['x_coordinates'] = alien['x_coordinates'] + x_increment
print ('\nx coordinates:'+str(alien['x_coordinates']))
print ('\nthe current position of alien is :',str(alien['x_coordinates'])+','+str(alien['y_coordinates']))

# 2.to delete a key value pair

l = {'colour':'green','points':'5','species':'nigga'}
print(l)
del l['species']
print(l)

# 3.loop through key-value pair in a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key , value in my_dict.items(): # for looping in dictionaries in python .itms() is used note - key and value is variable and remember that comma is a must between the key and value variable
    print('\n'+key,':', value ,end=" ")
print()
# 4.loop through keys 
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for key in favorite_languages.keys() :# note even if you don't write .keys() the output would be same because Looping through the keys is actually the default behavior when looping through a dictionary
    print (key.upper())

# sorted function can also be used Ex - sorted(dictionary.keys()) 
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(sorted(favorite_languages.keys()))

# 5.loop through values 
    
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Set - It is a type of list in which element doesn't repeat just like in maths
    
l = {'phil':'python','jody':'javaScript','nile':'C#','ruby':'javaScript'}
print ('Languages considered are :')
for value in sorted(set(l.values())):
    print(value)

l = {'India':'Ganges','egypt':'nile','britain':'Thames'}
for country,river in l.items() :
    print ('The',river.title(),'runs through',country.title())
for river in l.values() :
    print (river.upper())
for country in l :
    print(country.upper())

# 6.nesting

# Sometimes you’ll want to store a set of dictionaries in a list or a list of items as a value in a dictionary. This is called nesting. You can nest a set of dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.
    
aliens = []
for alien_number in range (0,30) :
    new_alien = {'colour':'green','speed':'slow','points':'5'}
    aliens.append(new_alien)
for alien in aliens[:5] :
    print (alien)
print ('...')
print('Total number of aliens :',len(aliens))
for alien in aliens [:3] :
    if alien['colour'] == 'green' :
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
for alien in aliens [:5] :
    print(alien)
print('...')   
print ('Total number of aliens :',len(aliens)) 
for alien in aliens[3:13] :
    if alien['colour'] == 'green' :
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
for alien in aliens [:30] :
    print (alien)
print ('Total number of aliens :',len(aliens))

# A List in a Dictionary

pizza = {
'crust': 'thick',
'toppings': ['mushrooms', 'extra cheese']
}
print ('you ordered a '+pizza['crust'] +'-crust pizza','with the following toppings :')
for topping in pizza['toppings'] :
    print (topping)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    if len(languages) >1 :
        print("\n" + name.title() + "'s favorite languages are :")
    else :
        print("\n" + name.title() + "'s favorite language is :")
    for language in languages:
        print(language.title())

# A Dictionary in a Dictionary
        
users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
} , 
'mcurie': {
'first': 'marie',
'last': 'curie',
'location': 'paris',
}
}
for username, user_info in users.items():# in a (dict. in dict. format) username is for dict. 1 and 2 respectively
# and user_info is for values of dictionary 
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

pets = {
'michael':{
'species':'Dog' ,
'owner_name':'kylian'
} ,
'rupert':{
'species':'Parrot',
'owner_name':'Rebecca'
} , 
'franz':{
'species':'cat',
'owner_name':'Brock'
}
}
print ('\nDetails of pet :')
for name , info in pets.items() :
    print ('1.Name'+'\n'+name.upper())
    print ('2.Species :'+'\n'+info['species'].upper())
    print ('3.Owner name :'+'\n'+info['owner_name'].upper()) 


# CHAPTER 7 (USER INPUT AND WHILE LOOPS)
    
# done in diff. file

# CHAPTER 8 (FUNCTIONS)

# here we will use a function called def(define) which is used to define a fucntion
def greet_user() : # The parentheses hold that information. In this case, the name of the function is greet_user(),
# and it needs no information to do its job, so its parentheses are empty. (Even so, the parentheses are required.)
    """Display a simple greeting."""
# Note - """Display a simple greeting.""" is a comment called docstring and it describe what a function does and 
# docstring is enclosed in triple quotes which Python looks for when it generates documentation for the functions 
# in your programs.
    print('Hello!')
greet_user() # note this is called callng a function

# 1.Passing Information to a Function

def greet_user(username) : # here username is called a parameter
    """Display a simple greeting."""
    print ('Hello'+username.title()+'!')
greet_user('arnav') # the velue 'arnav' is called an argument

def display_message() :
    """This will display what you learnt in this chapter."""
    print('I learnt functions in this chapter.')
display_message()

def fav_book(title):
    """This will display favourite book."""
    print ('My favourite book is '+title)
fav_book('48 laws of power.')

# 2.positional arguments (When multiple parameters are required then positional arguments are used.)

def pet(species,name):
    """Will display info about pet"""
    print('I have a '+species.title()+'.')
    print('He goes by '+name.title()+'.')
pet('cat','murphy')
pet('dog','slim shady')

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet( pet_name='harry',animal_type='hamster') # by this we don't need to math order with parameter.

# 3.default value

# When writing a function, you can define a default value for each parameter. If an argument for a parameter is 
# provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value.

def pet_info(pet_name,specie='Dog'):
    """will display information about pet"""
    print('I own a',specie.title())
    print('My pet name is '+pet_name.title())
pet_info(pet_name='hank')

def pet_info(pet_name,specie='dog'):
    """will display information about pet"""
    print('I own a',specie.title())
    print('My',specie.title(),'name is '+pet_name.title())
pet_info(pet_name='hank',specie='cat') # here specie will be cat because argument was specified if it was empty then
# dog would've been displayed .

def pet_info(pet_name='hank',specie='python'):
    """will display information about pet"""
    print('I own a',specie.title())
    print('My pet name is '+pet_name.title())
pet_info('drake') # here only hank is written so it will be stored in pet_name due to positional argument therefore
# this time order is necessary.

def make_shirt(size,text) :
    """Will display size and text on the shirt"""
    print ('The size of shirt is : '+size.title())
    print ('Required message on shirt is : '+text.title())
make_shirt('m','i love India')

def make_shirt(size='large',message='i love python') :
    """Will display size and text on the shirt"""
    print ('The size of shirt is : '+size.title())
    print ('Required message on shirt is : '+message.title())
make_shirt()
make_shirt('medium')
make_shirt('small','programmer bolte')

# 4.return values

def formatted_name(first_name,middle_name,last_name):
    """Return a full name"""
    full_name = first_name+' '+middle_name+' '+last_name #This might seem like a lot of work to get a neatly formatted name when we could
# have just written:print("Arnav Pratap Singh") But when you consider working with a large program that needs to store many first and 
# last names separately, functions like get_formatted_name() become very useful. You store first and last names separately and then call 
# this function whenever you want to display a full name.
    return full_name.title()
name = formatted_name('arnav','pratap','singh')
print(name)

def formatted_name(first_name,last_name,middle_name=''):
    """return a full name"""
    if middle_name:
        full_name=first_name+' '+middle_name+' '+last_name
        return full_name.title()
    else :
        full_name=first_name+' '+last_name
        return full_name.title()
name= formatted_name('arnav','pratap','singh')
print(name)

# note- print() , len() , type() , range() are pre defined functions we call them in order to use.

# print()
# sep: str | None = " ", sep(seperator)
# =" " i.e. when we seperate two values by comma then automatically there will be space b/w them
# end: str | None = "\n", end(ending) = "\n" i.e. one line gap if we use print function again 
# we can manipulate print dunction

print ("Arnav pratap",end=" ") # here ending parameter = " " i.e. now there won't be one line gap instead there will be just a space
print("singh")

# len()

cities = ['delhi','gurgaon','noida','pune','mumbai','chennai']
heroes= ['luffy','naruto','icchigo','goku']
def print_len(list):
    print(len(list))
print_len(cities)
print_len(heroes) # this function will print length of a list

cities = ['delhi','gurgaon','noida','pune','mumbai','chennai']
print(cities[0],end=',')
print(cities[4]) # this will print 1st and 5th element of the list in same line

# function to print all the items of a list in a single line

def print_list(list):
    for items in list :
        print(items,end=' ')

l=['a','b','c','d']
print_list(l)

# to print factorial

def calc_factorial(n):
    fact=1
    for i in range(1,n+1) :
        fact*=i
    print(fact) # this won't be indented with for loop because we don't want to print fact
calc_factorial(5)

# for 1 USD = 83 INR  make a function which will convert USD to INR

def converter(USD_value):
    INR_value = USD_value*83
    print(USD_value,'USD =', INR_value,'INR')
converter(69)

def num_type(x):
    if int(x) % 2 == 0 :
        print(x,'is an EVEN number')
    else :
        print(x,'is an ODD number')
num_type(69)

# 5.recursion (function call itself repeatedly)

# these are same as loops every thing that can be done by can be dine by recursion and vice versa.

def show(n): # we will use recursion such that we wan to print n , n-1 , n-2 , ___ 1
    if (n==-1): # this condition is called base case.This will stop recursion at n=0
        return
    print(n)
    show(n-1)
show(5) # 5=n , 4=n-1 , 3=n-2 , 2=n-3 , 1

# call stack - every function is stacked as a layer in the memory so when we use return for a particular value then in the end we also 
# wrote print (something) then it will be printed the same number of times as thr values given by recursion for ex-

def show(n):
    if (n==-1):
        return
    print(n)
    show(n-1)
    print ('END')
show(3) # here END will be printed 4 times 

# n!=n*(n-1)! now very inportant we will need a base case here as factorial of -ve is undefined so we need the code to stop at 0

def build_person(first_name,last_name):
    person_info={'first':first_name,'last':last_name}
    return person_info
person = build_person('harry','maguire')
print(person)

def person_(first_n,last_n,age):
    info={'first':first_n,'last':last_n}
    if age :
        info['age']=age
    return info 
person=person_('Kylian','Mbappe',25)
print(person)

def factorial(n):
    if n==0 or n==1 :
        return 1
    return factorial(n-1)*n
print(factorial(5))

# first n natural numbers

def nos(n):
    if n==0 : # will stop at n=0
        return 0
    print(n,end=',')
    nos(n-1)
nos(5)

# sum of first n natural numbers

def sum(x):
    if x==0 : # will stop at n=0
        return 0
    return sum(x-1)+x
print(sum(5))

# print a particular element of a list

def elements(list,idx):
    if idx==len(list):
        return 
    print(list[idx].title())
    print(list[idx+1].title)
mc=['luffy','naruto','light','vegeta']
elements(mc,0)

# 6.storing function in a module
# a module is a file ending in .py that contains the code you want to import into your program.

# 7.File I/O in python
# python can be used to perform operations on a file.(read and write data)

# types of all files 
# 1.Text Files: .txt , .docx , .log , etc.
# 2.Binary Files: .mp4 , .mov , .png , .jpeg , etc.

# open read and close file
# f = open("file_name","mode")

# modes = r=read , w=write(overwrite i.e. all the data of file will be deleated then we can write in the file) ,
# a=append , x=new file , b=binary , t=text mode(by default function) , +=open a disk for updating 
# (reading and writing)
f=open("me.txt","r") # file_name,mode 
# note - if we didn't specified mode then python by default would've read the file 
data = f.read()# here we can also set some parameter like how many characters we want to read.
print(data)
print(type(data))
f.close()

f=open("me.txt","r")
data = f.read()
print(data)
line_1=f.readline()
print(line_1)
line_2=f.readline()
print(line_2) # after this a blank line will be printed because in the end pointer will read nothing.
f.close()                                                                                                                                                                                                                                                               

# writing a file
# 1st way - using "w" mode (write)
# 2nd way - using "a" mode (append)

f = open("demo.txt","w") # we are using "w" mode so the previous data will be overwritten
f.write("I am a react native developer")
f.close()

f = open("demo.txt","a")
f.write("\nThen I will move on to rust.")

# for reading and writing simultaneously 
# 1.r+
# note-this mode doesn't overwrite the file it will remove the words which will coincide with the one we are writing a code for

f = open("demo.txt","r+")
f.write("I am a programmer")
print(f.read())
f.close()

# to make a new txt file automatically

f = open("newfile.txt","w")
f.close()

# 2.w+ ( it will truncate the file)
f = open("newfile.txt","w+")
# this will wipe the file off
print(f.read()) # it'll read nothing
f.write("abc")
f.close()

# 3.a+ (it will append at the end of the file)
f = open("newfile.txt","a+")
f.write("def")
f.close()

#  With Syntax

with open("sample.txt","r") as f: # here f is an 'alias' 
# example of alias - Krish is an alias of Arnav and vice versa.
    data = f.read()
    print(data) # with syntax automatically closes the file.

with open("sample.txt","w") as f:
    f.write("new data.")

# deleting a file 
# file can be deleted by using a module called os(operating system)

# import os 
# os.remove("random.txt") # commenting this out because it'll delete the file so when we run other programs
# it'll throw error because no such file exists as it is deleted
# note - it is a preinstalled module.

# practise 

with open("practise.txt","w") as f:
    f.write("Hi everyone.\nWe are learning file I/O.\n")
    f.write("using Java.\nI like programming in Java.")

# replace Java with python in practise.txt

with open("practise.txt","r") as f:
    data = f.read()
new_data = data.replace("Java","python")
print(new_data)

# check whether the world "learning" is present in a file

word = "learning"
with open("practise.txt","r") as f:
    data=f.read()
    if (word in data):
        print("Found")
    else:
        print("Not Found")

# in which line learning occur first

def check_line():
    word = "learning"
    data = True
    line_number = 1
    with open("practise.txt","r") as f:
        while data :
            data = f.readline()
            if(word in data) :
                print(line_number)
                return
            line_number += 1
    return -1
check_line()

# PYTHON STRING FORMATTING
# done in string_formatting.py

# VIRTUAL ENVIRONMENT (to be done)

# A virtual environment in Python is an isolated workspace that lets you manage dependencies for a specific project without interfering with other projects or the system-wide Python installation.

# Imagine you’re working on two projects:

# Project A needs Django 3.2

# Project B needs Django 5.0

# If both are installed globally, they’ll conflict. A virtual environment solves this by keeping each project’s dependencies separate.

# python -m venv myenv       this will create a folder named myenv in the directory

# myenv\Scripts\activate      this will activate the virtual environment now every package installed goes to the environment

# typing deactivate will deactivate the virtual environment

# pip freeze        this command will gives list of all the packages installed on the environment 

# pip freeze > requirement.txt            this command will put all the list of packages in a .txt file

# pip install -r requirements.txt           to install the packages from a .txt file