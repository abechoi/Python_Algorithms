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
    nums = [0,1,2,3,4,2,2,3,3,4]
                  l
    """


if __name__ == "__main__":

    my_array = [0,0,1,1,1,2,2,3,3,4]

    output= remove_duplicates(my_array)

    print(output)