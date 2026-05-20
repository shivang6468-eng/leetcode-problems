class Solution:
    def romanInt(self, s):
        letter = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        result = 0
        n = len(s)

        for i in range(n):
            if i+1 < len(s) and letter[s[i]] < letter[s[i+1]]:
                result -= letter[s[i]]
            else:
                result += letter[s[i]]
        return result

s = input("Enter the roman number(in capitalize letter): ")
sol  = Solution()
print("Intger value is: ", sol.romanInt(s))

