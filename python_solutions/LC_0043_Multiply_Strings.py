class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        l1, l2 = len(num1), len(num2)
        x, ans = [], 0
        for i in range(l1):
            for j in range(l2):
                power = l1 + l2 - i - j - 2
                x.append(int(num1[i]) * int(num2[j]) * 10**power)
        ans = sum(x)
        return str(ans)
        """
        return str(sum([int(num1[i]) * int(num2[j]) * 10**(len(num1+num2)-i-j-2) \
                        for i in range(len(num1)) for j in range(len(num2))]))
