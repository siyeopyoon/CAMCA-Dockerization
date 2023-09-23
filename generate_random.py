import os
import time
import numpy as np
#import torch
import matplotlib.image as plt


if __name__ == '__main__':

    print (f"python app start at \n {time.gmtime()}")
    random_matrix=np.random.random((250,250))

    plt.imsave('example.png', random_matrix, cmap='gray')
    np.save("random.npy",random_matrix)