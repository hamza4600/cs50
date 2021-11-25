# Creat a function  that will modify another functions   this is called decurator  
# fucntions then self are values they can modify each other 
def announce(f):
    def wrapper():
        print("About to run the functin....") 
        f()
        print("Done with the function.")
    return wrapper
# another functon that will wrap the decurator with the hel fucntion 
@announce
def hel():
    print("Hello world")
    
hel()    
    #it provides us the Power that we can take a function and modify it at anytime we want  
    
    # Pyhton gives us the Power that we can Nest the Data structure as we want in each other List in the Dict and Dict iin the Tuple 
    
    # Another Example of Lambda 
people=[
    {"name": "hamza","city":"karachi"},
    {"name": "ali","city":"LAHORE"},
    {"name": "dany","city":"pakati"}
]     


# we want to sort the   list  But Python don,t knows that we have to define the way in a fuction
def d(person):
    return person["name"]
    
    # now the answer will be the sorted as we have 
    # now we will defin inthe lambda way  lambda is a complete function 
people.sort(key=lambda person:person["city"])    
people.sort(key=d)
print(people)
# print(qa)