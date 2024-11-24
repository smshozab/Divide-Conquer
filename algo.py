import streamlit as st
import random
import numpy as np
import matplotlib.pyplot as plt

# Function to generate random points
def generate_random_points(n):
    return [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n)]

# Utility function to calculate Euclidean distance
def distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# # Divide and Conquer approach for Closest Pair of Points
# def closest_pair_dc(points):
#     # Sort points by x-coordinate
#     points_sorted_by_x = sorted(points, key=lambda point: point[0])
#     points_sorted_by_y = sorted(points, key=lambda point: point[1])
    
#     return closest_pair_recursive(points_sorted_by_x, points_sorted_by_y)

# def closest_pair_recursive(points_sorted_by_x, points_sorted_by_y):
#     # Base case: if there are 3 or fewer points, use brute-force (already handled)
#     if len(points_sorted_by_x) <= 3:
#         min_dist = float('inf')
#         closest_points = None
#         for i in range(len(points_sorted_by_x)):
#             for j in range(i + 1, len(points_sorted_by_x)):
#                 dist = distance(points_sorted_by_x[i], points_sorted_by_x[j])
#                 if dist < min_dist:
#                     min_dist = dist
#                     closest_points = (points_sorted_by_x[i], points_sorted_by_x[j])
#         return closest_points, min_dist

#     # Divide the points into two halves
#     mid = len(points_sorted_by_x) // 2
#     left_half = points_sorted_by_x[:mid]
#     right_half = points_sorted_by_x[mid:]

#     # Recursively find the closest pairs in the left and right halves
#     left_closest, left_dist = closest_pair_recursive(left_half, [point for point in points_sorted_by_y if point in left_half])
#     right_closest, right_dist = closest_pair_recursive(right_half, [point for point in points_sorted_by_y if point in right_half])

#     # Find the minimum distance from the two halves
#     min_dist = min(left_dist, right_dist)
#     closest_points = left_closest if left_dist < right_dist else right_closest

#     # Create a strip of points that are within `min_dist` of the center line
#     mid_x = points_sorted_by_x[mid][0]
#     strip = [point for point in points_sorted_by_y if abs(point[0] - mid_x) < min_dist]

#     # Check if there are closer points in the strip
#     for i in range(len(strip)):
#         for j in range(i + 1, len(strip)):
#             if (strip[j][1] - strip[i][1]) >= min_dist:
#                 break  # No need to check further
#             dist = distance(strip[i], strip[j])
#             if dist < min_dist:
#                 min_dist = dist
#                 closest_points = (strip[i], strip[j])

#     return closest_points, min_dist

# Function to visualize the divide and conquer steps
def visualize_closest_pair(points, closest_pair, strip, step_title):
    x, y = zip(*points)
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color="blue", label="Points")
    
    # Highlight the closest pair
    if closest_pair:
        plt.scatter(
            [closest_pair[0][0], closest_pair[1][0]],
            [closest_pair[0][1], closest_pair[1][1]],
            color="red",
            label="Closest Pair"
        )
    
    # Highlight the strip points
    if strip:
        strip_x, strip_y = zip(*strip)
        plt.scatter(strip_x, strip_y, color="orange", label="Strip Points")
    
    plt.legend()
    plt.title(step_title)
    plt.xlabel("X-coordinate")
    plt.ylabel("Y-coordinate")
    st.pyplot(plt)

# Modified recursive function with visualization
def closest_pair_recursive_with_visualization(points_sorted_by_x, points_sorted_by_y, step):
    # Base case: if there are 3 or fewer points, use brute-force
    if len(points_sorted_by_x) <= 3:
        min_dist = float('inf')
        closest_points = None
        for i in range(len(points_sorted_by_x)):
            for j in range(i + 1, len(points_sorted_by_x)):
                dist = distance(points_sorted_by_x[i], points_sorted_by_x[j])
                if dist < min_dist:
                    min_dist = dist
                    closest_points = (points_sorted_by_x[i], points_sorted_by_x[j])
        visualize_closest_pair(points_sorted_by_x, closest_points, [], f"Step {step}: Base Case")
        return closest_points, min_dist

    # Divide the points into two halves
    mid = len(points_sorted_by_x) // 2
    left_half = points_sorted_by_x[:mid]
    right_half = points_sorted_by_x[mid:]
    mid_x = points_sorted_by_x[mid][0]

    # Recursively find the closest pairs in the left and right halves
    step += 1
    left_closest, left_dist = closest_pair_recursive_with_visualization(
        left_half, [point for point in points_sorted_by_y if point in left_half], step
    )
    step += 1
    right_closest, right_dist = closest_pair_recursive_with_visualization(
        right_half, [point for point in points_sorted_by_y if point in right_half], step
    )

    # Find the minimum distance from the two halves
    min_dist = min(left_dist, right_dist)
    closest_points = left_closest if left_dist < right_dist else right_closest

    # Create a strip of points that are within `min_dist` of the center line
    strip = [point for point in points_sorted_by_y if abs(point[0] - mid_x) < min_dist]

    # Check if there are closer points in the strip
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1]) >= min_dist:
                break  # No need to check further
            dist = distance(strip[i], strip[j])
            if dist < min_dist:
                min_dist = dist
                closest_points = (strip[i], strip[j])

    # Visualize the current step
    visualize_closest_pair(points_sorted_by_x, closest_points, strip, f"Step {step}: Merging Step")
    return closest_points, min_dist

