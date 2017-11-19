import numpy as np

def create_laplacian_1d(n_x):
    laplacian = np.zeros(shape = (n_x, n_x), dtype=np.float64)
    for i in range(1, n_x-1): # create laplacian matrix (2nd to 2nd-to-last row)
        laplacian[i, i] = -2.0
        laplacian[i, i+1] = 1.0
        laplacian[i, i-1] = 1.0

    laplacian[0,n_x-1] = 1.0 # treat first row separately
    laplacian[0,0] = -2.0
    laplacian[0,1] = 1.0

    laplacian[n_x-1,0] = 1.0 # treat last row separately
    laplacian[n_x-1,n_x-1] = -2.0
    laplacian[n_x-1,n_x-2] = 1.0

    return laplacian

# def create_laplacian_2d(n_x, n_y):
#     laplacian = np.zeros(shape = (n_x*n_y, n_x*n_y), dtype=np.float64)
#     for i in range(1, n_x*n_y-1): # create laplacian matrix (2nd to 2nd-to-last row)
#         laplacian[i, i] = -4.0
#         laplacian[i, i+1] = 1.0
#         laplacian[i, i-1] = 1.0

#     laplacian[0,n_x*n_y-1] = 1.0 # treat first row separately
#     laplacian[0,0] = -4.0
#     laplacian[0,1] = 1.0

#     laplacian[n_x*n_y-1,0] = 1.0 # treat last row separately
#     laplacian[n_x*n_y-1,n_x*n_y-1] = -4.0
#     laplacian[n_x*n_y-1,n_x*n_y-2] = 1.0

#     return laplacian