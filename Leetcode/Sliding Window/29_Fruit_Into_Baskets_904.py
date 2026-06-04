class Solution:
    def totalFruit(self, fruits):
        low = 0
        high = 0
        freq = {}
        res = 0

        for high in range(len(fruits)):
            fruit = fruits[high]

            if fruit in freq:
                freq[fruit] += 1
            else:
                freq[fruit] = 1

            while len(freq) > 2:
                left_fruit = fruits[low]
                freq[left_fruit] -= 1

                if freq[left_fruit] == 0:
                    del freq[left_fruit]

                low += 1

            
            res = max(res, high - low + 1)

        return res
