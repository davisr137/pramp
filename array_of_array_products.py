def cumprod(A):
    """
    Compute cumulative product of array.
    """
    # Pre-allocate memory for array
    A_prod = [1] * len(A)
    # Iterate over values
    for i, val in enumerate(A):
        if i == 0: 
            A_prod[i] = 1
            continue
        A_prod[i] = A_prod[i-1] * A[i-1]
    return A_prod

def array_of_array_products(A):
    """
    Compute array of products of all other
    values other than current value.
    """
    # Empty array
    if not A:
      return []
    # Length one array
    L = len(A)
    if L == 1:
      return []
    # Cumulative product from left and right
    A_left = cumprod(A)
    A_rev = list(reversed(A))
    A_right = cumprod(A_rev)
    # Array of array products
    A_prod = [1] * L
    for i in range(L):
      A_prod[i] = A_left[i] * A_right[L-1-i]
    return A_prod
