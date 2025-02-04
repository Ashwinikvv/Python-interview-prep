#By Using Multiple Dispatch Decorator 

#Multiple Dispatch Decorator Can be installed by: 

#pip3 install multipledispatch
'''https://www.geeksforgeeks.org/python-method-overloading/
6
12
17.985999999999997
In Backend, Dispatcher creates an object which stores different implementation and on runtime, it selects the appropriate method as the type and number of parameters passed.'''






from multipledispatch import dispatch

# passing one parameter


@dispatch(int, int)
def product(first, second):
    result = first*second
    print(result)

# passing two parameters


@dispatch(int, int, int)
def product(first, second, third):
    result = first * second * third
    print(result)

# you can also pass data type of any value as per requirement


@dispatch(float, float, float)
def product(first, second, third):
    result = first * second * third
    print(result)


# calling product method with 2 arguments
product(2, 3)  # this will give output of 6

# calling product method with 3 arguments but all int
product(2, 3, 2)  # this will give output of 12

# calling product method with 3 arguments but all float
product(2.2, 3.4, 2.3)  # this will give output of 17.985999999999997
