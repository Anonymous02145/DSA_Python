class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def count(self):
        count = 0
        _list = self.head

        while _list:
            count += 1
            _list = _list.next

        print(count)

    def printlist(self):
        if self.head is None:
            print("List None")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node
        
    def search(self, target):
        _search = self.head
        
        while _search:
            if _search.data == target:
                print("Found", target, " > ", True)
                return True
            _search = _search.next

if __name__ == '__main__':
    link = LinkedList()
    link.insert_begining(13)
    link.insert_begining(24)
    link.insert_begining(88)
    link.insert_at_tail(23)
    link.search(24)
    link.printlist()
    link.count()
