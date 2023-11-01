def remove_duplicates(nums: list[int]) -> int:
    # l is the left pointer and number of unique elements
    l = 1

    # r is the right pointer
    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
        print(f"r = {r}, nums = {nums}")

    return l

    """
                      r  
    nums = [0,1,2,1,1,2,2,3,3,4]
                  l
    """

def remove_element(nums: list[int], val: int) -> int:

    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


    """
                                i      
        my_array = [0,1,2,2,3,0,4,2]
                              k
    """



if __name__ == "__main__":

    # my_array = [0,0,1,1,1,2,2,3,3,4]
    # output= remove_duplicates(my_array)

    my_array = [0,1,2,2,3,0,4,2]
    output = remove_element(my_array, 2)



    print(output)