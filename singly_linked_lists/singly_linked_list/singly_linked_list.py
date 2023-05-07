class Node:
    """A class used to represent a Node in a Singly Linked List

    Attributes
    ----------
    value : any
        The value being stored in the Node
    nextNode : Node
        Pointer to the next Node in the list (default None)
    """

    def __init__(self, value, nextNode=None):
        """
        Parameters
        ----------
        value : any
            The value to store in the node
        nextNode : Node
            The next node in the list
        """
        self.value = value
        self.next = nextNode


class List:
    """A class used to represent a Singly Linked List

    Attributes
    ----------
    head : Node
        The first node in the list
    tail: Node
        The last node in the list

    Methods
    -------
    push(value)
        Pushes a node onto the beginning of the list
    insertBefore(node, value)
        Inserts a new node into the list before the given node
    insertAfter(node, value)
        Inserts a new node in the list after the given node
    append(value)
        Appends a new node to the end of the list
    deleteLast()
        Deletes the last node in the list
    deleteFirst()
        Deletes the first node in the list
    delete(value)
        Deletes the node containing the value if it exists
    empty()
        Checks if the list is empty
    display()
        Displays the current list
    """

    def __init__(self):
        """Initializes a new Singly Linked List"""
        self.head = None
        self.tail = None

    def push(self, value) -> None:
        """Pushes a new node with the given value onto the beginning of the list

        Parameters
        ----------
        value : any
            The value to be stored in the node
        """
        newNode = Node(value, self.head)
        self.head = newNode

        if self.tail is None:
            self.tail = newNode

    def insertBefore(self, node: Node, value) -> None:
        """Inserts a new node before the given node

        Parameters
        ----------
        node : Node
            The node to insert before
        value : any
            The value to store in the new node
        """
        if self.empty() or self.head == node:
            self.push(value)
        else:
            prev = None
            curr = self.head

            while curr is not None and curr is not node:
                prev = curr
                curr = curr.next
            if curr is not None:
                prev.next = Node(value, curr)
            else:
                self.append(value)

    def insertAfter(self, node: Node, value) -> None:
        """Inserts a new node after the given node

        Parameters
        ----------
        node : Node
            The node to insert after
        value : any
            The value to store in the new node
        """
        newNode = Node(value, node.next)
        node.next = newNode

        if self.tail.value == node.value:
            self.tail = newNode

    def append(self, value) -> None:
        """Appends a new node to the end of the list

        Parameters
        ----------
        value : any
            The value to store in the new node
        """
        newNode = Node(value, None)

        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def deleteLast(self) -> None:
        """Deletes last node in the list

        Raises
        ------
        IndexError
            If the list is empty
        """
        if self.empty():
            raise IndexError("can't delete node from empty list")

        # If there is only one node remove it
        if self.head.value == self.tail.value:
            self.head = None
            self.tail = None
            return None

        currentHead = self.head

        while currentHead.next.next is not None:
            currentHead = currentHead.next

        self.tail = currentHead
        currentHead.next = None
        return None

    def deleteFirst(self) -> None:
        """Deletes the first node in the list

        Raises
        ------
        IndexError
            If the list is empty
        """
        if self.empty():
            raise IndexError("can't delete node from empty list")

        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return None

    def delete(self, value) -> None:
        """Deletes node with the given value

        Parameters
        ----------
        value : any
            The value to delete from the list

        Raises
        ------
        IndexError
            If the list is empty or the value is not stored in the list
        """
        if self.empty():
            raise IndexError("can't delete node from empty list")

        curr = self.head

        while curr.next is not None:
            if curr.next.value == value:
                curr.next = curr.next.next
                return None
            curr = curr.next
        raise IndexError("can't find given node")

    def empty(self) -> bool:
        """Checks if the linked list is empty

        Returns
        -------
        bool
            True if list is empty otherwise False
        """
        return self.head is None

    def display(self) -> None:
        """Displays the current list"""
        list = self.head

        while list is not None:
            print(f"{list.value} ")
            list = list.next
        print()
