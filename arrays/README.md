### 1. Static Arrays

## Overview

| Operation           | Big-O Time |
| ------------------- |:----------:|
| R / W i-th element  | O(1) |
| Insert / Remove End | O(1) |
| Insert Middle       | O(n) |
| Remove Middle       | O(n) |

Reading through arrays are instant, given the element, because each index is mapped to an address in the RAM. Size of array is irrelevant.

Traversal through an array of size n is O(n).

When removing from the end of the array, replace the last value with `0`, `null`, or `-1`; then reduce array length by 1.

However removing from an i-th index, is different because replacing the i-th value with `0` would break the contiguous nature of the array.

## Remove Duplicates

Given an integer array in ascending order with duplicates, remove duplicate elements. This function will use 2 pointers, `r` the index, and `l` which increments whenever `r` does not equal `r - 1`, and also acts as a count for non-duplicates.

```
def remove_duplicates(nums: list[int]) -> int:
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l
```

To remove duplicates in an array in ascending order, start loop from position 1 and check position 0 using `r - 1`. If `nums[r]` does not equal `nums[r - 1]`, copy `nums[r]` to `nums[l]`, then increment `l`. If `nums[r]` does equal `nums[r - 1]` then simply keep iterating, because there is no need to increment the count, `l`.

## Remove Element

Given an integer array and value to remove, remove all elements that match the value. This function will use 2 pointers, `i` the index, and `k` the number of times `nums[i]` does not match the value.

```
def remove_element(nums: list[int], val: int) -> int:
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
```

To remove matching elements within an array, loop through all elements, and if `nums[i]` does not equal `val`, copy `nums[i]` to `nums[k]`, then increment `k`. This makes it so that `k` only takes on a new value when `nums[i]` does not equal `val`. If `nums[i]` does equal `val`, `i` will keep iterating.