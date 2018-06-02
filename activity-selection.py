def actSelect(s, f):
    """
    Given n activities with their start and finish times. 
    Select the maximum number of activities that can be perform by a single person. 
    A person can only work on a single activity at a time.
    """
    n = len(s)
    act = [0]   # first activity should be selected
    k = 0
    for i in range(1, n):
        if s[i] >= f[k]:    # the start time of the activity should greater than or equal to the finish time of the last selected activity
            act.append(i)
            k = i
    return act

if __name__ == '__main__':
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]  # must be sorted
    act = actSelect(s, f)
    print(act)
