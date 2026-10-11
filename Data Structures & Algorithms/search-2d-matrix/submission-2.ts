class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
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
    searchMatrix(matrix: number[][], target: number): boolean {
        let l = 0;
        let r = matrix.length - 1;
        while (l <= r){
            if (matrix[l][matrix[l].length - 1] >= target){
                return this.search(matrix[l],target) !== -1;
            } else if (matrix[r][0] <= target){
                return this.search(matrix[r],target) !== -1;
            } else {
                let m = Math.trunc((r - l)/2);
                if (matrix[m][0] > target){
                    r = m - 1
                } else if (matrix[m][matrix[m].length - 1] < target){
                    l = m + 1
                } else {
                    return this.search(matrix[m],target) !== -1;
                }
            }
        }
    }
}
