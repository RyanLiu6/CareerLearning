from collections import defaultdict, deque
from typing import List


class Solution:
    def count_students(self, students: List[int], sandwiches: List[int]) -> int:
        """
        #1700
        The school cafeteria offers circular and square sandwiches at lunch break,
        referred to by numbers 0 and 1 respectively. All students stand in a queue.
        Each student either prefers square or circular sandwiches.

        The number of sandwiches in the cafeteria is equal to the number of students.
        The sandwiches are placed in a stack. At each step:

        If the student at the front of the queue prefers the sandwich on the top of the stack,
        they will take it and leave the queue.

        Otherwise, they will leave it and go to the queue's end.
        This continues until none of the queue students want to take the top sandwich and
        are thus unable to eat.

        You are given two integer arrays students and sandwiches where sandwiches[i] is the
        type of the ith sandwich in the stack (i = 0 is the top of the stack) and students[j]
        is the preference of the jth student in the initial queue (j = 0 is the front of the queue).
        Return the number of students that are unable to eat
        """
        students = deque(students)
        sandwiches = deque(sandwiches)
        students_dict = defaultdict(int)
        for student in students:
            students_dict[student] += 1

        while True:
            if len(sandwiches) == 0:
                break
            if students_dict[sandwiches[0]] <= 0:
                break
            if students[0] == sandwiches[0]:
                student = students.popleft()
                sandwiches.popleft()
                students_dict[student] -= 1
            else:
                students.append(students.popleft())

        return len(students)

        # Slightly better approach
        # students_dict = defaultdict(int)
        # for student in students:
        #     students_dict[student] += 1

        # for sandwich in sandwiches:
        #     if sandwich == 0:
        #         if students_dict[sandwich] == 0:
        #             return students_dict[1]
        #         students_dict[sandwich] -= 1
        #     else:
        #         if students_dict[sandwich] == 0:
        #             return students_dict[0]
        #         students_dict[sandwich] -= 1

        # return 0


class MyStack:
    """
    #225
    Implement a last-in-first-out (LIFO) stack using only two queues. The implemented
    stack should support all the functions of a normal stack (push, top, pop, and empty).

    Notes:
        You must use only standard operations of a queue, which means that only push to back,
        peek/pop from front, size and is empty operations are valid.

        Depending on your language, the queue may not be supported natively. You may simulate a
        queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.

    The question specifies that we're only allowed to push to back (append) and pop from front (popleft()).
    Python's built-in pop() pops from right cannot be used. Otherwise this implementation is trivial.
    """
    def __init__(self):
        self.stack = deque()

    def push(self, x: int) -> None:
        n = len(self.stack)
        self.stack.append(x)
        for _ in range(n):
            self.stack.append(self.stack.popleft())

    def pop(self) -> int:
        return self.stack.popleft()

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0
