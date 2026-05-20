class Sol(object):
    # for time complexity of O(n^2)
    def twosum(self, target, num):
        n = len(num)
        for i in range(0, n-1):
            for  j in range(i+1, n):
                if num[i] + num[j] == target:
                    return [i,j]
    
    # for time complexity of O(n)
    def twoSum(self, target, num ):
        n = len(num)
        dic = {}
        for i in range(0, n):
            rem = target - num[i]
            if rem in dic:
                return [dic[rem], i]
            dic[num[i]] = i

target = 13
num = [3, 2, 1, 5, 4, 9, 4]

result  = Sol()
print(result.twosum(target, num))  #brute force
print(result.twoSum(target, num)) #optimize