# Updated closest_pair_dc to include visualization
def closest_pair_dc_with_visualization(points):
    points_sorted_by_x = sorted(points, key=lambda point: point[0])
    points_sorted_by_y = sorted(points, key=lambda point: point[1])
    return closest_pair_recursive_with_visualization(points_sorted_by_x, points_sorted_by_y, 0)

def karatsuba(x, y, steps):
    # Base case for recursion
    if x < 10 or y < 10:
        steps.append(f"{x} * {y} = {x * y}")
        return x * y
    
    # Determine the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2
    
    # Split the numbers
    high_x, low_x = divmod(x, 10**m)
    high_y, low_y = divmod(y, 10**m)
    
    # Log the split
    steps.append(f"Split {x} into {high_x} and {low_x}")
    steps.append(f"Split {y} into {high_y} and {low_y}")
    
    # Recursive calls for three products
    z0 = karatsuba(low_x, low_y, steps)
    z2 = karatsuba(high_x, high_y, steps)
    z1 = karatsuba(low_x + high_x, low_y + high_y, steps) - z0 - z2
    
    # Log intermediate results
    steps.append(f"z0 = {low_x} * {low_y} = {z0}")
    steps.append(f"z1 = ({low_x} + {high_x}) * ({low_y} + {high_y}) - z0 - z2 = {z1}")
    steps.append(f"z2 = {high_x} * {high_y} = {z2}")
    
    # Combine the results
    result = z2 * 10**(2 * m) + z1 * 10**m + z0
    steps.append(f"Combine results: {z2}*10^{2*m} + {z1}*10^{m} + {z0} = {result}")
    
    return result

# Driver code
steps = []
result = karatsuba(7792928598171287, 1638140281417127, steps)

print("Step-by-step working:")
for step in steps:
    print(step)
print(f"Final Result: {result}")

# Initialize session state for points and numbers
if "points" not in st.session_state:
    st.session_state.points = []
if "numbers" not in st.session_state:
    st.session_state.numbers = None



# App title
st.title("Divide & Conquer Algorithm - Closest Pair & Karatsuba Multiplication")

# Tabs for algorithms
tab1, tab2 = st.tabs(["Closest Pair of Points", "Karatsuba Multiplication"])

