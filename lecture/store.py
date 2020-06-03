# define a store using oop principles

class Store:
    def __init__(self, name, departments):
        self.name = name
        # departments will be a list of strings
        self.departments = self.init_departments(departments)
    
    def __str__(self):
        # this will print out the name of the store
        # as well as any departments that the store has
        output = f"{self.name}\n"
        for d in self.departments:
            output += " id:" + str(d.get_id()) + ", name:" + d.get_name() + "\n"
        return output
    # Take in a string of department names and returns a list of Department instances
    def init_departments(self, departments):
        instances = []
        for i, d in enumerate(departments):
            instances.append(Department(i + 1, d))
        return instances
        


class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'Department {self.id}: {self.name}'

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name



# add a way for a user to select departments
#selection = input("Select a department number. ")
#print(f'You selected {selection}')

departments = [ 
    "Running",
    "Fishing",
    "Baseball",
    "BasketBall"
]
my_store = Store("The Dugout", departments)

print(my_store)

selection = int(input("Select a department number: "))
print(f"You selected Department {selection}, {my_store.departments[selection-1].get_name()}")

# Let's add a more streamlined way to add Departments to our store
# Let's add a method on the Department class that will take in a list of Strings
# Representing Department names, and create the department instances for us.