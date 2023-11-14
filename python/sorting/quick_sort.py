
def partition(arr, low, high):
    z = low - 1
    for j in range(low, high):
        if arr[j] <= arr[high]:
            z += 1
            arr[z], arr[j] = arr[j], arr[z] # Makes sure that up to index z, all elements are sorted ascendently
    z += 1
    arr[z], arr[high] = arr[high], arr[z] # Puts arr[high] at the end of sorted elements, making them sorted until index z
    return z # Returns the index of the last sorted elements

def sort_quick(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        print(pivot)
        arr = sort_quick(arr, pivot+1, high)
        print(arr)
        arr = sort_quick(arr, low, pivot-1) #I don't understand: In our choice of the pivot as the last element, everything before pivot should already be sorted. Maybe it is sorted compared to the elements in this slice but not sorted for the whole array? 
        print(arr)
    return arr

def quick_sort(arr):
    if len(arr) < 2:
        return arr

    return sort_quick(arr, 0, len(arr)-1)


print(quick_sort([3, 5 , 8, 454 ,45, 89 ,68 , -8, -91, 5, 91]))

t  = input()

def quick_sort_pythonic(z):
    if(len(z)>1):
        piv=int(len(z)/2)
        val=z[piv]
        lft=[i for i in z if i<val]
        mid=[i for i in z if i==val]
        rgt=[i for i in z if i>val]

        res=quicksort(lft)+mid+quicksort(rgt)
        return res
    else:
        return z
