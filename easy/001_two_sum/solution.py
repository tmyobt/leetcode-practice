
from typing import List, Callable, Any
import time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

def test(func: Callable, answer,  *args) -> bool:
    output = func(*args)
    ret =  (answer == output )
    return ret

def benchmark(func: Callable, loops: int = 10000, *args) -> float:
    start = time.time()
    for _ in range(loops):
        func(*args)
    end = time.time()
    return end - start

def run_all_test(solution_instance: Any, answer: Any, *args):
    methods = get_methods(solution_instance)
    for name, method in methods:
        ret = test(method, answer, *args)
        print(f"{name}: {ret}") 

def run_all_benchmark(solution_instance: Any, loops: int, *args):
    methods = get_methods(solution_instance)
    
    for name, method in methods:
        t = benchmark(method, loops, *args)
        print(f"{name}: {t:.6f} sec")

def get_methods(solution_instance: Any):
    return [
        (name, getattr(solution_instance, name))
        for name in dir(solution_instance)
        if callable(getattr(solution_instance, name)) and not(name.startswith("_"))
    ]

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    output = [0,1]
    loops = 10000

    sol = Solution()
    run_all_test(sol, output, nums, target)

    print(f"Benchmarking all methods with: loops={loops}")
    print("------")
    run_all_benchmark(sol, loops, nums, target)