def binary_search(arr, element, low, high):
    if low <= high:
        mid = (low + high)//2
        if element == arr[mid]:
            return mid
        elif element > arr[mid]:
            return binary_search(arr, element, mid+1, high)
        else:
            return binary_search(arr, element, low, mid-1)
    else:
        return -1
nums = [3,7,9,11,14,19,24,29,39]
user = int(input("Enter the number: "))
low = 0
high = len(nums)- 1
print(binary_search(nums, user,low, high))
