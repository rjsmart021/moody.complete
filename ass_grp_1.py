#mood_responses.py
def mood_response(mood):
    return "I am feeling " + mood

#main.py
import mood_responses
mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

#2. Exploring Python Modules and Data Structures Assignment
#Task 1: Contact List Manager
# contacts_manager.py
# Define functions to add, remove, and display contacts
contacts = []
def add(contact):
    contacts.append(contact)

def remove(contact):
    contacts.remove(contact)

def display():
    for contact in contacts:
        print(contact)

# main.py
# Implement the logic to interact with the contact manager

#3. Mastering Python Modules and Aliases
#Task 1: Custom Module with Aliases
# text_utils.py
def reverse_string(s):
    # function to reverse a string
    r_s = ""
    for i in range(len(s)-1, -1, -1):
        r_s += s[i]
    
    return r_s

def capitalize_string(s):
    # function to capitalize a string
    return s.upper()
    
#3. Mastering Python Modules and Aliases
# text_utils.py
def reverse_string(s):
    # function to reverse a string
    r_s = ""
    for i in range(len(s)-1, -1, -1):
        r_s += s[i]
    
    return r_s

def capitalize_string(s):
    # function to capitalize a string
    return s.upper()

# main.py
import text_utils as tu
print(tu.reverse_string("Take"))
print(tu.capitalize_string("Take"))

#Lesson 2: Assignment | OOP Fundamentals
#1. City Infrastructure Management System
class Vehicle:
    def __init__(self, r,t,o):
        self.registration_number = r
        self.vehicle_type = t
        self.owner = o

    def update_owner(self, new_owner):
        self.owner = new_owner
    
# main.py
import Vehicle as veh
vehicle1 = veh("TDS-2154", "Sedan", "Jack Smith")
vehicle2 = veh("EBN-1234", "Truck", "John Doe")
vehicle3 = veh("GAR-1040", "SUV", "Jane Doe")

vehicle1.update_owner("Reggie")
vehicle2.update_owner("Miller")
vehicle1.update_owner("Kevin")

#Task 2: Event Management System Enhancement

class Event:
    def __init__(self, name, date, num_participants):
        self.name = name
        self.date = date
        self.num_participants = num_participants

    def add_participant(self):
        self.num_participants += 1
        
    def get_participant_count(self):
        return self.num_participants
    
#2. Python City Planning Simulator
#Task 1: File Handling for Building Records

class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
# Methods to save to file and load from file
    def save_to_file(file_path, buildings):
        with open(file_path, 'w') as file:
            file.writelines('Building name, Floors\n')
            for i in buildings:
                file.writelines('%s, %s\n' % (i.name, (str(i.floors))))

        file.close()

    def load_from_file(file_path):
        with open(file_path, 'r') as file:
            buildings = file.read()
            return buildings
        file.close()

#main.py
import Building as bdg

building1 = bdg("Trump Tower", 55)
building2 = bdg("Empire State", 48)
building3 = bdg("Westin, ATL", 72)
buildings = []
buildings.append(building1)
buildings.append(building2)
buildings.append(building3)
bdg.save_to_file("city.txt", buildings)
buildings = bdg.load_from_file(file_path = "city.txt")
print(buildings)

#3. City Services Simulation: Python OOP and Modular Design
#Task 1: Public Transportation Module
#transportation.py
class Bus:
    #class variables
    city_name = input("Enter city name! ")
    base_fare = input("Enter base fare! ")

    def __init__(self, route_num, pass_capacity):
        #instance variables
        self.route_num = route_num
        self.pass_capacity = pass_capacity

    def info_summary(self):
        print("City:", self.city_name)
        print("Base Fare:", self.base_fare)
        print("Route Number:", self.route_num)
        print("Passenger Capacity:", self.pass_capacity)

#main.py
#bus instances
bus1 = Bus(route_num="1", pass_capacity=51)
bus2 = Bus(route_num="2", pass_capacity=44)
bus3 = Bus(route_num="3", pass_capacity=30)


print("Bus 1 Info:")
bus1.info_summary()
print("Bus 2 Info:")
bus2.info_summary()

#Lesson 3: Assignments: OOP Principles
#1. Encapsulation in Personal Budget Management
#Task 1: Define Budget Category Class

class BudgetCategory:
    
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.remaining_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category_name(self, category_name):
        if category_name.isalpha:
            self.__category_name = category_name

    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget

    #Task 3: Add Budget Functionality
    def add_expense(self, amount):
        if amount > 0:
            self.remaining_budget -= amount

    #Task 4: Display Budget Details
    def display_category_summary(self):
        # Method to display the budget category details
        print("Name of Budget Category: ", self.get_category_name())
        print("Allocated Budget: ", self.get_allocated_budget())
        print("Remaining Budget After Expense: ", self.remaining_budget)

#main.py
import BudgetCategory

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()