import time

class Solution:
    pairs = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    def isValid(self, s: str) -> bool:
        l = []
        for c in s:
            if c in self.pairs:
                l.append(c)
            else:
                if len(l) == 0 or not c == self.pairs[l.pop()]:
                    return False
        
        if len(l) == 0:
            return True
        else:
            return False


# ベンチマーク関数
def benchmark(func, x, loops=100000):
    start = time.time()
    for _ in range(loops):
        func(x)
    end = time.time()
    return end - start

if __name__ == "__main__":
    test_value = "()[]{}"
    loops = 100000

    sol = Solution()
    print(f"Testing with value: {test_value}, loops: {loops}")
    print("------")

    t = benchmark(sol.isValid, test_value, loops)
    print(f"Reverse version time:  {t:.6f} seconds")




        