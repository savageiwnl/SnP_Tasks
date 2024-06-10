class Solution:
    def sort_list(self, array: list):
        if not array:
            return []
        else:
            x = min(array)
            y = max(array)
            for i in range(0, len(array)):
                if array[i] == x:
                    array[i] = y
                    continue
                if array[i] == y:
                    array[i] = x
            array.append(x)
            return array


arr = [1, 2, 1, 3]
sol = Solution()
res = sol.sort_list(arr)
print(res)
