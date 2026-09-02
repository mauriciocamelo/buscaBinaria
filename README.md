# Binary Search Implementation

This repository contains a Python implementation of the **Binary Search** algorithm, developed as a college assignment.

## 📖 Description

The script searches for a specific number chosen by the user within a pre-defined sorted list of integers. It uses the binary search method, which is highly efficient for finding items in sorted arrays by repeatedly dividing in half the portion of the list that could contain the target item.

**Note on the dataset:** The current list contains numbers from 0 to 30 (excluding 8).

## 🚀 How to Run

1. Make sure you have [Python](https://www.python.org/) installed on your machine.
2. Run the script in your terminal:
```bash
python binary_search.py

```


3. When prompted, type a number between 0 and 30.
4. The program will output the exact index where the number was found, or inform you if the item is not present in the list. During the search, it also prints the intermediate indices checked by the algorithm.

## ⚙️ Complexity

Binary search provides a significant performance advantage over linear search, especially for large datasets.

* **Time Complexity (Best Case):** $O(1)$ — occurs when the target is exactly at the middle of the list on the first try.
* **Time Complexity (Worst/Average Case):** $O(\log n)$ — where $n$ is the number of elements in the list.
* **Space Complexity:** $O(1)$ — because the algorithm only uses a few pointers (`esquerda`, `direita`, `meio`) regardless of the list size.
