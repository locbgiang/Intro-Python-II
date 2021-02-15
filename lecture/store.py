class Store:
    def __init__(self, name, departments):
        self.name = name
        self.departments = self.init_departments(departments)
    def __str__(self):
        output = f"{self.name}\n"
        print('self.department is', self.departments)
        for d in self.departments:
            output += " id:" + str(d.get_id()) + ", name:" + d.get_name() + "\n"
        return output
    def init_departments(self, departments):
        instances = []
        for i, d in enumerate(departments):
            instances.append(Department(i+1, d))
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