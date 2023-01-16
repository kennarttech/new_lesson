rr = 55
mm = 55

print(rr == mm)
print(rr > mm)
print(rr != mm)
print(rr is mm)#this checks if the element has the same thing not having the same thing
print()


for i in range(5):
    for j in range(4):
        for m in range(4-i):
            print('😀', end='')
    print()


#=========This add the value in the list by each itration======
list1 = [2, 5, 6]
list2 = [4, 3, 5]
result = []


for i in list1:
    for j in list2:
        result.append(i+j)
print(result)
# ================The End========================



# ========Multiplying==========
list2 = [2,4,6]
list3 = [2,4,6]
for i in list2:
    for j in list3:
        if i == j:
            continue
        print(i, '😀', j, '= ', i*j)

# =====================End=======
a = 1
while a < 100:
    count = 0
    for i in range(1, a):
        if a % i == 0:
            count += i
    if count == a:
        print('Perfect number:', a)
    a += 1
# ============End===============

row = int(input('Enter the number of rows: '))
colums = int(input('Enter the number of columns: '))
symbol = input('ENter a symbol to use: ')

for x in range(row):
    for y in range(colums):
        print(symbol, end='')
    print()