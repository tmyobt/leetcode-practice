import time

class Solution:
    symbols = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    
    def romanToInt(self, s: str) -> int:
        ret = 0
        prev_roman = "I"
        for i in reversed(s):
            if (self.symbols[prev_roman] > self.symbols[i]):
                ret = ret - self.symbols[i]
            else:
                ret = ret + self.symbols[i]
            prev_roman = i
        return ret


# ベンチマーク関数
def benchmark(func, x, loops=100000):
    start = time.time()
    for _ in range(loops):
        func(x)
    end = time.time()
    return end - start

if __name__ == "__main__":
    # テストする値（11桁の回文数）
    test_value = "MCMXCIV"
    loops = 100000

    sol = Solution()
    print(f"Testing with value: {test_value}, loops: {loops}")
    print("------")

    t = benchmark(sol.romanToInt, test_value, loops)
    print(f"Reverse version time:  {t:.6f} seconds")
