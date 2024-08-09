def get_n_longest_unique_words(words, n):
    new_lst =[]
    dup_lst = list(set([item for item in words if words.count(item) > 1]))

    new_wrd_lst = list(set(words) - set(dup_lst))
    new_wrd_lst.sort(key=len,reverse=True)
   
    #new_wrd_lst = new_wrd_lst[:-n]
    for i in range(0,n):
            new_lst.append(new_wrd_lst[i])
            n = n-1

    return new_lst

    

    