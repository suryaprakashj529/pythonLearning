def pairs_sum_to_target(list1, list2, target):
    # Write your code here.
    target_list = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if (list1[i] + list2[j]) == target :
                target_list.append([i,j])
                
    return target_list