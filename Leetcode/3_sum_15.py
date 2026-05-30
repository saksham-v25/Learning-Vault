class Solution:
    def threeSum(self, a: list[int]) -> list[list[int]]:

        a.sort()
        res = []
        n = len(a)

        for i in range(0, n - 2):

            if i > 0 and a[i] == a[i - 1]:
                continue

            l = i + 1
            r = n - 1
            sum = -1 * a[i]

            while l < r:
                s = a[l] + a[r]

                if s == sum:
                    res.append([a[i], a[l], a[r]])
                    l += 1
                    r -= 1

                    while l < n and a[l] == a[l - 1]:
                        l += 1

                    while r >= 0 and a[r] == a[r + 1]:
                        r -= 1

                elif s < sum:
                    l += 1

                else:  # (s > sum)
                    r -= 1

        return res