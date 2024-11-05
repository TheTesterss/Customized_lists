
# ? Imports
from File import File
from Pile import Pile
import random

""" Demo of each methods that can be print avoid 3 lines to be copied x times """
def demoFile():
    global list
    # * print(list.isEmpty())
    # * print(list.Length())
    list.Show()

""" Demo of each methods that can be print avoid 3 lines to be copied x times """
def demoPile():
    global list_1
    # * print(list_1.isEmpty())
    # * print(list_1.Length())
    list_1.Show()

# ! Test File
list = File()
demoFile()
for i in range(15):
    list.Insert(random.randint(0, 100))
demoFile()
for i in range(5):
    list.Remove()
demoFile()

print(list.At(random.randint(0, 10)))

print()

# ! Test Pile

list_1 = Pile()
demoPile()
for i in range(15):
    list_1.Insert(random.randint(0, 100))
demoPile()
for i in range(5):
    list_1.Remove()
demoPile()

print(list_1.At(random.randint(0, 10)))