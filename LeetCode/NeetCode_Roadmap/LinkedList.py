from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solutions:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        #206. Reverse Linked List

        Given the head of a singly linked list, reverse the list, and return the reversed list.
        """
        def iterative():
            curr, prev = head, None

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        def recursive():
            def _helper(curr, prev):
                if not curr:
                    return
                else:
                    nxt = curr.next
                    curr.next = prev
                    return _helper(nxt, curr)
            return _helper(head, None)

        return iterative()

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        #21. Merge Two Sorted Lists

        You are given the heads of two sorted linked lists list1 and list2.

        Merge the two lists into one sorted list. The list should be made by splicing together
        the nodes of the first two lists.

        Return the head of the merged linked list.

        Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4,]
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

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        #143. Reorder List

        L0 → L1 → … → Ln - 1 → Ln
        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
        You may not modify the values in the list's nodes. Only nodes themselves may be changed.

        Do not return anything, modify head in-place instead.

        Example 1:
        Input: head = [1,2,3,4]
        Output: [1,4,2,3]
        """
        # Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge the two halves, first half should always be larger
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        #19. Remove Nth Node From End of List

        Given the head of a linked list, remove the nth node from the end of the list
        and return its head.

        Follow up: Could you do this in one pass?

        Example 1:
        Input: head = [1,2,3,4,5], n = 2
        Output: [1,2,3,5]

        Length = 5, n = 2 -> 5 - 2 = 3 -> Remove element at position 3

        Example 2:
        Input: head = [1,2], n = 1
        Output: [1]

        Length = 2, n = 1 -> 2 - 1 = 1 -> Remove element at position 1
        """
        # Two pass method
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        if length - n == 0:
            return head.next

        curr = head
        count = 0
        prev = None
        while curr:
            if count == length - n:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            count += 1

        return head

        # One pass method
        slow = fast = head
        prev = None
        count = 0
        while fast:
            if count >= n:
                prev = slow
                slow = slow.next
            count += 1
            fast = fast.next

        if prev:
            prev.next = slow.next
        else:
            head = head.next

        return head

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        #138. Copy List with Random Pointer

        A linked list of length n is given such that each node contains an additional
        random pointer, which could point to any node in the list, or null.

        Construct a deepcopy of the list. The deep copy should consist of exactly n
        brand new nodes, where each new node has its value set to the value of its
        corresponding original node.

        Both the next and random pointer of the new nodes should point to new nodes
        in the copied list such that the pointers in the original list and copied list
        represent the same list state. None of the pointers in the new list should point
        to nodes in the original list.

        Example 1:
        Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
        Explanation:
        7.random = null
        13.random = node 0 (7)
        11.random = node 4 (1 - currently not in the consideration yet)
        10.random = node 2 (11)
        1.random = node 0 (7)

        Note: a node's random can be itself!
        """
        # One pass approach that maps original nodes to their copies
        deepcopy = Node(0)
        copy_iter = deepcopy
        og_iter = head

        random_mapping = { None: None }

        while og_iter:
            # If current original Node was found in the mapping, then it was .random
            # for some previous node, and the node was already created then
            if og_iter in random_mapping:
                new_node = random_mapping[og_iter]
            else:
                new_node = Node(og_iter.val)
                random_mapping[og_iter] = new_node

            # Try to fetch random node from mapping. If it doesn't exist, then current .random
            # is a new Node, so we create it. Otherwise, it was either a previous node, or
            # a .random for some previous node, and the node was already created then
            og_random = og_iter.random
            if og_random in random_mapping:
                new_node.random = random_mapping[og_random]
            else:
                random_node = Node(og_random.val)
                new_node.random = random_node
                random_mapping[og_random] = random_node

            # Moving to next
            og_iter = og_iter.next
            copy_iter.next = new_node
            copy_iter = copy_iter.next

        return deepcopy.next

        # Two pass approach, first pass maps all originals to copies
        # Second pass sets .next and .random
        old_to_copy = { None: None }

        og_iter = head
        while og_iter:
            new_node = Node(og_iter.val)
            old_to_copy[og_iter] = new_node
            og_iter = og_iter.next

        og_iter = head
        while og_iter:
            copy = old_to_copy[og_iter]
            copy.next = old_to_copy[og_iter.next]
            copy.random = old_to_copy[og_iter.random]
            og_iter = og_iter.next

        return old_to_copy[head]

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2. Add Two Numbers

        You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order, and each of their nodes contains a single digit.
        Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero,
        except the number 0 itself.

        Example 1:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.
        """
        # Initial implementation
        result = ListNode()
        curr = result
        carry = False

        while l1 and l2:
            val = l1.val + l2.val
            val = val + 1 if carry else val
            if val >= 10:
                val = val % 10
                carry = True
            else:
                carry = False

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        # Guaranteed to be only one of l1 or l2, both can't be leftovers
        leftover = l1 if l1 else l2
        while leftover:
            val = leftover.val + 1 if carry else leftover.val
            if val >= 10:
                val = val % 10
                carry = True
            else:
                carry = False

            curr.next = ListNode(val)
            curr = curr.next
            leftover = leftover.next

        if carry:
            curr.next = ListNode(1)

        return result.next

        # Cleaned up implementation
        carry = 0
        result = ListNode()
        curr = result

        while l1 or l2 or carry:
            val_1 = l1.val if l1 else 0
            val_2 = l2.val if l2 else 0

            val = val_1 + val_2 + carry
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return result.next

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        #141. Linked List Cycle

        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        There is a cycle in a linked list if there is some node in the list that can be reached
        again by continuously following the next pointer.

        Internally, pos is used to denote the index of the node that tail's next pointer is
        connected to. Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.

        Example 1:
        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to
        the 1st node (0-indexed).

        In the example, the LinkedList is represented as:
        3 -> 2 -> 0 -> -4 -> 2, hence, a cycle
        """
        # Two pointer iteration
        # slow iterates at pace 1, fast iterates at pace 2
        # If a cycle does not exist, fast will eventually be None
        # If a cycle exists, slow == fast (not including the start where slow = fast = head)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        # If while loop is broken, then fast or fast.next was None, meaning it was not a loop
        return False

    def findDuplicate(self, nums: List[int]) -> int:
        """
        #287. Find the Duplicate Number

        Given an array of integers nums containing n + 1 integers where each integer
        is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses only
        constant extra space.

        Example 1:
        Input: nums = [1,3,4,2,2]
        Output: 2

        Using Example 1 -> len(nums) = 5 -> n = 5 - 1 = 4. Sum of 1 to 4 is (n)(n + 1)/2 = 10
        If we add everything up and minus sum function result, we get the duplicate

        Unfortunately this math approach only works if every single integer appears exactly once
        and the duplicate also appears once. In this question, the duplicate can appear two or
        more times. Thus, the math approach does not work.
        """
        # Consider the list as a LinkedList such that the values point to the next index
        # to traverse to. With this, duplicates will create a cycle
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                # Now we found the cycle, we want the entrance
                slow = nums[0]
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]

                return slow
