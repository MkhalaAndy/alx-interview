0x01. Lockboxes

# Box Unlocking Algorithm

## Introduction
This algorithm is designed to determine whether all the boxes in a set of sequentially numbered locked boxes can be opened. Each box may contain keys to other boxes, and a key with the same number as a box can open that box. The algorithm checks if it's possible to unlock all boxes starting from the first one, and returns True if all boxes can be opened, else it returns False.

## Method
The algorithm is implemented in Python and provided as a method named `canUnlockAll(boxes)`. The method takes a single argument:
 `boxes`: A list of lists, where each inner list represents a box and contains the keys it holds.

The method iteratively explores boxes using a breadth-first search (BFS) approach:
1. It starts by assuming the first box (`boxes[0]`) is unlocked.
2. It maintains a set to keep track of opened boxes (`opened_boxes`) and a list to keep track of boxes to explore (`boxes_to_explore`), initially containing only the first box.
3. It iterates until there are no more boxes to explore:
    - For each box in `boxes_to_explore`:
        - Marks the current box as opened.
        - Iterates through the keys in the current box:
            - If a key corresponds to an unopened box, it adds that box to `boxes_to_explore`.
4. After the iteration, it checks if all boxes have been opened. If so, it returns True; otherwise, it returns False.

## Example Usage
```python
boxes = [[1], [2], [3], []]  # Example set of locked boxes
result = canUnlockAll(boxes)  # Check if all boxes can be opened
print(result)  # Output: True (all boxes can be opened)
```

## Assumptions
- All keys are positive integers.
- There can be keys that do not correspond to any box.
- The first box (`boxes[0]`) is always unlocked.

## Contributions
Contributions and improvements to the algorithm or its documentation are welcome. Please submit a pull request with your changes.

This README provides a clear explanation of the algorithm, its usage, assumptions, and invites contributions for further improvements.