# ---- Closest Pair of Points ----
with tab1:
    st.header("Closest Pair of Points")
    st.markdown(""" 
        The Closest Pair of Points problem involves finding the pair of points with the minimum Euclidean distance among a set of points on a 2D plane. 
        Using the **Divide and Conquer approach**, the points are recursively split into halves, and the closest pair is found in each half. 
        The results are then merged while considering the points near the dividing line.  
        This approach reduces the time complexity to \( O(n \log n) \), making it significantly faster than the brute-force method for large datasets.
    """)

    # Input options
    option = st.radio(
        "Choose how to provide input:",
        ("Generate Random Points", "Upload Input File"),
        key="closest_pair_option"
    )

    # # Random input generation
    # if option == "Generate Random Points":
    #     num_points = st.number_input("Number of points to generate:", min_value=2, value=10, step=1)
    #     if st.button("Generate Points"):
    #         st.session_state.points = generate_random_points(num_points)
    #         st.write("Generated Points:", st.session_state.points)
    # Random input generation
    if option == "Generate Random Points":
        num_points = st.number_input("Number of points to generate:", min_value=100, value=100, step=1)
        if st.button("Generate Points"):
            points = generate_random_points(num_points)
            st.session_state.points = points  # Store points in session state
            st.write("Generated Points:", points)

            # Prepare the random points as a string for download
            points_string = ";".join([f"{x},{y}" for x, y in points])
            
            # Create a download button for random points
            st.download_button(
                label="Download Random Points as Text File",
                data=points_string,
                file_name="random_points.txt",
                mime="text/plain"
            )

    # File upload
    elif option == "Upload Input File":
        uploaded_file = st.file_uploader("Upload a file with points (format: x1,y1;x2,y2;...):", type=["txt"], key="file_upload_points")
        if uploaded_file:
            content = uploaded_file.read().decode("utf-8").strip()
            try:
                st.session_state.points = [tuple(map(int, p.split(','))) for p in content.split(';')]
                st.write("Uploaded Points:", st.session_state.points)
            except Exception as e:
                st.error(f"Invalid file format! Error: {e}")

    # Run the algorithm
    # if st.button("Run Closest Pair Algorithm"):
    #     if len(st.session_state.points) > 0:
    #         closest_points, min_dist = closest_pair_dc(st.session_state.points)
    #         st.write(f"Closest Pair: {closest_points}")
    #         st.write(f"Minimum Distance: {min_dist:.2f}")

    #         # Plot the points and highlight the closest pair
    #         x, y = zip(*st.session_state.points)
    #         plt.scatter(x, y, color="blue", label="Points")
    #         plt.scatter(
    #             [closest_points[0][0], closest_points[1][0]],
    #             [closest_points[0][1], closest_points[1][1]],
    #             color="red",
    #             label="Closest Pair"
    #         )
    #         plt.legend()
    #         plt.title("Closest Pair of Points (Divide and Conquer)")
    #         plt.xlabel("X-coordinate")
    #         plt.ylabel("Y-coordinate")
    #         st.pyplot(plt)
    #     else:
    #         st.warning("No points available to run the algorithm! Please generate or upload points.")
    if st.button("Run Closest Pair Algorithm with Visualization"):
        if len(st.session_state.points) > 0:
            closest_points, min_dist = closest_pair_dc_with_visualization(st.session_state.points)
            st.write(f"Closest Pair: {closest_points}")
            st.write(f"Minimum Distance: {min_dist:.2f}")
        else:
            st.warning("No points available to run the algorithm! Please generate or upload points.")

# ---- Karatsuba Multiplication ----
with tab2:
    st.header("Karatsuba Multiplication")
    st.markdown("""  
        The Karatsuba algorithm is an efficient method for multiplying two large numbers. Unlike the traditional approach with a time complexity of \( O(n^2) \), 
        Karatsuba reduces the number of multiplications required using a recursive strategy. It breaks numbers into smaller parts, computes three partial products, 
        and combines them to find the result. This clever optimization brings the time complexity down to \( O(n^{\log_2 3}) \), making it ideal for large integers.
    """)
    # Input options
    option = st.radio(
        "Choose how to provide input:",
        ("Generate Random Inputs", "Upload Input File"),
        key="karatsuba_option"
    )

    # Random input
    if option == "Generate Random Inputs":
        # Generate random large numbers for Karatsuba
        num1 = random.randint(10**5, 10**6)  # Random number with 6 digits
        num2 = random.randint(10**5, 10**6)  # Random number with 6 digits
        
            # Display the generated inputs
        st.write(f"Generated Inputs:\nFirst Number: {num1}\nSecond Number: {num2}")
        
        # Prepare the random inputs as a string for download
        random_input_string = f"{num1}\n{num2}"

        # Create a download button for random inputs
        st.download_button(
            label="Download Random Inputs as Text File",
            data=random_input_string,
            file_name="random_inputs.txt",
            mime="text/plain"
        )


        if st.button("Run Karatsuba Algorithm"):
            try:
                num1 = int(num1)
                num2 = int(num2)
                steps = []  # Initialize an empty list for storing steps
                result = karatsuba(num1, num2, steps)
                st.write(f"Product of {num1} and {num2} using Karatsuba Multiplication: {result}")
                
                # Display step-by-step computation
                st.subheader("Step-by-Step Computation")
                for step in steps:
                    st.write(step)
            except ValueError:
                st.error("Please enter valid integers.")

    # File upload
    elif option == "Upload Input File":
        uploaded_file = st.file_uploader("Upload a file with two numbers separated by a comma (e.g., 12345,67890):", type=["txt"], key="file_upload_numbers")
        if uploaded_file:
            content = uploaded_file.read().decode("utf-8").strip()
            try:
                num1, num2 = map(int, content.split(','))
                st.session_state.numbers = (num1, num2)
                steps = []  # Initialize an empty list for storing steps
                result = karatsuba(num1, num2, steps)
                st.write(f"Product of {num1} and {num2} using Karatsuba Multiplication: {result}")

                # Display step-by-step computation
                st.subheader("Step-by-Step Computation")
                for step in steps:
                    st.write(step)
            except Exception as e:
                st.error(f"Invalid file format! Error: {e}")
