# Object orination {rogramming concept define the methods }
# simple Program for Booking the fLIGHT obrations
# define a Object and Its Methods Properties and use it in the conditions  we have 

class Plan():
    def __init__(self, capicaty):
        self.capicaty=capicaty
        self.passange=[]
        
    def add_passanger(self, name):
        if not self.open_seat():
            return False
        self.passange.append(name)
        return True

    def open_seat(self):
        return self.capicaty - len(self.passange)
    # thera are 3 seats in Plane
flight=Plan(3)          

people=["Hassan","hamza","Sammer","Ammer"]
for person in people:
    success=flight.add_passanger(person)
    if success:
        print(f"Added  {person} to flifgt successfuly ")
    else:
        print(f"No Avalabe seats for {person}")    