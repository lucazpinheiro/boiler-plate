
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, data):
        """
        insert node on first position
        """ 
        self.head = Node(data, self.head)
        self.size += 1

    def insert(self, data):
        """
        insert node on last position
        """
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node
        self.size += 1
    
    def insert_at(self, data, index):
        if index < 0 or index >= self.size:
            print('index out of range')
            return

        if index == 0:
            self.head = Node(data, self.head)
            self.size += 1
            return

        node = Node(data)
        current = self.head
        count = 0

        while count < index:
            previous = current
            count += 1
            current = current.next

        node.next = current
        previous.next = node
        self.size += 1

    def get_at(self, index):
        if index < 0 or index >= self.size:
            print('index out of range')
            return

        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.next
        
        return current.data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            print('index out of range')
            return

        previous = ''
        current = self.head
        count = 0
        while count < index:
            previous = current
            count += 1
            current = current.next
        
        previous.next = current.next
        self.size -= 1

    def set_at(self, index, data):
        if index < 0 or index >= self.size:
            print('index out of range')
            return

        current = self.head
        count = 0
        while count < index:
            count += 1
            current = current.next
        
        current.data = data

    def clear_list(self):
        self.head = None
        self.size = 0

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def list_size(self):
        return self.size
        

# ls = LinkedList()

# ls.insert_first('one')
# ls.insert('two')
# ls.insert('three')

# print(ls.print_list())
# print('\n')
# print(ls.list_size())

# ls.insert_at('teste', 1)
# print(ls.print_list())