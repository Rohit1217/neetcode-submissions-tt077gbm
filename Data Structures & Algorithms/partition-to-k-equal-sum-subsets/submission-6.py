class Solution:
    def canPartitionKSubsets(self, nums, k):
        total = sum(nums)

        if total % k:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        bucket = [0] * k

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):

                if bucket[j] + nums[i] > target:
                    continue

                bucket[j] += nums[i]

                if dfs(i + 1):
                    return True

                bucket[j] -= nums[i]

                # symmetry breaking
                if bucket[j] == 0:
                    break

            return False

        return dfs(0)