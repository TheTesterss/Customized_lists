
# ? Imports
from File import File
from Pile import Pile
import random

""" Show the list """
def show(list):
    # * print(list.isEmpty())
    # * print(list.Length())
    list.Show()

""" Build a list depending from the classe """
def build(Classe):
    list = Classe()
    show(list)
    for i in range(15):
        list.Insert(random.randint(0, 100))
    show(list)
    for i in range(5):
    list.Remove()
    show(list)

    print(list.At(random.randint(0, 10)))

build(File)
print()
build(Pile)
