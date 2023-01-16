class Kennart():
    """the underscore is a magic method that get call by default"""
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


    def __str__(self) -> str:
        """The __str__ returns a string or turning ur object into a string"""
        return f'Person {self.name}, {self.age} years old.'

    
    def __repr__(self) -> str:
        """This also return string and also use in debuger method"""
        return f'<Person({self.name}, {self.age})>'





    
bob = Kennart('Ben', 22)
print(bob)
bob.__repr__
# print(Kennart.__doc__)
