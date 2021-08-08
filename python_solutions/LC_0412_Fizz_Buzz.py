class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_list = []
        for i in range(1, n+1):
            if i%15 == 0:
                fizz_list.append("FizzBuzz")
            elif i%5 == 0:
                fizz_list.append("Buzz")
            elif i%3 == 0:
                fizz_list.append("Fizz")
            else:
                fizz_list.append(str(i))
        return fizz_list
