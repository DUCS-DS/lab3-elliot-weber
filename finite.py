#elliot weber
from genfinite import lst
from llist import LList, Node, append





def length(lst):


    counter =1
    if lst.head:
        node = lst.head
        while node.next:
            node=node.next
            counter=counter+1
    else:
        return "no"
    return counter


def llprint(lst):
    if lst.head: 
        node = lst.head
        while node.next:
            node=node.next
            print(node.val)
    
    else:
        print("no")




if __name__ == "__main__":


    llist=LList()

    append(llist,Node(1))
    append(llist,Node(2))
    append(llist,Node(4))        
    append(llist,Node(8))
    append(llist,Node(16))
    append(llist,Node(32))
    append(llist,Node(64))
    append(llist,Node(128))
    append(llist,Node(256))
    append(llist,Node(512))

    

    print(length(lst))
    llprint(llist)
