# #################################################### #
#                       Pile                           #
# #################################################### #

# ? Imports
from Cellule import Cellule

class Pile:
    __length: int
    __start: Cellule
    
    # ? CONSTRUCTOR
    
    """ Construct the default values. """
    def __init__(self):
        self.__length = 0
        self.__start = None
    
    """ Inserts any type of value at the beginning of the list """
    def Insert(self, value: any):
        cellule = Cellule(value)
        
        if self.isEmpty():
            cellule.setNext(None)
        else:
            cellule.setNext(self.__start)
        
        self.__start = cellule
        self.__length += 1
    
    """ Removes the value at the beginning of the list """
    def Remove(self):
        assert self.isEmpty() == False, "List empty."
        self.__start = self.__start.getNext()
        self.__length -= 1
    
    """ Returns the length of the list"""
    def Length(self) -> int:
        return self.__length
    
    """ Checks if the list is empty or not """
    def isEmpty(self) -> bool:
        return self.__length == 0
        # * Or "return not self.__start"
    
    """ Prints the list as a python list's format"""
    def Show(self):
        if self.isEmpty():
            return print("[]")
        
        print("[", end="")
        v = self.__start
        for i in range(self.__length - 1):
            print(f"{v.getValue()},", end="")
            v = v.getNext()
        print(f"{v.getValue()}]")
    
    """ Returns the value at a specific position """
    def At(self, position):
        assert self.isEmpty() == False, "List empty"
        assert self.Length() >= position, "Out of range"
        
        v = self.__start
        for i in range(position):
            v  = v.getNext()
        return v.getValue()