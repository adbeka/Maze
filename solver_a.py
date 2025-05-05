# Maze Solver with A* Search Algorithm
# Written by [Your Name]
# Assistance from ChatGPT for structure and explanations.

import heapq
import math

def read_maze(filename):
    """Reads the maze from a text file and returns a 2D list."""
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

def find_start_and_goal(maze):
    """Finds the start 'S' and goal 'G' positions."""
    start = None
    goal = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'G':
                goal = (i, j)
    return start, goal

def heuristic(a, b):
    """Heuristic function: Euclidean distance for 8-direction movement."""
    return math.hypot(a[0] - b[0], a[1] - b[1])

def solve_maze_astar(maze):
    """Finds best path using A* search (fewest moves, lowest coins)."""
    rows, cols = len(maze), len(maze[0])
    start, goal = find_start_and_goal(maze)

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    heap = []
    heapq.heappush(heap, (0 + heuristic(start, goal), 0, 0, start[0], start[1], [(start[0], start[1])]))

    visited = dict()

    while heap:
        priority, moves, coins, r, c, path = heapq.heappop(heap)

        if (r, c) == goal:
            return coins, path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                cell = maze[nr][nc]
                if cell != 'X':  # not a wall
                    new_coins = coins
                    if cell.isdigit():
                        new_coins += int(cell)

                    if (nr, nc) not in visited or \
                        (moves + 1 < visited[(nr, nc)][0]) or \
                        (moves + 1 == visited[(nr, nc)][0] and new_coins < visited[(nr, nc)][1]):

                        visited[(nr, nc)] = (moves + 1, new_coins)
                        estimated_cost = moves + 1 + heuristic((nr, nc), goal)
                        heapq.heappush(heap, (estimated_cost, moves + 1, new_coins, nr, nc, path + [(nr, nc)]))

    return None, []

def main():
    # Replace 'maze1.txt', 'maze2.txt', 'maze3.txt' with your maze files
    mazes = ['maze1.txt', 'maze2.txt', 'maze3.txt']
    results = []

    for maze_file in mazes:
        maze = read_maze(maze_file)
        coins, path = solve_maze_astar(maze)
        if coins is not None:
            results.append(str(coins))
        else:
            results.append("NoPath")

    # Print result as requested: single row, separated by commas
    print(",".join(results))

if __name__ == "__main__":
    main()
