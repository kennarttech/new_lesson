def greet(name, name_friend=True) -> str:
    if name_friend:
        return 'Hello ' + name + '! Welcome to my app'
    return 'Go away ' + name




def greet_all(people) -> str:
    for person in people:
        per = greet(person)
        visit = tour(person)
        return visit, per



import random

def tour(visit):
    print("How may we help you?")
    user = input('Please tell us:😀) ')
    if visit:
        print(f'Ok thats great {random.randint(2, 8)}we will do that ' + user)
    else:
        return user





print("**=== Welcome to kennart tech ===**")
user_name = input('Please input your name ')

people_to_greet = [user_name]
greet_all(people_to_greet)









