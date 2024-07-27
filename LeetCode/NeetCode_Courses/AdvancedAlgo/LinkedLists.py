from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class FastSlowPointers:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        #876. Middle of the Linked List

        Given the head of a singly linked list, return the middle node of the linked list.

        If there are two middle nodes, return the second middle node.

        Example 1:
        Input: head = [1,2,3,4,5]
        Output: [3,4,5]
        Explanation: The middle node of the list is node 3.

        Example 2:
        Input: head = [1,2,3,4,5,6]
        Output: [4,5,6]
        Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
        """
        # Two iterations
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        # If length is odd, we find middle node at length // 2
        # If length is even, we find middle node at length // 2
        curr = head
        for _ in range(length // 2):
            curr = curr.next

        return curr

        # One iteration with two pointers
        # slow iterates at pace 1, fast iterates at pace 2
        slow = fast = head

        while slow:
            if fast == None:
                break
            elif fast.next == None:
                break
            else:
                slow = slow.next
                fast = fast.next.next

        return slow

        """
        Above while loop can be simplified to:

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
        """

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

    def pairSum(self, head: Optional[ListNode]) -> int:
        """
        #2130. Maximum Twin Sum of a Linked List

        In a linked list of size n, where n is even, the ith node (0-indexed) of the
        linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

        For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
        twin of node 2. These are the only nodes with twins for n = 4.

        The twin sum is defined as the sum of a node and its twin.

        Given the head of a linked list with even length, return the maximum twin sum
        of the linked list.

        Example 1:
        Input: head = [5,4,2,1] or 5 -> 4 -> 2 -> 1
        Output: 6
        Explanation:
        Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
        There are no other nodes with twins in the linked list.
        Thus, the maximum twin sum of the linked list is 6.

        Example 2:
        Input: head = [4,2,2,3] or 4 -> 2 -> 2 -> 3
        Output: 7
        4 + 3 = 7 while 2 + 2 = 4
        """
        # Single iteration, converts LinkedList into List
        nums = []
        curr = head
        while curr:
            nums.append(curr.val)
            curr = curr.next

        # n will always be an even number
        # Using Example 1, n = 2, so n / 2 = 2 -> i will be 0 and 1
        n = len(nums)
        # 1 <= node.val <= 10^5 so max_sum can be set to -1
        max_sum = -1
        for i in range(n // 2):
            max_sum = max(max_sum, nums[i] + nums[n - i - 1])

        return max_sum

        # Two pointers fast and slow -> find mid point of LinkedList first
        # Once we find mid point we can then reverse that half of the LinkedList
        prev = None
        slow = fast = head
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Now slow is the head of the second half of the LinkedList and prev is the
        # last node of the first half of the LinkedList
        # First set prev.next to None to terminate the first half
        prev.next = None

        # Then we reverse the second half
        curr, prev = slow, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 1 <= node.val <= 10^5 so max_sum can be set to -1
        max_sum = -1
        # Once reversed, prev is head of reversed second half
        # Both halves should be the same size
        while head and prev:
            max_sum = max(max_sum, head.val + prev.val)
            head = head.next
            prev = prev.next

        return max_sum

        # Two pointers fast and slow, but instead of reversing second half
        # we reverse the first half as we find the mid point
        prev = None
        slow = fast = head

        # No need for condition of (and fast.next) since we know len(LinkedList) is even
        while fast:
            # Have to set fast first because we are reversing in the same loop
            fast = fast.next.next
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        # 1 <= node.val <= 10^5 so max_sum can be set to -1
        max_sum = -1
        # Now slow is the start of the second half
        while slow and prev:
            max_sum = max(max_sum, slow.val + prev.val)
            slow = slow.next
            prev = prev.next

        return max_sum

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        #142. Linked List Cycle II

        Given the head of a linked list, return the node where the cycle begins.
        If there is no cycle, return null.

        There is a cycle in a linked list if there is some node in the list that
        can be reached again by continuously following the next pointer.

        Internally, pos is used to denote the index of the node that tail's next pointer
        is connected to (0-indexed). It is -1 if there is no cycle.

        Note that pos is not passed as a parameter.

        Do not modify the linked list.

        Example 1:
        Input: head = [3,2,0,-4], pos = 1
        Output: tail connects to node index 1
        Explanation: There is a cycle in the linked list, where tail connects to the second node.

        Follow up: Can you solve it using O(1) (i.e. constant) memory?
        """
        # Using Floyd's algorithm for cycle detection and entrance finding
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they ever meet, then we have a cycle
            if slow == fast:
                slow = head
                # Run Floyd's algorithm to find entrance
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

        # If we break out of the loop, then there was no cycle
        return None

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
