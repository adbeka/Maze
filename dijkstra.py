# Maze Solver with Dijkstra's Algorithm
# Written by [Your Name]
# Assistance from ChatGPT for structure and explanations.

import heapq

def read_maze(filename):
    """Reads the maze from a text file and returns a 2D list."""
    maze = []
    with open(filename, 'r') as f:
        for line in f:
            maze.append(list(line.strip()))
    return maze

def find_start(maze):
    """Finds the start position 'S'."""
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                return (i, j)
    return None

def solve_maze_dijkstra(maze):
    """Finds the best path using Dijkstra's (fewest moves, then least coins)."""
    rows, cols = len(maze), len(maze[0])
    start = find_start(maze)

    # 8 possible moves
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Priority queue: (moves, coins_sum, row, col, path)
    heap = []
    heapq.heappush(heap, (0, 0, start[0], start[1], [(start[0], start[1])]))

    visited = dict()

    while heap:
        moves, coins, r, c, path = heapq.heappop(heap)

        if maze[r][c] == 'G':
            return coins, path

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                cell = maze[nr][nc]

                if cell != 'X':  # Not a wall
                    new_coins = coins
                    if cell.isdigit():
                        new_coins += int(cell)

                    # Only move if better or unvisited
                    if (nr, nc) not in visited or \
                        (moves + 1 < visited[(nr, nc)][0]) or \
                        (moves + 1 == visited[(nr, nc)][0] and new_coins < visited[(nr, nc)][1]):

                        visited[(nr, nc)] = (moves + 1, new_coins)
                        heapq.heappush(heap, (moves + 1, new_coins, nr, nc, path + [(nr, nc)]))

    # If no path
    return None, []

def main():
    # Replace 'maze1.txt', 'maze2.txt', 'maze3.txt' with your maze files
    mazes = ['/workspaces/Maze/maze_11x11.txt', '/workspaces/Maze/maze_31x31.txt', '/workspaces/Maze/maze_101x101.txt']
    results = []

    for maze_file in mazes:
        maze = read_maze(maze_file)
        coins, path = solve_maze_dijkstra(maze)
        if coins is not None:
            results.append(str(coins))
        else:
            results.append("NoPath")

    # Print result as requested: single row, separated by commas
    print(",".join(results))

if __name__ == "__main__":
    main()
