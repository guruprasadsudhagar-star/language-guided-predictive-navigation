from astar import astar
from visualize import show_grid

grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)

print("Path found:")
print(path)

show_grid(grid, start, goal, path)
