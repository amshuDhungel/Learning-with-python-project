def binary_search(arr, element):
    low = 0
    high = len(arr)-1
    found = False
    while (low <= high and not found):
        mid = (low + high)//2
        if arr[mid]== element:
            print(f"found at index {mid}")
            found = True

        else:
            if element < arr[mid]:
                high = mid -1
            else:
                low = mid +1
    if found == False:
        print("Number not found")
    else:
        return

num = [2,4,5,7,8,9,10]
element = int(input("Enter the number: "))
print(binary_search(num, element))        