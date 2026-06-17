class Solution:
    def maximumSum(self, arr):

        nodelete = arr[0]
        onedelete = float('-inf')
        result = arr[0]

        for i in range(1, len(arr)):

            prev_nodelete = nodelete
            prev_onedelete = onedelete

            nodelete = max(nodelete + arr[i], arr[i])

            if prev_onedelete == float('-inf'):
                v1 = arr[i]
            else:
                v1 = prev_onedelete + arr[i]

            onedelete = max(v1,prev_nodelete)

            result = max(result, max(nodelete, onedelete))

        return result