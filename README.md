# Divide & Conquer Algorithm - Closest Pair of Points & Karatsuba Multiplication

This project implements two well-known divide and conquer algorithms:
1. **Closest Pair of Points Problem**: Finds the pair of points with the minimum Euclidean distance from a set of 2D points using the divide and conquer approach.
2. **Karatsuba Multiplication**: A fast multiplication algorithm that divides large numbers into smaller parts to reduce time complexity, implemented using a divide and conquer strategy.

## Technologies Used:
- **Python**: Main programming language.
- **Streamlit**: For building an interactive web application.
- **Matplotlib**: For visualizing the closest pair of points and the algorithm steps.
- **NumPy**: For efficient mathematical operations.

## Features:
- **Closest Pair of Points**:
  - Generate random points on a 2D plane.
  - Upload points from a file.
  - Visualize the process of finding the closest pair using divide and conquer.
  - Display step-by-step calculations and visualizations of merging and splitting points.
  
- **Karatsuba Multiplication**:
  - Multiply large numbers efficiently.
  - Visualize each recursive step of the multiplication.
  - Step-by-step logging of the calculations.

## How to Use:

### 1. **Closest Pair of Points**:
   - **Input**: You can either generate random points or upload a file containing points in the format `x1,y1;x2,y2;...`.
   - **Output**: After running the algorithm, the closest pair of points and their distance will be displayed, along with a visualization of the points and the closest pair.

### 2. **Karatsuba Multiplication**:
   - **Input**: Enter two large integers, and the algorithm will show the step-by-step multiplication process.
   - **Output**: Displays the recursive steps, splits, intermediate calculations, and final result.

## How to Run Locally:
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/closest-pair-karatsuba.git
   cd closest-pair-karatsuba
2. Install the required dependencies: bash Copy code
   ```bash
   pip install -r requirements.txt
3. Run the Streamlit app:
  ```bash
  streamlit run app.py
