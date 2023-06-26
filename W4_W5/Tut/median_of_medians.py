import quickslect_quicksort as qs


#not completed
def median_of_medians(arr):
    if len(arr) < 5:
        return qs.quicksort_random(arr, 0, len(arr)-1)[len(arr)//2]

    #lists with length of 5 of list
    #uses list slicing and a list comprehension to divide the
    #input array arr into sublists of at most 5 elements each
    #< 5, become a new list with length < 5
    #7 => list1 (len = 5), list 2 (len = 2)
    #list slicing does not raise an IndexError even if the indices are out of range
    #sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    #medians = [qs.quicksort_random(arr, 0, len(arr-1)[len(

        
    
def find_median(arr):
    n = len(arr)
    if n % 2 == 1:
        return qs.quickselect(arr, 0, n-1, n//2)

    if n % 2 == 0:
        return 0.5 * (qs.quickselect(arr, 0, n-1, n//2-1) + qs.
                      quickselect(arr, 0, n-1, n//2+1))


def quicksort_median(arr,low,high):
    n = len(arr)
    if low < high:
        p = find_median(arr)
        #p is the pivot in the correct position, so leave this alone)
        qs.quicksort_random(arr, low, p-1)
        qs.quicksort_random(arr, p+1, high)

