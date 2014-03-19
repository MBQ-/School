def remove_adjacent_duplicates2(old_list):
    new_list = []
    first_element_of_old_list = old_list[0]
    new_list.append(first_element_of_old_list)
    
    index = 1
    
    while index < len(old_list):
        if old_list[index] != old_list[index - 1]:
            new_list.append(old_list[index]);
            
        index += 1
            
    return new_list
