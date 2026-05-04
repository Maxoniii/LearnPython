def merge_sorted_lists(s1, s2):
    merged_set = set(s1) | set(s2)

    return sorted(merged_set)



s1 = [1,3,5,7,9]
s2 = [2,4,6,8,10]
print(merge_sorted_lists(s1, s2))  
