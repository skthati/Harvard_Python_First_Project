# Harvard_Python_First_Project


Harvard Course CS50W | Python class notes and exercises.

<hr>

## Conditions.
Self explainatory 
```
val = input("Enter the Number:")

# To get index value of input
print(val[0]) # Gets first index value.

print(val[1]) # Gets second index value.
```

# lists
Sequence of mutable values

`names = ["Sandeep", "Kumar", "Auckland"]`

To append a value to list

`names.append = 39`


# Tuple
Sequence of immutable values

`coordinate = (10.0, 20.0)`

# Set
Collection of unique values. unordered. No element ever appears more than once. Even if the set has multiple duplicates, output will be unique values.

To create empty set.

`s = set()`

To add elements to set

`s.add("test")` 

To remove value from set.

`s.remove("test")


# Dict
Collection of key-value pairs

```
names = {
    "f_name" = "Sandeep",
    "l_name" = "Kumar",
    "age" = 38
}
```

# len

len is to calculate the length of an element.

`len(s)`

# loops

`for i in range(5)`

## range
range(5) counts from 0 to 4.

# functions

Function definition
```Python
def square(a)
{
    return a**
}
```

Function instance

`square(a)`

# Classes

```Python
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(3, 5)

print(p.x, p.y)
```

Another example using classes to check flight availability and add passengers

```Python
class Flights():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    
    def add_passenger(self, name):
        if not self.check_availability():
            print(f"There are no seats for {name}")
        else:
            print(f"{name} has successfully allocated seat.")
        return self.passengers.append(name)

    
    def check_availability(self):
        return self.capacity - len(self.passengers)
    
 
flight = Flights(3)

names = ["Alfa", "Tango", "Victor", "Charlie"]  

for name in names:
    flight.add_passenger(name)
    
```

# Decorators
Decorators are functions which take function as input and give a modified version of that function.

Also called as Functional programming.

```Python
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("End of the function")
    return wrapper

@announce
def hello():
    print("Hello World")

hello()
```

# lambda


```Python
people = [
    {"name": "Alpha", "house": "Auckland"},
    {"name": "Bravo", "house": "Wellington"},
    {"name": "Charlie", "house": "Taupo"}
]
 
# people.sort() # will get an error

def f(person):
    return person["name"] # Or you can use also "house"

people.sort(key=f)

print(people)
```

We can change all of this above lines simply by using lambda expression
```Python
people.sort(key=lambda person: person["name"]) # Or use "house"
```

# Exceptions

```Python
import sys  
x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.)
    sys.exit(1)

print(f"{x} / {y} = {result}")
```


 