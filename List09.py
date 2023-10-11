def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    j=0
    i=0
    while i<len (list1)-1:
        if list1[i]==list1[i+1]:
            j=j
        else:
            j+=1
        i+=1
    return not bool(j)
print(main([0, 0, 0, 0, 0]))