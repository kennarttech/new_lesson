numbers = [2, 4, 1, 5, 4, 9,8]

fruits = ['mango', 'banana', 'orange', 'graps']

book_dic = {'titanic': 1987, 'the gods': 2010}

string_names = ('kenneth')

names_turple = ('less', 'more', 'many', 'much')

set_ = {'fruit', 'name', 'milk'}



# userPassword = ''

# while userPassword != 'secret':
#     userPassword = input('Type in your password: ')

# print('Access granted!')



for i in range(4):
    for j in range(10):
        if j == 5:
            print('loop end')
            break
        if i % 2 == 0:
            continue
        print(i, j)



def ask_ok(prompt, retries=4, reminder='Please try again: '):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries > 0:
            raise ValueError('Invalid user respond')
        print(reminder)
        

ask_ok('Do you realy want to Quit: ')
ask_ok('Ok to overide the file: ')
ask_ok('Ok to overide the file: ','come on', 'only yes or no')



def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))




user_number = int(input('Please enter your number: '))

for count in range(1, 11):
    result = user_number * count
    print(user_number, '*', count, '=', result)


# Example 1
# ======use sum in calculation instead of for loop====
numbers = [10, 20, 33, 40, 11]

repo = 0

for i in numbers:
    repo += i
print(repo)
# ==================Ending=============


# ========Instead of for loop use Sum===✔️
result = sum(numbers)
print(result)
# =========Ending===================



# =======Instead of using for loop for iteration use enumerate====
numbers = [10, 20, 33, 40, 11]

for idx in range(len(numbers)):
    print(idx, numbers[idx])
# ==================Ending============================



# ===========Use enumerate instead of len====✔️
for inx, val in enumerate(numbers, start=1):
    print(inx, val)
# ===========Ending========================


# ======Instead of len fun use Zip function=====
a = [1,2,3]
a = [1,2,3, 4]
b = ['a', 'b', 'c']

for ind in range(len(a)):
    print(a[ind], b[ind])
# ==========Ending=================


# =============Use Zip function==========
a = [1,2,3, 4]
b = ['a', 'b', 'c']

for val1, val2 in zip(a, b, strict=False):
    print(val1, val2)
# =============Ending===================


# =================Checking how many time we learn=====
events = [('learn', 5), ('learn', 10), ('relaxed', 20)]

counter = False

for event in events:
    if event[0] == 'learn':
        counter += event[1]
print(counter)
# # ==============Ending=====================


# =======================================
empty = []

xa = int(input('Please enter your value: '))

for x in range(32):
    empty.append(x ** xa)
    print(empty)
# ======================================


# =================Start==================
count = 0

for i in range(1, 8):
    if i % 3 == 0:
        count += i
print(count)
# print(count, end='')
print('')
# ==============end========================


# ==================Start==============
for i in range(4):
    for m in range(1, 10):
        print(m, end="")
    print()
else:
    print('loop execute successfuly')
# =====================================


# =============Start
grocery_list = ['mango', 'pawpaw', 'banana', str(7)]

for g in grocery_list:
    for m in g:
        print(m, end='')
    print('')
# =============End===================


# ======================
total_gpa = int(input('How many GPA do you have: '))

grades = []

for i in range(0, total_gpa):
    grade = float(input('Please Enter your grade: '))
    grades.append(grade)
    print(grades)
print()
print('Your grades are ')
for i in range(0, total_gpa):
    print(grades[i])
    
print('That is all')
# ==============================


# ======================For loop============
row = int(input('Enter the number of rows: '))
colums = int(input('Enter the number of columns: '))
symbol = input('ENter a symbol to use: ')

for x in range(row):
    for y in range(colums):
        print(symbol, end='')
    print()
    