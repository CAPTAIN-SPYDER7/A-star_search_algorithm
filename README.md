# A* Path Planning Project

This project demonstrates the implementation of the A* path planning algorithm for navigating a grid-based environment. The A* algorithm is used to find the shortest path from a start point to an end point while avoiding obstacles.

## Overview

The A* algorithm is a widely used search algorithm in pathfinding and graph traversal. It combines the benefits of Dijkstra's algorithm and a greedy best-first search. The algorithm uses a heuristic to estimate the cost to reach the goal, which helps in efficiently finding the shortest path.

### Key Concepts

- **Grid-based Environment**: The environment is represented as a grid where each cell can be either passable or an obstacle.
- **Movement Model**: The robot can move in four directions—up, down, left, and right.
- **Heuristic Function**: The Euclidean distance is used as the heuristic to estimate the cost from any cell to the goal.


### Pseudocode Explanation

Let \( g(n) \) be the cost from the start node to the node \( n \), and \( h(n) \) be the heuristic estimate from node \( n \) to the goal. The total cost function \( f(n) \) is defined as:

\[ f(n) = g(n) + h(n) \]

Where:
- \( g(n) \) represents the actual cost from the start node to the current node \( n \).
- \( h(n) \) is the heuristic estimate of the cost from \( n \) to the goal.

The A* algorithm proceeds by expanding nodes with the lowest \( f(n) \) value until the goal node is reached.

### Equations

- **Euclidean Distance (Heuristic)**:
  \[ h(n) = sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2} \]

  Where \( (x_1, y_1) \) and \( (x_2, y_2) \) are the coordinates of the current node and the goal node, respectively.

- **Path Cost**:
  \[ g(n) = g_{{current}} + {cost to move to neighbor} \]

  The `cost_to_move_to_neighbor` is typically 1 for grid-based movements in this implementation (assuming a cost of 1 for each step in the grid).

## Usage

To run the A* Path Planning project, follow these steps:

1. **Setup**:
   - Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone https://github.com/praneelraghuraman/A-star_search_algorithm.git
     ```

3. **Navigate to the Project Directory**:
   - Open your terminal or command prompt and navigate to the project directory:
     ```bash
     cd A-star_search_algorithm
     ```

4. **Install Required Libraries**:
   - Install any required Python libraries (if any are needed beyond standard libraries). Typically, this might include `tkinter` for the GUI:
     ```bash
     pip install -r requirements.txt
     ```
   - Ensure you have `tkinter` installed for the graphical user interface. It usually comes pre-installed with Python, but you can install it manually if needed.

5. **Run the GUI**:
   - Start the graphical user interface by running the following command:
     ```bash
     python3 gui.py
     ```
   - This will open the GUI window where you can set up the grid, place the start and goal points, and add obstacles.

6. **Execute the A* Algorithm**:
   - After setting up the environment in the GUI, click the "Run" button to execute the A* pathfinding algorithm.
   - The path found by the algorithm will be displayed on the grid.

7. **Modify Grid and Rerun**:
   - You can adjust the grid settings, change the start or end points, add or remove obstacles, and rerun the algorithm to see how it navigates different scenarios.

## Test Cases

Here are some example test cases showcasing the functionality of the A* path planning algorithm. The images below depict various scenarios, including simple paths and paths with obstacles.

### Test Case 1: Simple Path

In this test case, the algorithm finds the shortest path from the start point to the goal in an obstacle-free environment.

![Test Case 1]

### Test Case 2: Path with Obstacles

This test case illustrates the algorithm's ability to navigate around obstacles to reach the goal.

![Test Case 2]

### Test Case 3: Complex Obstacles

In this scenario, the algorithm finds a path through a more complex obstacle arrangement.

![Test Case 3]

### Test Case 4: Narrow Passages

This test shows the algorithm's capability to navigate through narrow passages to find the goal.

![Test Case 4]


## Conclusion

This project demonstrates the efficiency and effectiveness of the A* pathfinding algorithm in navigating grid-based environments. Key highlights include:

- **Optimal Pathfinding**: A* efficiently finds the shortest path from the start to the goal, even in the presence of obstacles.
- **Heuristic-Driven**: The use of a heuristic function (Euclidean distance) allows the algorithm to prioritize nodes closer to the goal, reducing the number of explored nodes.
- **Versatile Applications**: The A* algorithm is applicable in various domains, including robotics, games, and geographical navigation.

The implementation provided is flexible and can be adapted to different grid sizes, start and goal configurations, and obstacle patterns. Users can experiment with different setups to see how the algorithm performs under various conditions.

Feel free to explore the code, modify the parameters, and extend the functionality to suit your specific needs. Your contributions and feedback are always welcome!


