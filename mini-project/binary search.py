lst = [1,3,2,4,5,6,9,8,7,10] # index = [0,1,2....n]
lst.sort() # list = [1,2,3,4,5,6,7,8,9,10]
print(lst)
firstIndex=0
lastIndex=len(lst)-1 # Here computer, starts from number 1 while counting length of list 
                    # And for determining postion of items of an list, it start from 0

midIndex = (firstIndex+lastIndex)//2 # 4.5 it will determine as 4
item = int(input("enter the number to be search")) # user inputed 2
found = False
while( firstIndex<=lastIndex and not found):
    midIndex = (firstIndex + lastIndex)//2
    if lst[midIndex] == item :
         print(f"found at location {midIndex}")
         found= True
    else:
        if item < lst[midIndex]:
            lastIndex = midIndex - 1
        else:
            firstIndex = midIndex + 1 
   
if found == False:
    print("Number not found")