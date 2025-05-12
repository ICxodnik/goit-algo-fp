class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"
    
    def __str__(self):
        return self.__repr__()
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(4)
    ll.insert_at_end(2)
    ll.insert_at_end(5)
    ll.insert_at_end(1)

    print("Оригінальний список:")
    ll.print_list()

    ll.sort()
    print("Відсортований список:")
    ll.print_list()

    ll.reverse()
    print("Реверсований список:")
    ll.print_list()