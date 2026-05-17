import matplotlib.pyplot as plt
import numpy as np

def show_grid(grid, start, goal, path=None):
    grid_array = np.array(grid)

    plt.figure(figsize=(6, 6))
    plt.imshow(grid_array, cmap="gray_r")

    # Show start point
    plt.scatter(start[1], start[0], marker="o", s=150, label="Start")

    # Show goal point
    plt.scatter(goal[1], goal[0], marker="*", s=200, label="Goal")

    # Show path
    if path:
        path_rows = [p[0] for p in path]
        path_cols = [p[1] for p in path]
        plt.plot(path_cols, path_rows, linewidth=3, label="Path")

    plt.xticks(range(len(grid[0])))
    plt.yticks(range(len(grid)))
    plt.grid(True)
    plt.legend()
    plt.title("2D Indoor Navigation Simulator")
    plt.show()
