# Functions in Python:

def greeting_fn(name):
    print(f"Welcome! {name.strip().title()}");

greeting_fn("ayush dutta");
greeting_fn("       sarah williams         ");

# default parameters:
def greet(name="ayush dutta"):
    print(f"hello, {name.strip().title()}");

greet("Rohini Sharma");

# fn to square num:
def square(num):
    return num**2;

print(square(5));

sum = lambda a,b: a+b;
print(f"Sum of a and b: {sum(5,7)}");

# kwargs
def data(name, address, id):
    print(f"My name is {name.strip().title()}, address is {address}, and id is {id}");

data(id=12345, name="ayush dutta", address="55-A Colony");