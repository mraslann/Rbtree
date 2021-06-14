# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from rbtree import Rbtree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   tree =Rbtree();
   tree.insert(5);
   tree.insert(2);
   tree.insert(3);
   node=tree.root.right
   print(tree.root.item);
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
