def countingSort(new_list):
    #find max value
    max_item = new_list[0]
    for item in new_list:
        if item >max_item:
            max_item = item
                       

    #create count_array
    #off by 1
    count_array = [0]*(max_item + 1)
    for item in new_list:
        count_array[item] += 1

        
    #update input list with count_array
    index = 0 #for updating input list from first index
    for i in range(len(count_array)):
        item = i
        frequency = count_array[i]

        for j in range(frequency):
            new_list[index] = item
            index += 1


    return new_list

        
        
