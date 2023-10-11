def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    i=1
    j=list_num[0]
    while i<len(list_num):
        if list_num[i]>j:
            j=list_num[i]
        i+=1
    return j
print(main([5, 32, 1, 4, 3]))