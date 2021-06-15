# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from rbtree import Rbtree

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    counter = 0
    rb = Rbtree()
    dictf = open('EN-US-Dictionary.txt', 'r')
    dictionary = dictf.read().splitlines()
    for key in dictionary:
        rb.insert(key)
        counter = counter + 1
    print(f'The number of words in the dictionary are {counter}')
    print(f'The height of the tree is {rb.treeheight(rb.root)}')

operation = input('1-Print dictionary size\n2-Insert a word\n3-Look up a word\n')
if operation == '1':
    print(f'The size of the dictionary is {counter}\n')
elif operation == '2':
    x = rb.insert(input('Write the word you want to insert\n'))
    if x == 2:
        print("ERROR: Word already in the dictionary!")
    else:
        print("ERROR: Word inserted")

else:
    rb.search(input('Write the word you want to search for\n'))
