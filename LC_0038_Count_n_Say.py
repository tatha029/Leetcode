class Solution:
    def countAndSay(self, n: int) -> str:
        def say(x: str) -> str:
            say_x, ctr, v = "", 0, x[0]
            for i in x:
                if v == i:
                    ctr += 1
                else:
                    say_x += str(ctr) + v
                    v, ctr = i, 1
            say_x += str(ctr) + v
            return say_x

        for i in range(n):
            if i == 0:
                say_x = "1"
            else:
                say_x = say(say_x)
        return say_x
