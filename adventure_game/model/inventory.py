from . import *

class Inventory():
    def __init__(self):

        self.capacity = 10
        self.contents = ["Heineken ", "Carlsberg"]

    def remove_item(self, index):
        temp = self.contents[index - 1]
        del self.contents[index - 1]
        return "Removed " + temp + " Succesfully!"


    def add_item(self, item):
        if len(self.contents) < self.capacity:
            self.contents.append(item)
            return item + " succefully added to inventory"

        elif len(self.contents) >= self.capacity:
            return "Your inventory is full"

    def view(self):
        return self.contents