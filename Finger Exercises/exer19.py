class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        self.myList = []

    def size(self):
        return len(self.myList)

    def add(self, elem):
        self.myList.append(elem)
        # Your code here

    def show(self):
        return self.myList

class Stack(Container):

    def remove(self):
        del_val = None
        if len(self.myList) != 0:
            del_val = self.myList[-1]
            del self.myList[-1]
        return del_val
        # Your code here

c1 = Container()
c1.add('1')
c1.add('2')
print(c1.show())

c2 = Stack()
c2.add(1)
c2.add(2)
print(c2.show())
c2.remove()
print(c2.show())
c2.remove()
print(c2.show())