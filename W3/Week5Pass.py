import timeit

ALPHABET_SIZE = 97
#################################################################### Implementation of Basic Counting Sort with Numbers ####################################################################
def counting_sort_numbers(lst):
    """
    The implementation of a stable counting sort for integers 
    Time Complexity: O(M+N), where M is the maximum value in the list, and where N is the length of the input list(lst)
    Aux Space Complexity: O(M+N), where M is the maximum value in the list, and where N is the length of the input list(lst)
    """
    return_array = [] 
    if len(lst) == 0:
        return return_array 
    
    #Finding max is O(N) time, initializing count_array of max length is O(M) time and aux space
    count_array = [None]*(max(lst)+1)
    for i in range(len(count_array)):
        count_array[i] = []
    
    #Filling up our count_array, O(N)
    for current_item in lst:
        #this will append the ideentical number in order which maintain stability
        count_array[current_item].append(current_item)
    
    # print(count_array)
    #Appending everything to our return_array, O(M+N) time, not O(MN)!
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            #like adjancy_list
            return_array.append(count_array[i][j])
    
    return return_array 
# print(counting_sort_numbers([3,6,1,2,9,7,7,2]))

#################################################################### Implementation of Basic Counting Sort with Alphabets ####################################################################
def counting_sort_alphabets(lst):
    """
    The implementation of a stable counting sort for alphabets 
    Time Complexity: O(N), where N is the length of the input list(lst)
    Aux Space Complexity: O(N), where N is the length of the input list(lst)
    """
    return_array = []
    if len(lst) == 0:
        return return_array 

    #Initializing count_array is O(1)
    count_array = [None]*26
    for i in range(len(count_array)):
        count_array[i] = [] 
    
    #Filling up our count_array, O(N)
    for current_alphabet in lst: 
        count_array[ord(current_alphabet)-97].append(current_alphabet)
    
    # print(count_array)
    #Appending everything to our return_array, O(N)
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            return_array.append(count_array[i][j])
    
    return return_array

# print(counting_sort_alphabets(["a","c","b","z","x","g","d","c","a"]))

#################################################################### Implementation of a Basic Radix Sort ####################################################################
def counting_sort_for_radix(lst, position):
    """
    The implementation of a stable counting sort to be used for radix sort
    Time Complexity: O(N), where N is the length of the input list(lst)
    Aux Space Complexity: O(N), where N is the length of the input list(lst)
    """
    return_array = []
    if len(lst) == 0:
        return return_array 

    #make each element to be individual list
    count_array = [None]*26 
    for i in range(len(count_array)):
        count_array[i] = [] 
    
    for current_item in lst:
        #if it is number
        #base = 10
        #K = log10 max(lst)
        #for i in K:
        # col = i
        #(number // (base^col)) % base
        count_array[ord(current_item[position])-97].append(current_item)
    
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            return_array.append(count_array[i][j])
    
    return return_array

def radix_sort(lst):
    """
    Implementation of a radix sort, which is basically just calling counting sort multiple times 
    Time Complexity: O(kN), where k is the number of columns to determine the amount of times we have to call counting sort 
    Aux Space Complexity: O(N), where N is the lenght of the input list(lst)
    """
    #get the K - columns, times to run counting sort
    iteration_needed = len(lst[0])
    return_array = lst 
    for i in range(iteration_needed):
        position = iteration_needed - (i+1)
        return_array = counting_sort_for_radix(return_array, position)
        # print(return_array)
    return return_array 

# print(radix_sort(["abc","baa","qvs","zbc"]))

#################################################################### Implementation of a Flexible Radix Sort with different bases ####################################################################
def flexible_counting_sort(lst, position, base):
    """
    The implementation of a counting sort that is flexible in terms of bases to be used for radix sort
    Time Complexity: O(N+B), where N is the length of the input list(lst), and B is our base 
    Aux Space Complexity: O(N+B), where N is the length of the input list(lst), and B is our base
    """
    return_array = [] 
    if len(lst) == 0:
        return return_array 

    #Initializing our count_array based on the base, O(B)
    count_array = [None]*base
    for i in range(len(count_array)):
        count_array[i] = [] 
    
    #Filling up our count_array, O(N)
    for current_item in lst: 
        count_array[(current_item//(base**position))%base].append(current_item)
    
    #Appending everything back to our return_array, O(N+B)
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            return_array.append(count_array[i][j])
    
    return return_array 

def flexible_radix_sort(lst, base):
    """
    The Implementation of a radix sort that can be flexible with different bases 
    Time Complexity: O(k(N+B)), where k is the number of columns to determine the amount of times we need to call counting sort, N is the length of the input list(lst), and B is our base
    Aux Space Complexity: O(N+B), where N is the length of the input list(lst), B is our base
    """
    iteration_needed = len(f"{lst[0]}")
    return_array = lst 
    for i in range(iteration_needed):
        return_array = flexible_counting_sort(return_array, i, base)
    return return_array 


# print(flexible_radix_sort([200, 151, 291, 981, 369, 421, 671], 10))
# print(flexible_radix_sort([1101, 1100 ,1011], 2))
# print(flexible_radix_sort([20762216160, 15692626611, 22367821891, 96197173781, 39283328969, 48728464621, 67727992741], 100))
# print(flexible_radix_sort([20762216160, 15692626611, 22367821891, 96197173781, 39283328969, 48728464621, 67727992741], 10))

# start = timeit.timeit()
# REPLACE WITH FUNCTION YOU WANT TO TEST THE RUNTIME OF
# end = timeit.timeit() 
# print(end-start)

#################################################################### END ####################################################################




