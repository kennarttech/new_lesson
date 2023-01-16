from typing import List, Tuple, Set, Dict



class Book():
    pass



class BookShelf():
    def __init__(self, books: List[Book]) -> None:
        self.books = books 


    def __str__(self) -> str:
        return f"BookShelf with ({len(self.books)} books"




def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)








mm = list_avg([33, 33])
print(mm)