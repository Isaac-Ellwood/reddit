# Step 1: Create a blank list of lists with 5 inner lists
list_of_lists = [[]]
list_of_lists.append([0])
list_of_lists.append([3])
list_of_lists.append([])
list_of_lists.append([])
list_of_lists.append([])
list_of_lists.append([])
list_of_lists.append([])
list_of_lists.append([])
# Step 2: Add number 42 to the inner list at index 2
list_of_lists[2].append(42)

# Step 3: Add number 7 to the inner list at index 2
list_of_lists[2].append(7)

# Add a number to another index, e.g., index 3
list_of_lists[3].append(99)

# Print the list of lists to see the result
print(list_of_lists)