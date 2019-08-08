def get_indices_of_item_wights(arr, limit):  
    """
    Given a list of integers 'arr' and a value 'limit', return
    the indices [i, j] of two integers arr[i] and arr[j] whose sum
    is 'limit' (i > j). If there are no two integers, return
    an empty list.
    """
    # Dictionary of visited integers
    D = {}
    # Iterate over array
    for j, val in enumerate(arr):
        y = limit - val
        # Found matching integer -> return indices
        if y in D:
            return [j, D[y]]
        # Update dict with latest integer
        D[val] = j
    # Traversed full array with no solution -> return empty list
    return []

