class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        count = {}

        for i in range(len(numbers)):
            tar = target - numbers[i] 
            if tar in count:
                return [count.get(tar),i+1]
            else:
                count[numbers[i]] = i+1
        