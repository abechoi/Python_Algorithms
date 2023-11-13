def get_concatenation(nums: list[int]) -> list[int]:

    ans = []
    # Amortized Complexity - adding elements take constant time, O(1), not O(n).
    # In math it has to do with power series.
    for i in range(2):
        for n in nums:
            ans.append(n)
            print(ans)
    return ans



if __name__ == "__main__":
    my_array = [1,3,2,1]

    print(get_concatenation(my_array))
