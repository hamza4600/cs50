# we want our program to handel the errs that often happen in the Programs what to do if they happen 

# a simple program that will divide the Numbers with each other

# as we know that if we divide  with any Number it will show erro so we want display this in a Message as a user doe,s that
import sys
# similarly we can modify our program if a user enter a String occurs an erro
def divid():
    try:
        x=int(input("x: ")) 
        y=int(input("y: "))
    except ValueError:
        print("Please Enter the NUmbers NOt Strings")
        sys.exit(1)
    try:
        result=x/y
    except ZeroDivisionError:
        print("Error : can,t divide with Zero ")
        sys.exit(1)
    print(f"The {x}/{y} answer is {result}")

divid()     
# if we don,t use that it will crash the Program entierly