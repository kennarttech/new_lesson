
# ============Destructuring_variables==============
x, y = (4,5)
aa = x,y
print(aa)
# ======================

print()

# =================Example2================
student_attedance = {'Kenn':99, 'Bob': 60, 'Steven': 90}

for i, attendance in student_attedance.items():
    print(f'{i}:, {attendance}')
# ===================End====================

print()

# ====================Example 3=======================
people = [('Bob', 44, 'Mechanic'), ('Mecha', 89, 'Artist'), ('James', 76, 'Lecturer')]

for name, age, profession in people:
    print(f'Name: {name}, Age: {age}, Profesion: {profession}')
# ======================End============================

print()

# ======================Example 4=====================
person = ('bob',44, "Mechanic")

name, _, profession = person

print(name, profession)
# ====================End==================

print()

# =====================Example 5================
head, *tail = [2,3,1,4, 54]
print(head, tail)
