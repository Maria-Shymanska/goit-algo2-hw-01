import random

def quick_select(arr, k):
    """
    Find the k-th smallest element in an unsorted array using the Quick Select algorithm.
    k is 1-based: k=1 means the smallest element.
    """
    if not 1 <= k <= len(arr):
        raise ValueError("k is out of bounds")

    pivot = random.choice(arr)
    
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k <= len(lows):
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        return pivot
    else:
        return quick_select(highs, k - len(lows) - len(pivots))


arr = [7, 10, 4, 3, 20, 15]
k = 3
result = quick_select(arr, k)
print(f"The {k}-th smallest element is: {result}")
