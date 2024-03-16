from llist import LList, Node, append


def length(lst):
    count = 0
    node = lst.head
    while node.next:
        count = count + 1
        lst = node.next
        if node.next == None:
            break
        return(count)


def llprint(lst):
    node = lst.head
    while node.next:
        print(lst)
        if node.next = None:
            break


if __name__ == "__main__":
    llist = LList() 
    append(llist, Node(1))
    append(llist, Node(2))
    append(llist, Node(4))
    append(llist, Node(8))
    append(llist, Node(16))
    append(llist, Node(32))
    append(llist, Node(64))
    append(llist, Node(128))
    append(llist, Node(256))
    append(llist, Node(512))
    llprint(llist)
    length(llist)