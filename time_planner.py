def meeting_planner(slotsA, slotsB, dur):
    """
    Given the availability of two people and a meeting duration 
    return the earliest time slot that works for both of them 
    and is of duration dur.
    """
    if not slotsA:
        return []
    if not slotsB:
        return []
    # Indices
    a = 0
    b = 0
    while a < len(slotsA) and b < len(slotsB):
        # Intervals
        A_int = slotsA[a]
        B_int = slotsB[b]
        # Starts
        start = max(A_int[0], B_int[0])
        # Ends
        end = min(A_int[1], B_int[1])
        # Found time slot
        if end - start >= dur:
            return [start, start+dur]
        # Increment interval
        if A_int[1] >= B_int[1]:
            b += 1
        else:
            a += 1
    # If no slot found, return empty array.
    return []

