class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(stack, left_count, right_count):
            if left_count == n and right_count == n:
                res.append("".join(stack))
                return

            if left_count < n:
                stack.append("(")
                dfs(stack,left_count+1,right_count)
                stack.pop()
            if right_count < left_count:
                stack.append(")")
                dfs(stack,left_count,right_count+1)
                stack.pop()
        dfs([],0,0)
        return res