import time
from typing import List, Callable, Any
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for chars in zip(*strs):
            if(len(set(chars)) == 1):
                prefix = prefix + chars[0]
            else:
                break
        return prefix


# ベンチマーク関数
def benchmark(func, x, loops=100000):
    start = time.time()
    for _ in range(loops):
        func(x)
    end = time.time()
    return end - start

if __name__ == "__main__":
    # テストする値（11桁の回文数）
    test_value = ["flower", "flex", "float"]
    loops = 100000

    sol = Solution()
    print(f"Testing with value: {test_value}, loops: {loops}")
    print("------")

    t = benchmark(sol.longestCommonPrefix, test_value, loops)
    print(f"Reverse version time:  {t:.6f} seconds")
