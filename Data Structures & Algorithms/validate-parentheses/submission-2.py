class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        left = {
            '(':1,
            '{':2,
            '[':3
            }
        right = {
            ')':1,
            '}':2,
            ']':3
        }

        for char in s:
            if char in right:
                if not stack:
                    return False

                pair = stack.pop()
                if left.get(pair) != right.get(char):
                    return False
                else:
                    continue
            else:
                stack.append(char)
        return not stack