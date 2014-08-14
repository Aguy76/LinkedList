class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        return str(self.item)

class EntryNode(Node):
    def __init__(self, first=None, last=None, length=0, item=None):
        self.first = first
        self.last = last
        self.length = length
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, *args):
        self.entry = EntryNode()
        self.value = 0
        for i in args:
            self.append(i)
    
    def __str__(self):
        """should return all items in LinkedList
        like LinkedList[item, item, ...]"""
        begining = 'LinkedList(['
        ending = '])'
        if self.isEmpty():
            return begining + ending
        itemString = ''
        if self.entry.length == 2:
            itemString += str(self.entry.first.item)
            itemString += ', '
            itemString += str(self.entry.last.item)
        else:
            for i in self[:self.entry.length-1]:
                itemString += str(i)
                itemString += ', '
            itemString += str(self.entry.last.item)
        return begining + itemString + ending

    def __add__(self, y):
        """__add__(y)
            x.__add__(y) <==> x + y"""
        if y.isEmpty():
            return
        elif len(y) == 1 and not self.isEmpty():
            self.entry.last.next = y.entry.last
            self.entry.last = y.entry.last
            self.entry.length += 1
            return
        else:
            for i in range(len(y)):
                newNode = y.get(i, resultType='node')
                self.append(newNode.item)

    def __contains__(self, y):
        """element y is in list x
        y in x"""
        for i in self:
            if i == y:
                return True
        else:
            return False

    def __setitem__(self, index, value):
        """sets item at index to value
        x[index] = value"""
        node = self.get(index, resultType='node')
        node.item = value
    
    def __delitem__(self, index):
        """deletes the node at index in x
        del x[index]"""
        if index > self.entry.length or index < 0:
            raise IndexError('list index out of range')
        node = self.get(index, resultType='node')
        if node is self.entry.first:
            self.pop()
        elif node is self.entry.last:
            self.popRight()
        else:
            oneLess = self.get(index-1, resultType='node')
            oneLess.next = node.next
            del node
            self.entry.length -= 1
    
    def __len__(self):
        if self.entry:
            return self.entry.length
        
    def __iter__(self, types='item'):
        """Returns an iterator object over the list.
        types specifies whether to get the values of
        the nodes or the nodes themselves.
        x.__iter__(types='nodes')
        """
        for i in range(self.entry.length):
            yield self.get(position=i, resultType=types)

    def __reversed__(self, types='item'):
        """Returns a reverse iterator over the list.
        types specifies whether to get the values of
        the nodes or the nodes themselves.
        x.__reversed__(types='nodes')"""
        for i in reversed(range(self.entry.length)):
            yield self.get(i, resultType=types)
    
    def __getitem__(self, position, resultType='item'):
        """___getitem__(index)
            x.__getitem__(y) <==> x[y]"""
        
        def _returnCheck(result, resultType):
            """Checks what type we should be returning
            and returns the matching representation of
            the node."""
            if resultType == 'item':
                return result.item
            elif resultType == 'node':
                return result
            else:
                raise TypeError('get failed: bad resultType')
                return
           
        if self.entry.length == 0:
            return None
        elif position > self.entry.length-1:
            raise IndexError('list index out of range')
        elif self.entry.length < position:
            result = self.entry.last
            return _returnCheck(result, resultType)
        elif self.entry.length == 1:
            result = self.entry
            return _returnCheck(result, resultType)
        else:
            result = self.entry.first
            for i in range(position):
                result = result.next
            return _returnCheck(result, resultType)

    def __getslice__(self, i, j):
        """get slice from i to j
        tree[i:j] no neg indices"""
        if i >= 0 and j <= self.entry.length:
            newList = LinkedList()
            for index in range(i, j):
                newList.append(self.get(index))
            return newList
        else:
            raise IndexError("list index out of range")
    
    def __lt__(self, y):
        """less than
        x < y"""
        pass

    def __le__(self, y):
        """less than or equal to
        x <= y"""
        pass

    def __gt__(self, y):
        """greater than
        x > y"""
        pass

    def __ge__(self, y):
        """greater than or equal to
        x >= y"""
        pass

    def __eq__(self, y):
        """equal to
        x == y"""
        pass

    def __ne__(self, y):
        """x not equal to y
        x != y"""
        pass
    
    def isEmpty(self):
        """Checks if the list is empty or not
        we define empty as a list of length 0."""
        if self.entry.length == 0:
            return True
        else:
            return False

    def get(self, position, resultType='item'):
        """Returns the element at position starting from 0.
        
        resultType is either node or item, which specifies
        whether you want the node itself or it's item at that
        position."""
        return self.__getitem__(position, resultType)
    
    def insert(self, element):
        """Adds a new node with element as it's item
        to the start (or left side) of the list."""
        new = Node(item=element)
        old = self.entry.first
        self.entry.first = new
        new.next = old
        if self.entry.last == None:
            self.entry.last = new
        self.entry.length += 1

    def pop(self):
        """Removes the first item from the list
        and returns it. Returns None if empty"""
        if self.isEmpty():
            return None
        oldfirst = self.entry.first
        self.entry.first = oldfirst.next
        self.entry.length -= 1
        return oldfirst

    def append(self, element):
        """Adds a new node with element as it's item
        to the end (or right side) of the list."""
        oldlast = self.entry.last
        self.entry.last = Node(item=element)
        if self.entry.first == None:
            self.entry.first = self.entry.last
        if oldlast != None:
            oldlast.next = self.entry.last
        self.entry.length += 1

    def popRight(self):
        """Removes the last item from the list
        and returns it. Returns None if empty"""
        if self.isEmpty():
            return None
        elif self.entry.length == 1:
            oldlast = self.entry.last
            self.entry.last = None
            self.entry.first = None
            self.entry.length = 0
            return oldlast
        else:
            oldlast = self.entry.last
            newlast = self.get(self.length - 1)
            self.entry.last = newlast
            newlast.next = None
            self.entry.length -= 1
            return oldlast

    def remove(self, index):
        """Removes a specified node at position from the list."""
        self.__delitem__(index)

    def count(self, item):
        """returns the number of times item
        occurs in the list
        x.count(item)"""
        count = 0
        for i in self:
            if i == item:
                count += 1
        return count
    
    def sort(self):
        """sorts the list via insertion sort
        x.sort()"""
        for i in xrange(1, len(self)):
            key = self[i]
            last = i - 1
            while last >= 0 and myList[last] > key:
                self[last+1] = self[last]
                last -= 1
            self[last+1] = key


if __name__ == '__main__':
    import random
    myList = LinkedList(1,2,3)
    print myList
    for i in myList:
        print i
    print 'len is', len(myList)
    print myList[2:3]
    numRange = xrange(300)
    for i in numRange:
        myList.append(random.choice(numRange))
    myList.sort()
