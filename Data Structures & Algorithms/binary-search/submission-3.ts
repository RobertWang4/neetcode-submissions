class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let l = 0;
        let r = nums.length - 1;
        while (l <= r){
            let n = l + Math.trunc((r - l) / 2)
            if (nums[n] < target){
                l = n + 1;
            } else if (nums[n] > target){
                r = n - 1;
            } else {
                return n;
            }
        }
        return -1;
    }
}
