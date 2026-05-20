class Solution(object):
    # brutal force
    def decrpyt(self, k, code):
        n = len(code)
        res = [0]*n

        if k==0:
            return res
        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k+1):
                    total += [(i+j)%n]

            if k<0:
                for j in range(1, abs(k)+1):
                    total += [(i-j)%n]
            res[i] = total
        return res
    
k = 3
code = [2, 4, 5, 6, 7]