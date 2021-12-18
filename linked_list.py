"""Linked lists are lists that has each element store up the reference to its previous and next elements"""


class Node:
    """Linked list element class"""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.length = 1 if head else 0

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
        self.length += 1

    def get_position(self, pos):
        current = self.head
        counter = 1
        if self.head:
            while counter < pos:
                if current.next:
                    current = current.next
                    counter += 1
                else:
                    return None
            return current
        else:
            return None

    def insert(self, new_element, pos):
        current = self.head
        counter = 1
        prev = 0
        if self.head:
            while counter < pos:
                if current:
                    prev = current
                    current = current.next
                    counter += 1
                else:
                    return None
            new_element.next = current
            prev.next = new_element
            self.length += 1
        else:
            return None

    def replace(self, new_element, pos):
        current = self.head
        counter = 1
        if pos > 1:
            while counter < pos - 1:
                if current:
                    current = current.next
                    counter += 1
                else:
                    print("position out of list")
            new_element.next = current.next.next
            current.next = new_element
        else:
            new_element.next = current.next
            self.head = new_element

    def delete(self, value):
        current = self.head
        if self.head:
            if self.head.value == value:
                self.head = current.next
                self.length -= 1
            else:
                while current.next:
                    if current.next.value == value:
                        current.next = current.next.next
                        self.length -= 1
                        break
                    else:
                        current = current.next
        else:
            pass

    def get_middle(self):
        """
        1. get the pos of the middle element
        2. get the element in the middle position
        """
        mid_pos = (self.length // 2) + 1
        return self.get_position(mid_pos)

    def rotate_list(self, pos):
        """
        1. link the last element to the head
        2. break the element after the element at pos and make it the head
        """
        current = self.head
        counter = 1
        if self.head:
            while current.next:
                current = current.next
            current.next = self.head
            while counter <= pos:
                current = current.next
                counter += 1
            self.head = current.next
            current.next = None
        else:
            pass

    def display(self, label=""):
        current = self.head
        disp = str(current.value)
        while current.next:
            disp += " -> " + str(current.next.value)
            current = current.next
        disp += " -> Null"
        print(label, disp)

    def reverse(self):
        """
        1. use 3 pointers; head, temp1 and temp2
        2. the head holds the current node
        3. temp1 holds the previous node
        4. temp2 holds the next node
        """
        head = self.head
        prev_node = None
        while head:
            forward_node = head.next
            head.next = prev_node
            prev_node = head
            head = forward_node
        self.head = prev_node

    @staticmethod
    def get_value(node):
        return node.value if node else node

    def is_palindrome(self):
        """
        1. Uses 3 pointers, p1, p2, pp2
        2. p1 to track the end of the list, will move 2 steps per move
        3. p2 to get the middle of the list
        4. pp2 will trail p2 and will be used to break the list
        4. p2 will be used to break the list into 2 equal parts
        5. The head list will be reversed.
        6. The 2 list will be compared
        """
        p1 = p2 = self.head
        pp2 = None
        # getting the middle of the list
        while self.head:
            p1 = p1.next.next
            pp2 = p2
            p2 = p2.next
            if not p1:
                break
            if not p1.next:
                p2 = p2.next
                break
        # break the list at pp2
        pp2.next = None

        # reverse the first list with head of self.head
        head = self.head
        prev_node = None
        while head:
            forward_node = head.next
            head.next = prev_node
            prev_node = head
            head = forward_node
        self.head = prev_node

        # compare lists
        head1 = self.head
        head2 = p2
        while head2:
            if head1.value != head2.value:
                return False
            head1 = head1.next
            head2 = head2.next
        return True

    def remove_duplicate(self):
        """
        1. create a dictionary with the key as the
        2. Loop through the list
        """
        current = self.head
        checker = {current.value: 1}
        if self.head:
            while current.next:
                prev = current
                current = current.next
                try:
                    # delete the item in that pos
                    if checker[current.value]:
                        prev.next = current.next
                except:
                    checker[current.value] = 1
                self.display("testing with %s:" % self.get_value(current))
                print(checker)
                print("prev:", self.get_value( prev), "next current:", self.get_value(current.next))

        else:
            print("No way home!")


e1 = Node("r")
e2 = Node("a")
e3 = Node("c")
e4 = Node("e")
e5 = Node("c")
e6 = Node("a")
e7 = Node("r")

linkedlist = LinkedList(e1)
linkedlist.append(e2)
linkedlist.append(e3)
linkedlist.append(e4)
linkedlist.append(e5)
linkedlist.append(e6)
linkedlist.append(e7)

# linkedlist.display("list:")

linkedlist.remove_duplicate()
linkedlist.display("list after duplicates have been removed:")
