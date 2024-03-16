from llist import *

def llprint(lst, num):
    node = lst.head
    while node.next:
        print(num)
        if node.next = None:
            break

def find_cycle(f, x0) -> (int, int):
    lst1 = f(x0)
    lst2 = f(f(x0))
    while lst1 != lst2:
        lst1 = f(lst1)
        lst2 = f(lst2)
    lst = 0
    lst1 = x0
    while lst1 != lst2:
        lst1 = f(lst1)
        lst2 = f(lst2)
        lst += 1
    lst0 = 1
    lst2 = f(lst1)
    while lst1 != lst2:
        lst2 = f(lst1)
        lst0 += 1
    return lst0, lst


if __name__ == "__main__":
from llist import LList
tup = find_cycle(lst)
print(f"cycle start: [tup[0]]")
print(f"     length: [tup[1]]")
