from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedLists:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        #206

        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Given the head of a singly linked list, reverse the list, and return the reversed list.
        Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
        """
        def _iterative():
            curr, prev = head, None
            while curr:
                nnext = curr.next
                curr.next = prev
                prev = curr
                curr = nnext
            return prev

        def _iterative_2():
            if not head:
                return None

            curr = head
            reversed_list = ListNode(curr.val)
            curr = curr.next

            while curr:
                curr_node = ListNode(curr.val)
                curr_node.next = reversed_list
                reversed_list = curr_node
                curr = curr.next

            return reversed_list

        def _recursive():
            def __helper(curr, prev):
                if not curr:
                    return prev
                else:
                    nnext = curr.next
                    curr.next = prev
                    return __helper(nnext, curr)
            return __helper(head, None)

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #21
        You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into
        one sorted list. The list should be made by splicing together the nodes of the first two lists.

        Return the head of the merged linked list.

        Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
        """
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return head.next


class MySinglyLinkedList:
    """
    #707

    Design your implementation of the linked list. You can choose to use a singly
    or doubly linked list.

    A node in a singly linked list should have two attributes: val and next.
        val is the value of the current node, and next is a pointer/reference to the next node.

    If you want to use the doubly linked list, you will need one more attribute prev to indicate
    the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
    """
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return

        self.length +=1
        new_node = ListNode(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        nnext = curr.next
        curr.next = new_node
        new_node.next = nnext

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return

        self.length-= 1

        if index == 0:
            self.head = self.head.next
            return

        curr = self.head
        for _ in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next

class DoublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:
    """
    #1472
    You have a browser of one tab where you start on the homepage and you can visit another url,
    get back in the history number of steps or move forward in the history number of steps.
    """
    def __init__(self, homepage: str):
        self.history = DoublyNode(homepage)
        self.index = 0

    def visit(self, url: str) -> None:
        curr = self.history
        for _ in range(self.index):
            curr = curr.next
        curr.next = DoublyNode(url, curr)
        self.index += 1

    def back(self, steps: int) -> str:
        self.index = max(self.index - steps, 0)
        curr = self.history
        for _ in range(self.index):
            curr = curr.next
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.history
        for _ in range(self.index):
            curr = curr.next

        while steps > 0 and curr.next:
            self.index += 1
            steps -= 1
            curr = curr.next
        return curr.val


class BrowserHistory2:
    """
    #1472
    Noticed a pattern above where I only use head to get to current, so replaced
    head with current in init itself. Cleaner solution and don't always need to traverse
    to current index first!
    """
    def __init__(self, homepage: str):
        self.curr = DoublyNode(homepage)

    def visit(self, url: str) -> None:
        self.curr.next = DoublyNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val
