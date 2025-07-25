import time

class Solution:
    def isPalindrome_rev(self, x:int)->bool:
        if x < 0:
            return False    
        org = x
        rev = 0
        while(0<x):
            rev = rev*10 + x%10
            x = x//10
        
        return rev==org
        

    def isPalindrome_vec(self, x: int) -> bool:
        ret = True
        if x < 0:
            return False
        
        x_s = str(x)
        s_len = len(x_s)
        idx_half = s_len//2
        idx_max = s_len - 1 
        for i in range(idx_half):
            if not x_s[i] == x_s[idx_max-i]:
                ret = False
                break
        
        return ret

    def isPalindrome_str(self, x: int) -> bool:
        ret = True
        if x < 0:
            return False
        
        x_s = str(x)
        s_len = len(x_s)
        idx_half = s_len//2
        idx_max = s_len - 1 
        for i in range(idx_half):
            if not x_s[i] == x_s[idx_max-i]:
                ret = False
                break
        
        return ret
    
    def isPalindrome_str_simple(self, x: int) -> bool:
        if x < 0:
            return False
        x_s = str(x)
        return x_s == x_s[::-1]


# ベンチマーク関数
def benchmark(func, x, loops=100000):
    start = time.time()
    for _ in range(loops):
        func(x)
    end = time.time()
    return end - start

if __name__ == "__main__":
    # テストする値（11桁の回文数）
    test_value = 123456789877562949033726583123456789877562949033726583123456789877562949033726583123456789877562949033726583123456789877562949033726583123456789877562949033726583
    loops = 100000

    sol = Solution()
    print(f"Testing with value: {test_value}, loops: {loops}")
    print("------")

    t1 = benchmark(sol.isPalindrome_rev, test_value, loops)
    print(f"Reverse version time:  {t1:.6f} seconds")

    t2 = benchmark(sol.isPalindrome_vec, test_value, loops)
    print(f"Vector version time:  {t2:.6f} seconds")

    t3 = benchmark(sol.isPalindrome_str, test_value, loops)
    print(f"String version time:  {t3:.6f} seconds")

    t4 = benchmark(sol.isPalindrome_str_simple, test_value, loops)
    print(f"String simple version time:  {t4:.6f} seconds")