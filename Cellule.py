# #################################################### #
#                       Cellule                        #
# #################################################### #

class Cellule:
    
    # ? CONSTRUCTOR
    
    """ Construct the default values. """
    def __init__(self, value = None):
        self.__value = value
        self.__next = None
    
    # ? Setters
    
    """ Sets cellule's value """
    def setValue(self, value):
        self.__value = value
    
    """ Sets the next cellule to still have pointers on it """
    def setNext(self, next):
        self.__next = next
    
    # ? Getters
    
    """ Returns the current cellule value """
    def getValue(self):
        return self.__value
    
    """ Returns the next cellule that follows this one """
    def getNext(self):
        return self.__next