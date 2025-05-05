# Maze Solver for 'S' to 'G' with fewest moves, lowest coins.
# Allowed to move diagonally.
# Written by [Your Name].
# Assistance from ChatGPT for structure and comments.

from collections import deque

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

def solve_maze(maze):
    """Finds the best path from 'S' to 'G' with fewest moves and least coins."""
    rows, cols = len(maze), len(maze[0])
    start = find_start(maze)

    # 8 possible moves (including diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Queue for BFS: (row, col, moves, coin_sum, path)
    queue = deque()
    queue.append((start[0], start[1], 0, 0, [(start[0], start[1])]))

    # Visited with (moves, coin_sum) to prune bad paths
    visited = dict()

    best_moves = float('inf')
    best_coins = float('inf')
    best_path = []

    while queue:
        r, c, moves, coins, path = queue.popleft()

        # If reached goal
        if maze[r][c] == 'G':
            if (moves < best_moves) or (moves == best_moves and coins < best_coins):
                best_moves = moves
                best_coins = coins
                best_path = path
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check boundaries
            if 0 <= nr < rows and 0 <= nc < cols:
                cell = maze[nr][nc]

                if cell != 'X':  # Not a wall
                    # Calculate new coin sum
                    new_coins = coins
                    if cell.isdigit():
                        new_coins += int(cell)

                    # Only move if better or unvisited
                    if (nr, nc) not in visited or \
                        (moves + 1 < visited[(nr, nc)][0]) or \
                        (moves + 1 == visited[(nr, nc)][0] and new_coins < visited[(nr, nc)][1]):

                        visited[(nr, nc)] = (moves + 1, new_coins)
                        queue.append((nr, nc, moves + 1, new_coins, path + [(nr, nc)]))

    return best_coins, best_path

def path_to_moves(path):
    """Converts a path to a sequence of coin values collected."""
    moves = []
    for r, c in path:
        moves.append((r, c))
    return moves

def main():
    # Replace 'maze1.txt', 'maze2.txt', 'maze3.txt' with your maze files
    mazes = ['/workspaces/Maze/maze_11x11.txt', '/workspaces/Maze/maze_31x31.txt', '/workspaces/Maze/maze_101x101.txt']
    results = []

    for maze_file in mazes:
        maze = read_maze(maze_file)
        coins, path = solve_maze(maze)
        results.append(str(coins))

    # Print result as requested: single row, separated by commas
    print(",".join(results))

if __name__ == "__main__":
    main()
