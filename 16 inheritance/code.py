class Device():
    def __init__(self, name, connected_by) -> None:
        self.name = name 
        self.connected_by = connected_by
        self.connected = True



    def __str__(self) -> str:
        return f"Device {self.name} {self.connected_by}"



    def disconnect(self):
        self.connected = False
        print('Disconnected.')

from collections import Counter

class Printer(Device):
    """This printer class inherit from Device class with some attribut"""
    def __init__(self, name, connected_by, remaining_pages) -> None:
        super().__init__(name, connected_by)
        # self.capacity = capacity
        self.remaining_pages = remaining_pages



    def __str__(self) -> str:
        # return super().__str__()(self.remaining_pages)
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"



    def print(self, pages):
        """this is responsible for our printing"""
        if not self.connected:
            print('Your printer is not connected!')
            return 
        print(f"Printing {pages} pages")
        self.remaining_pages -= pages




printer = Printer('Printer', 'USB', 500)
printer.print(200)

print(printer)

# printer.disconnect()
# printer.print(30)