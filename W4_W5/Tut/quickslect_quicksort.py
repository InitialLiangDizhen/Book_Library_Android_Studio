import random

#startdart partion
def partition(arr,low,high):
    pivot = arr[low]
    #the arr[low] has been already swapped with arr[random_pivot]

    i = low
    j = high + 1

    while True:
        i += 1
        while arr[i] <= pivot: #unstable
            i += 1

        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j: #if the index i >= index j, the array is finished
            return j #so return j index
        #otherwise, perform swapping, move on
        arr[i], arr[j] = arr[j], arr[i]
        #every swap would know its own position




#to use as recursion must have arr, low, high and k to do recursion
#return kth smallest element, (k=0) th element is the smallest of the array

#index < what we want? repeat for right portion of list
#next round, pick a random pivot and start again
def quickselect(arr,low, high, k):
    #low = 0 index 0
    #high = len(arr)-1


    p = Hoares_petition(arr, low, high) #get a fixed index
    #until pivot = k 
    if k == p:
        return arr[k]
    #go into either one
    elif k < p:                  #into left-hand side
        return quickselect(arr, low, p-1, k)
    else:
        return quickselect(arr, p+1,high, k)



def Hoares_petition(arr, low, high):
    #get random pivot every time
    #then

    #get random pivot
    r = random.randint(low, high)

    arr[low], arr[r] = arr[low], arr[r]
    return Hoares_main_petition(arr, low, high)

def Hoares_main_petition(arr, low, high): #notmaining relative order ,not stable
    #pointers
    i = low + 1
    j = high

    pivot = arr[low]

    while i <= j:
        
        if arr[i] < pivot: #not <= to avoid breaking stability
            i += 1

        elif arr[j] > pivot:
            j -=1

        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1


    #now i = j, pointing the same element
    #final swap with pivot which would possiblely break stability
    arr[low], arr[j] = arr[j], arr[low]
    return j #return the index of the pivot


#Hoare's petition
#Q6 # quicksort = basically let the Hoare's petition repetively do the work of swapping
# by applying recursively on the left half and right half
def quicksort_random(arr,low,high):
    if low < high: #either low >= high, whole list is sorted,
        p = Hoares_petition(arr, low, high)#since size of list keep shrinking, need to get new pivot
        #p is already in correct order, so should not touch it
        quicksort_random(arr,low,p-1) #repeat on left of the pivot
        quicksort_random(arr,p+1, high)

    return arr

# def dutch_national(arr, low, high):
#     j = low
#
#     #part of the arry that is less than pivot
#     blue_boun = low
#     #part of the array that is greater than pivot
#     red_boun = high
#
#     # get random pivot
#     pivot = random.randint(low, high)
#
#     while j <= red_boun:
#         #arr[j] belongs to blue part of the array < pivot
#         if arr[j] < pivot:
#             if arr[blue_boun] == pivot:
#                 arr[blue_boun], arr[j] = arr[j], arr[blue_boun]
#             else:
#                 blue_boun+=1
#         #array[j] belongs to red part of the array > pivot
#         elif arr[j] > pivot:
#             if arr[red_boun] == pivot:


    

if __name__ == '__main__':
    arr = [2,72,6,3,72,74,7,2,5]
    low = 0
    high = len(arr)-1
    qr = quicksort_random(arr, low, high)
    print(qr)