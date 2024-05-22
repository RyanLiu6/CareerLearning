from collections import deque
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
        brackets = {
            ")" : "(",
            "]": "[",
            "}" : "{",
        }

        stack = deque()

        for item in s:
            if item in brackets.values():
                stack.append(item)
            else:
                try:
                    popped = stack.pop()
                except IndexError:
                    return False
                if popped != brackets[item]:
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
        def _is_operator(letter: str) -> bool:
            operators = ["+", "-", "*", "/"]
            return letter in operators

        def _calculate(operator: str, first: int, second: int) -> int:
            match operator:
                case "+":
                    return second + first
                case "-":
                    return second - first
                case "*":
                    return second * first
                case "/":
                    return int(second / first)

        stack = deque()
        for token in tokens:
            if _is_operator(token):
                first = stack.pop()
                second = stack.pop()
                stack.append(_calculate(token, first, second))
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
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() # Pop corresponding minimum value

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
