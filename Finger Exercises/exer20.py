class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        return len(self.myList)
        # Your code here

    def add(self, elem):
        self.myList.append(elem)
        # Your code here

class Queue(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        del_el = None
        if self.size() > 0:
            del_el = self.myList[0]
            del self.myList[0]
        return del_el

        # Your code here