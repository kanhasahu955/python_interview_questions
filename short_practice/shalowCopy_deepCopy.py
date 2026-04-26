from copy import deepcopy, copy

#######################################
############ Shalow Copy ##############
#######################################

############ Top level ################

original_list = [1,2,3,4,5]

# shallow_copy = original_list
# shallow_copy = copy(original_list)

# shallow_copy.append(6)
# original_list.append(7)

# print("Original Copy address:", id(original_list))
# print("Shallow Copy address:", id(shallow_copy))

# print("Original Copy:", original_list)  # Output: [1, 2, 3, 4, 5, 7]
# print("Shallow Copy:", shallow_copy)  # Output: [1, 2, 3, 4, 5, 6]


################## nested list ##################
# original_list = [[1,2,3], [4,5,6]]    

# shallow_copy = copy(original_list)
# shallow_copy[0].append(7)
# original_list[0].append(8)
# print("Original Copy:", original_list)  # Output: [[1, 2, 3, 7, 8], [4, 5, 6]]
# print("Shallow Copy:", shallow_copy)   # Output: [[1, 2, 3, 7, 8], [4, 5, 6]]


#######################################
############ Deep Copy ##############
#######################################

############ Top level ################

# original_list = [1,2,3,4,5]

# deep_copy = original_list
# deep_copy = deepcopy(original_list)

# deep_copy.append(6)
# original_list.append(7)

# print("Original Copy:", original_list)  # Output: [1, 2, 3, 4, 5, 7]
# print("Deep Copy:", deep_copy)  # Output: [1, 2, 3, 4, 5, 6]

################## nested list ##################
# original_list = [[1,2,3], [4,5,6]]    
# deep_copy = deepcopy(original_list)
# deep_copy[0].append(7)
# original_list[0].append(8)
# print("Original Copy:", original_list)  # Output: [[1, 2, 3, 7, 8], [4, 5, 6]]
# print("Deep Copy:", deep_copy)   # Output: [[1, 2, 3, 7], [4, 5, 6]]
