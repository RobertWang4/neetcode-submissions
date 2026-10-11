class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures: number[]): number[] {
        const res: number[] = new Array(temperatures.length).fill(0);
        const stack: [number,number][] = [];
        for (let i = 0; i < temperatures.length; i++){
            while (stack.length >0 && temperatures[i] > stack[stack.length-1][0]){
                const top = stack.pop();
                const stackInd = top[1];
                res[stackInd] = (i - stackInd);
            }
            stack.push([temperatures[i],i]);
        }
        return res
    }
}
