# reference : https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1?page=1&status=unsolved&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions


def is_subset(a1, a2):
    # Create a dictionary to store the counts of elements in a1
    counts = {}
    for num in a1:
        counts[num] = counts.get(num, 0) + 1
    
    # Iterate over the elements of a2 and check if each element exists in counts
    # If it does, decrement its count in counts
    # If it doesn't, return No
    for num in a2:
        if counts.get(num, 0) > 0:
            # If the count of num is greater than 0, decrement its count
            counts[num] -= 1
        else:
            # If the count of num is 0 or num doesn't exist in counts, return "No"
            return "No"
    
    # If all elements of a2 are found in a1 with sufficient counts,
    # return Yes, indicating that a2 is a subset of a1
    return "Yes"

# Example usage
a1 = [11, 7, 1, 13, 21, 3, 7, 3]
a2 = [11, 3, 7, 1, 7]
print(is_subset(a1, a2)) 


 