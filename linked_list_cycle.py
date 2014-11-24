from linked_list import Node


acyclic = Node(1, Node(2, Node(3)))

cyclic = Node(1)
cyclic.next = Node(2, Node(3, Node(4, cyclic)))

def node_generator(node):
    while node:
        yield node
        node=node.next
    

def is_cyclic(node):
    faster_generator = node_generator(node)
    slower_generator = node_generator(node)
    try:
        next(faster_generator)
        for item in slower_generator: #item = 3
            item0 = next(faster_generator) # item0 = 2
            item1 = next(faster_generator) # item1 = 3
            if id(item) == id(item0) or id(item) == id(item1):
                return True     
    except StopIteration:
        pass
    return False
   
    
print(is_cyclic(acyclic))
print(is_cyclic(cyclic))