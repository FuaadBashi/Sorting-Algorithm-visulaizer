# Sorting-Algorithm-visulaizer
An interactive Python app using Pygame to visualize 5 different Sorting algorithms in real time. Features customizable list resets, sorting directions, and dynamic block animations. Perfect for learning and teaching sorting algorithms! ( **Bubble Sort** , **Insertion Sort**, **Merge Sort**, **Selection Sort** and **Quick Sort**)

---

# Sorting Algorithm Visualizer

A Python-based visualizer for sorting algorithms using the Pygame library. This interactive application allows users to visualize the step-by-step sorting process for **Bubble Sort**, **Insertion Sort**, **Merge Sort**, **Selection Sort** and **Quick Sort**, with options for ascending or descending order.  

---

## Features

- **Visualize Sorting Algorithms**: Watch how sorting algorithms rearrange elements dynamically.
- **Interactive Controls**: 
  - `R`: Reset the list to random values.
  - `SPACE`: Start sorting.
  - `A`: Sort in ascending order.
  - `D`: Sort in descending order.
  algorithms = {
        - 'B': bubble_sort,
        - 'I': insertion_sort,
        - 'S': selection_sort,
        - 'M': merge_sort,
        - 'Q': quick_sort,
    }
- **Real-Time Feedback**: Highlight comparisons and swaps during sorting.

---

## How It Works

1. **Sorting Algorithms**: Implements the following sorting algorithms:
   - **Bubble Sort**: Repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
   - **Insertion Sort**: Builds the final sorted array one item at a time by repeatedly picking the next element and inserting it into its correct position.
   - **Quick Sort**: A divide-and-conquer algorithm that selects a pivot element and partitions the array into two subarrays, sorting them recursively.
   - **Selection Sort**: Divides the list into a sorted and an unsorted region and repeatedly selects the smallest element from the unsorted region to add to the sorted region.
   - **Merge Sort**: A divide-and-conquer algorithm that divides the array into halves, recursively sorts them, and then merges the sorted halves.
2. **Randomized Input**: Generates a new random list for sorting on reset.
3. **Customizable Visualization**: The blocks’ size and color change dynamically to represent the sorting process.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/sorting-visualizer.git
   cd sorting-visualizer
   ```

2. Install the required library:
   ```bash
   pip install pygame
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Controls

| Key         | Action                                 |
|-------------|---------------------------------------|
| **R**       | Reset list to new random values.      |
| **SPACE**   | Start sorting with the selected algorithm. |
| **A**       | Sort in ascending order.              |
| **D**       | Sort in descending order.             |
| **B**       | Switch to Bubble Sort.                |
| **I**       | Switch to Insertion Sort.             |
| **S**       | Switch to Selection Sort.             |
| **M**       | Switch to Merge Sort.                 |
| **Q**       | Switch to Quick Sort.                 |


---

## Project Structure

```
sorting-visualizer/
│
├── main.py                # Main application file
├── README.md              # Project documentation
└── requirements.txt       # Dependencies (if needed)
```

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code adheres to Python coding standards.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

