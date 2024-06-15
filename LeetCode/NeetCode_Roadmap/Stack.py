from collections import defaultdict, deque
from typing import List


class Solutions:
    def is_valid(self, s: str) -> bool:
        """
        #20

        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
        determine if the input string is valid.

        An input string is valid if:
            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.

        Example 1:
        Input: s = "()"
        Output: true

        Example 2:
        Input: s = "()[]{}"
        Output: true

        Example 3:
        Input: s = "(]"
        Output: false

        Constraints:
            1 <= s.length <= 104
            s consists of parentheses only '()[]{}'.
        """
        parentheses = {
            "{": "}",
            "(": ")",
            "[": "]"
        }

        stack = deque()
        for item in s:
            if item in parentheses.keys():
                stack.append(item)
            else:
                try:
                    open_part = stack.pop()
                except IndexError:
                    return False
                if parentheses[open_part] != item:
                    return False

        return len(stack) == 0

    def eval_RPN(self, tokens: List[str]) -> int:
        """
        #150
        You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
        Evaluate the expression. Return an integer that represents the value of the expression.

        Note that:
            The valid operators are '+', '-', '*', and '/'.
            Each operand may be an integer or another expression.
            The division between two integers always truncates toward zero.
            There will not be any division by zero.
            The input represents a valid arithmetic expression in a reverse polish notation.
            The answer and all the intermediate calculations can be represented in a 32-bit integer.

        Example 1:
        Input: tokens = ["2","1","+","3","*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9

        Example 2:
        Input: tokens = ["4","13","5","/","+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6
        """
        def _is_operator(token: str) -> bool:
            operators = ["+", "-", "*", "/"]
            return token in operators

        def _exec_operator(operator: str, first: int, second: int) -> int:
            match operator:
                case "+":
                    return first + second
                case "-":
                    return first - second
                case "*":
                    return first * second
                case "/":
                    return int(first / second)

        stack = deque()
        for token in tokens:
            if _is_operator(token):
                second = stack.pop()
                first = stack.pop()
                stack.append(_exec_operator(token, first, second))
            else:
                stack.append(int(token))

        return stack[-1]

    def generate_parenthesis(self, n: int) -> List[str]:
        def _generate(n: int) -> List[str]:
            if n == 0:
                return ""
            if n == 1:
                return "()"

        return _generate(n)

    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        # Slow brute force approach
        n = len(temperatures)
        results = [0] * n

        # Temperatures can have duplicates
        temp_map = defaultdict(list)
        for i, temp in enumerate(temperatures):
            temp_map[temp].append(i)

        for i, temp in enumerate(temperatures):
            closest_index = n
            for other_temp in range(temp + 1, 101):
                if other_temp in temp_map:
                    indices = temp_map[other_temp]
                    for index in indices:
                        if index > i:
                            closest_index = min(closest_index, index)

            if closest_index != n:
                results[i] = closest_index - i

        return results


class MinStack:
    """
    #155
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
    You must implement a solution with O(1) time complexity for each function.

    For each value added to the stack, we add a corresponding minimum to minStack. This way,
    len(stack) == len(minStack) and each corresponds to the minimum at that point in time.
    """
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
