#binary search algo

def binary_search_algo(array, target):
    first=0
    last=len(array)-1

    # mid=(first+last)//2

    # arr=len(array)-1/
    while first<=last:
        mid=(first+last)//2

        if target == array[mid]:
            return mid

        elif target > array[mid]:
            last=mid-1

        elif target < array[mid]:
            first = mid + 1


        return "No element found"

target=int(input("enter the element"))
array=[9,3,6,99,4,1,2,44,6,2,-4,-6,-2]

binary_search_algo(list, array)