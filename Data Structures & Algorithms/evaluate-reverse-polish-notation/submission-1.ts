class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens: string[]): number {
        const stack: number[] = []
        for (const t of tokens) {
            if (t === "+") {
                let b = stack.pop()!;
                let a = stack.pop()!;
                stack.push(a + b)
            }
            else if (t === "-") {
                let b = stack.pop()!;
                let a = stack.pop()!;
                stack.push(a - b)
            }
            else if (t === "*") {
                let b = stack.pop()!;
                let a = stack.pop()!;
                stack.push(a * b)
            }
            else if (t === "/") {
                let b = stack.pop()!;
                let a = stack.pop()!;
                stack.push(Math.trunc(a / b))
            }
            else {
                stack.push(Number(t))
            }
        } 
        return stack.pop()
    }
}
