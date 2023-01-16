def number(n):
    """This function perfomed calculation"""
    if n % 2 == 0:
        print('This is even number')
    else:
        print('This is odd number')



def new_number(mm) -> int:
    """This function perform logical calculation"""
    global even
    # nonlocal
    even = []
    for i in mm:
        if i % 2 == 0:
            even.append(i)
    return even

    

def arithmetic(num1, numb2):
    """==This function return multiple value =="""
    add = num1 + numb2
    sub = num1 - numb2
    multiply = num1 * numb2
    division = num1 // numb2
    return add, sub, multiply, division



def fucn(jj):
    total = sum(even + jj)
    return total




def lamb_func():
    """This program check for even numbers"""
    l = [3, 1, 4, 6, 2, 6]
    even_no = list(filter(lambda x: x % 2 == 0, l))
    return even_no





solution = new_number([2, 3, 42, 51, 62, 70])
print(f'Even numbers are -{solution}')

print(arithmetic(14, 12))

print(lamb_func())

print(fucn([3]))
# print(number.__doc__)



def greet(name, be_nice=True):  
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name



def greet_all(people):
    for person in people:
        print(greet(person)) #because it returns string


people_to_greet = ["Johnny", "Jacob"]
greet_all(people_to_greet)