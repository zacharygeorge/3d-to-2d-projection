import numpy as np
import matplotlib.pyplot as plt

cube_points = np.array([
    [1,1,1],
    [1,1,-1],
    [1,-1,1],
    [1,-1,-1],
    [-1,1,1],
    [-1,1,-1],
    [-1,-1,1],
    [-1,-1,-1]
    ])

# Define cube edges by point indices
edges = [
    (0, 1), (0, 2), (0, 4),
    (1, 3), (1, 5),
    (2, 3), (2, 6),
    (3, 7),
    (4, 5), (4, 6),
    (5, 7),
    (6, 7)
]

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot points
ax.scatter(cube_points[:, 0], cube_points[:, 1], cube_points[:, 2], color='red')

# Draw edges
for start, end in edges:
    xs = [cube_points[start][0], cube_points[end][0]]
    ys = [cube_points[start][1], cube_points[end][1]]
    zs = [cube_points[start][2], cube_points[end][2]]
    ax.plot(xs, ys, zs, color='blue')

# Labels and aspect
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

plt.show()