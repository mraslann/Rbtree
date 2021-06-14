# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from rbtree import Rbtree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter = 0
    rb = Rbtree()
    dictf = open('EN-US-Dictionary.txt', 'r')
    dictionary = dictf.read().splitlines()
    for key in dictionary:
        rb.insert(key)
        counter = counter+1
    print(counter)
    print(rb.treeheight(rb.root))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
