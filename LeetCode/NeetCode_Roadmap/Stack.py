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
        """
        #22

        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

        Example 1:
        Input: n = 3
        Output: ["((()))","(()())","(())()","()(())","()()()"]

        Example 2:
        Input: n = 1
        Output: ["()"]

        NOTE: Needed help on this one. Logic goes:
        1. We need a way to determine if a given pattern is considered "finished" -> Any finished pattern will
            contain 2n tokens
        2. If we start open and close at 0, then they represent how many more open and close parenthesis that
            we can add to the pattern
        3. Thus, open_paren < n means that we still have more open parenthesis to add
        4. Similarly, if open_paren > close_paren, that means that we've added an open parenthesis that we can
            close.

        n = 0 -> returns [] since 0 = 0*2

        n = 1 -> returns ["()"] since we start with open, then since open = n (1) we do a close. At this point
            both open and close are 1, and the first pattern is formed. Tracing back the stack of operations,
            since open and close are still equal in the first iteration, we're done.

        n = 2:
            ( -> (( -> (() -> (())
              -> () -> ()( -> ()()
        """
        def _helper(pattern: str, open_paren: int, close_paren: int) -> str:
            if len(pattern) == 2*n:
                result.append(pattern)
                return

            if open_paren < n:
                _helper(pattern + "(", open_paren + 1, close_paren)

            if open_paren > close_paren:
                _helper(pattern + ")", open_paren, close_paren + 1)

        result = []
        _helper("", 0, 0)
        return result


    def daily_temperatures(self, temperatures: List[int]) -> List[int]:
        """
        #739

        Given an array of integers temperatures represents the daily temperatures, return an array
        answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.

        If there is no future day for which this is possible, keep answer[i] == 0 instead.

        Notes:
        * 30 <= temperatures[i] <= 100
        """
        # # Slow brute force approach
        # n = len(temperatures)
        # results = [0] * n

        # # Temperatures can have duplicates
        # temp_map = defaultdict(list)
        # for i, temp in enumerate(temperatures):
        #     temp_map[temp].append(i)

        # for i, temp in enumerate(temperatures):
        #     closest_index = n
        #     for other_temp in range(temp + 1, 101):
        #         if other_temp in temp_map:
        #             indices = temp_map[other_temp]
        #             for index in indices:
        #                 if index > i:
        #                     closest_index = min(closest_index, index)

        #     if closest_index != n:
        #         results[i] = closest_index - i

        # return results

        # # Go backwards
        # n = len(temperatures)
        # results = [0] * n

        # # Here we set temp_map to be regular dict because if we encounter the same
        # # temp number going backwards, we will pick the earliest highest temp, so
        # # same temp but more in the future doesn't matter!
        # temp_map = {}
        # for i in range(n - 1, -1, -1):
        #     temp = temperatures[i]
        #     temp_map[temp] = i

        #     closest_index = n
        #     for higher in range(temp + 1, 101):
        #         if higher in temp_map:
        #             closest_index = min(closest_index, temp_map[higher])

        #     if closest_index != n:
        #         results[i] = closest_index - i

        # return results

        # Stack Solution - faster and more efficient
        results = [0] * len(temperatures)
        stack = deque()

        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temperatures[stack[-1]] < temp:
                colder_index = stack.pop()
                results[colder_index] = i - colder_index

            stack.append(i)

        return results

    def car_fleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        #853

        There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.

        You are given two integer array position and speed, both of length n, where position[i] is the starting
        mile of the ith car and speed[i] is the speed of the ith car in miles per hour.

        A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.

        A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.

        If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.

        Return the number of car fleets that will arrive at the destination.

        Example 1:
        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        Output: 3
        Explanation:
            The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
            The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
            The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

        Example 2:
        Input: target = 10, position = [3], speed = [3]
        Output: 1
        Explanation:
        There is only one car, hence there is only one fleet.

        Example 3:
        Input: target = 100, position = [0,2,4], speed = [4,2,1]
        Output: 1
        Explanation:
            The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
            Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
        """
        n = len(position)
        cars = {}
        for i in range(n):
            curr = position[i]
            if curr in cars:
                if speed[i] < cars[curr][0]:
                    cars[curr][0] = speed[i]
            else:
                cars[position[i]] = [speed[i], 0]



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
