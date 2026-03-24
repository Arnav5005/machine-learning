a = (input("Enter the number :")) # here we can't use int we have to use in in print because if we enter a word instead of a number then an error will be there because a word can't be converted into an integer
print(f"Multiplication table of {a} is :")
try :
    for i in range (1,11) :
        print(f"{int(a)} X {i} = {int(a)*i}") # try means try whether the code can be executed and if it can then it will be executed and if it doesn't then it will be an exception .
except:
    print("Invalid Input")
print("End of program")

# note - we can use multiple excepts for different types of errors

try :
    a = int(input("Enter index"))
    num = [6,9]
    print(num[a])
except ValueError: # value error means wrong value such as "fsfhsy" this is invalid
    print("Number entered is not an integer")
except IndexError: # index error - this list has only two elements so we can only give input as 0 and 1 
    print("Index Error")
print("End of program")

# Finally 

try :
    a = int(input("Enter a number :"))
    l = [3,6,2,9,1,0]
    print(l[a])
except :
    print("some error occured")
finally:
    print('I am always executed')

# advantage of finally over print 

# Ques - even if error occured print also executed if it is not indented so why do we use finally if we just want to print things which can be executed by using print function ?

# Ans - finally function helps while we are defining a function like if we use return before print then print won't be executed but instead of print if we are using finally then it will be executed.

def func():
    try :
        a = int(input("Enter a number :"))
        l = [3,6,2,9,1,0]
        print(l[a])
        return 1 # if 1 is printed i.e. it was executed.
    except :
        print("some error occured")
        return 0  # if 0 is printed i.e. it is not executed due to some error.
    finally:
        print('I am always executed')
x = func()
print (x)