import random

def find_max_min(arr):
    """
    Determine the minimum and maximum elements in an array using a divide-and-conquer approach.
    Returns a tuple (min_value, max_value).
    """
    if not arr:
        raise ValueError("Input array must not be empty")
    
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        return min(arr), max(arr)
    
    mid = len(arr) // 2
    left_min, left_max = find_max_min(arr[:mid])
    right_min, right_max = find_max_min(arr[mid:])
    
    return min(left_min, right_min), max(left_max, right_max)

# Create random array with 20 numbers from -100 to 100
random_array = [random.randint(-100, 100) for _ in range(20)]

print("Array:", random_array)

min_val, max_val = find_max_min(random_array)
print("Min:", min_val)
print("Max:", max_val)
