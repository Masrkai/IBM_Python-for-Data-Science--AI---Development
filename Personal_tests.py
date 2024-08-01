# %%
try:
    import matplotlib.pyplot as plt
    print("module 'matplotlib' is installed")
except ModuleNotFoundError:
    print("module 'matplotlib' is not installed")

class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)

    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()

# %%\
class Rectangle(object):
    
    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height 
        self.width = width
        self.color = color
    
    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height ,fc=self.color))
        plt.axis('scaled')
        plt.show()
# %%\

RedCircle = Circle(10, 'red')

print('Radius of object:',RedCircle.radius)
RedCircle.add_radius(2)
print('Radius of object of after applying the method add_radius(2):',RedCircle.radius)
RedCircle.add_radius(5)
print('Radius of object of after applying the method add_radius(5):',RedCircle.radius)

RedCircle.drawCircle()
# %%


SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
SkinnyBlueRectangle.drawRectangle()
# %%

FatYellowRectangle = Rectangle(20, 5, 'yellow')
FatYellowRectangle.drawRectangle()
# %%

class Vehicle:
    color = "white"

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None

    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def display_properties(self):
        print("Properties of the Vehicle:")
        print("Color:", self.color)
        print("Maximum Speed:", self.max_speed)
        print("Mileage:", self.mileage)
        print("Seating Capacity:", self.seating_capacity)

# Creating objects of the Vehicle class
vehicle1 = Vehicle(200, 20)
vehicle1.assign_seating_capacity(5)
vehicle1.display_properties()

vehicle2 = Vehicle(180, 25)
vehicle2.assign_seating_capacity(4)
vehicle2.display_properties()
# %%
class Graph():
    def __init__(self, id):
        self.id = id
        self.id = 80


val = Graph(200)
print(val.id)

# %%
for num in range(1, 6):
    if num == 3:
        break
    print(num)
# %%
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
# %%
count = 0
while count < 5:
    print(count) 
    count += 1
# %%
x = "Go"
if x == "Go":
    print('Go')
else:
    print('Stop')
print('Mike')
# %%
x = 1
x = x > -5
# %%
x = 5
while x != 2:
    print(x)
    x = x - 1
# %%
class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p1 = Points("A", "B")
p1.print_point()
# %%
for i, x in enumerate(['A', 'B', 'C']):
    print(i + 1, x)
# %%
class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p2 = Points(1, 2)
p2.x = 'A'
p2.print_point()
# %%
a = 1
def do(x):
    a = 100
    return x + a


print(do(1))
# %%
import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# %%
