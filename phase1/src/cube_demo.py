import numpy as np
import matplotlib.pyplot as plt

cube_points = np.array([
    [1,1,1,1],
    [1,1,-1,1],
    [1,-1,1,1],
    [1,-1,-1,1],
    [-1,1,1,1],
    [-1,1,-1,1],
    [-1,-1,1,1],
    [-1,-1,-1,1]
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

# Eventually i want to come back here and use lin alg principles of
# homogenous coordinates to use a 4x4 matrix to rotate scale and translate
# at the same time

def scale(arr, x):
    for coordinates in arr:
        coordinates[0] *= x
        coordinates[1] *= x
        coordinates[2] *= x
        
def rotatearoundz(arr):
    rotationmatrix = np.array([
        [0,1,0],
        [-1,0,0],
        [0,0,1]
    ])
    rotated = arr @ rotationmatrix.T
    return rotated

def homo(arr):
    matrix = np.array([
        [2,0,0,5],
        [0,2,0,-5],
        [0,0,2,0],
        [0,0,0,1]
    ])
    rotated = arr @ matrix.T
    return rotated

def pinhole(arr):
    f = 1
    K = np.array([
        [f,0,0,0],
        [0,f,0,0],
        [0,0,1,0]
    ])
    
    twoD = arr @ K.T
    
    projected_2d = []
    for coordinate in twoD:
        xP,yP,w = coordinate
        if w > 0:
            x = xP/w
            y = yP/w
            projected_2d.append([x,y])
        else:
            projected_2d.append([np.nan,np.nan])
            
    return np.array(projected_2d)


def plotcubetemp():
    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot points
    ax.scatter(cube_points[1:, 0], cube_points[1:, 1], cube_points[1:, 2], color='red')
    ax.scatter(cube_points[0, 0], cube_points[0, 1], cube_points[0, 2], color='green')

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

    plt.show(block = False)
    plt.pause(3)
    plt.close()
    
def plotcube():
    # Plotting
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot points
    ax.scatter(cube_points[1:, 0], cube_points[1:, 1], cube_points[1:, 2], color='red')
    ax.scatter(cube_points[0, 0], cube_points[0, 1], cube_points[0, 2], color='green')

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
    
def plotpinhole(arr):
    plt.figure()
    plt.scatter(arr[:, 0], arr[:, 1], color='red')
    
    for start, end in edges:
        x_coords = [arr[start][0], arr[end][0]]
        y_coords = [arr[start][1], arr[end][1]]
        if not np.isnan(x_coords).any() and not np.isnan(y_coords).any():
            plt.plot(x_coords, y_coords, color='blue')
            
    plt.gca().set_aspect('equal')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("2D Pinhole Projection of 3D Cube")
    plt.grid(True)
    plt.show()
    
    
plotcubetemp()
        
# scale(cube_points, 3)

# plotcubetemp()

# scale(cube_points, 1/3)

# plotcubetemp()

# cube_points = rotatearoundz(cube_points)

# plotcubetemp()

# cube_points = rotatearoundz(cube_points)

# plotcubetemp()

# cube_points = rotatearoundz(cube_points)

# plotcubetemp()

# cube_points = rotatearoundz(cube_points)

# plotcubetemp()

# cube_points += [1,1,1]

# cube_points = homo(cube_points)

# plotcubetemp()

projected = pinhole(cube_points)

plotpinhole(projected)