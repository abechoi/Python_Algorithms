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