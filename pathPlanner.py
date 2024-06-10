# Import any libraries required
# The main path planning function. Additional functions, classes,
# variables, libraries, etc. can be added to the file, but this
# function must always be defined with these arguments and must
# return an array ('list') of coordinates (col,row).
# DO NOT EDIT THIS FUNCTION DECLARATION
def do_a_star(grid, start, end, display_message):
    # Helper function to calculate Euclidean distance between two points

    def euclidean_distance(point1, point2):
        return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

    # Helper function to get valid neighbors of a given cell
    def get_neighbors(cell):
        neighbors = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Right, Left, Down, Up
        for dir in directions:
            neighbor = (cell[0] + dir[0], cell[1] + dir[1])
            if 0 <= neighbor[0] < COL and 0 <= neighbor[1] < ROW and grid[neighbor[0]][neighbor[1]] == 1:
                neighbors.append(neighbor)
        return neighbors

    # Calculate the heuristic (Euclidean distance) from a cell to the end point
    def heuristic(cell):
        return euclidean_distance(cell, end)

    # Get the size of the grid
    COL = len(grid)
    ROW = len(grid[0])

    # Initialize lists for open set, closed set, and path
    open_set = [start]
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start)}

    # A* algorithm implementation
    while open_set:
        current = min(open_set, key=lambda x: f_score[x])
        if current == end:
            # Reconstruct path if end point is reached
            path = []
            while current in came_from:
                path.insert(0, current)
                current = came_from[current]
            path.insert(0, start)  # Add start point to path
            display_message("Path found!")
            return path

        open_set.remove(current)
        neighbors = get_neighbors(current)
        for neighbor in neighbors:
            tentative_g_score = g_score[current] + 1  # Assuming cost of moving to neighbor is 1
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                if neighbor not in open_set:
                    open_set.append(neighbor)

    # If no path found, return an empty path
    display_message("No valid path found!")
    return []

# end of file
