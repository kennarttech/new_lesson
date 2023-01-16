class NameNotFound(ValueError):
    pass


def search(sequence, expected, finder):
    try:
        for elem in sequence:
            if finder(elem) == expected:
                return elem
    except:
        print(f'Your search did not match any any name {expected}')





friends = [
    {"name": "smith", "age": 22},
    {"name": "adam", "age": 20},
    {"name": "jane", "age": 18}


]


def get_friend_name(friend):
    return friend['name']



user_input = input('Please enter the to search: ').lower()
result = search(friends, user_input, get_friend_name)

print(f"Search finished, found {result} matching the search query")
