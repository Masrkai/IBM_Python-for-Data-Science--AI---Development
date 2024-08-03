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
import numpy as np
import pandas as pd
import lxml


# You can also use this section to suppress warnings generated by your code:
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')


URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"


# Extract tables from webpage using Pandas. Retain table number 3 as the required dataframe.
tables = pd.read_html(URL)
df = tables[3]

# Replace the column headers with column numbers
df.columns = range(df.shape[1])

# Retain columns with index 0 and 2 (name of country and value of GDP quoted by IMF)
df = df[[0,2]]

# Retain the Rows with index 1 to 10, indicating the top 10 economies of the world.
df = df.iloc[1:11,:]

# Assign column names as "Country" and "GDP (Million USD)"
df.columns = ['Country','GDP (Million USD)']

# Change the data type of the 'GDP (Million USD)' column to integer. Use astype() method.
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int)

# Convert the GDP value in Million USD to Billion USD
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000

# Use numpy.round() method to round the value to 2 decimal places.
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2)

# Rename the column header from 'GDP (Million USD)' to 'GDP (Billion USD)'
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'})

df.to_csv('./Largest_economies.csv')
# %%
import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage you want to scrape
url = 'https://en.wikipedia.org/wiki/IBM'

# Send an HTTP GET request to the webpage
response = requests.get(url)

# Store the HTML content in a variable
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Display a snippet of the HTML content
print(html_content[:500])

# Find all <a> tags (anchor tags) in the HTML
links = soup.find_all('a')
# Iterate through the list of links and print their text
for link in links:
     print(link.text)
# %%
import os
import requests
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

r.status_code
print(r.request.headers)

print("request body:", r.request.body)

header=r.headers
print(r.headers)
header['date']
header['Content-Type']

r.encoding
r.text[0:100]

url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r=requests.get(url)
print(r.headers)
r.headers['Content-Type']

path=os.path.join(os.getcwd(),'image.png')

with open(path,'wb') as f:
    f.write(r.content)

Image.open(path)

# %%
import os
import requests
from PIL import Image
from IPython.display import IFrame

url_get='http://httpbin.org/get'
#A query string is a part of a uniform resource locator (URL), this sends other information to the web server. The start of the query is a ?, followed by a series of parameter and value pairs, as shown in the table below. The first parameter name is name and the value is Joseph. The second parameter name is ID and the Value is 123. Each pair, parameter, and value is separated by an equals sign, =. The series of pairs is separated by the ampersand &.

#To create a Query string, add a dictionary. The keys are the parameter names and the values are the value of the Query string.

payload={"name":"Joseph","ID":"123"}
#Then passing the dictionary payload to the params parameter of the  get() function:

r=requests.get(url_get,params=payload)
#We can print out the URL and see the name and values.

r.url
#There is no request body.

print("request body:", r.request.body)
#We can print out the status code.

print(r.status_code)
#We can view the response as text:

print(r.text)
#We can look at the 'Content-Type'.

r.headers['Content-Type']
#As the content 'Content-Type' is in the JSON format we can use the method json(), it returns a Python dict:

r.json()
#The key args has the name and values:

r.json()['args']
#Post Requests
#Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:

url_post='http://httpbin.org/post'
#This endpoint will expect data as a file or as a form. A form is convenient way to configure an HTTP request to send data to a server.

#To make a POST request we use the post() function, the variable payload is passed to the parameter  data :

r_post=requests.post(url_post,data=payload)
#Comparing the URL from the response object of the GET and POST request we see the POST request has no name or value pairs.

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)
#We can compare the POST and GET request body, we see only the POST request has a body:

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)
#We can view the form as well:

r_post.json()['form']
#There is a lot more you can do. Check out Requests for more.

# %%
