import os
import time
import numpy as np
#import torch
import matplotlib.image as plt


if __name__ == '__main__':

    print (f"python app start at \n {time.gmtime()}")

    # 외부 폴더 경로 설정
    external_folder_path = "/external_folder"

    print ('Connected "container folder" = "system Volume"')

    # "output" 폴더 생성
    output_folder_path = f"{external_folder_path}/Projects/hellocamca/output"
    os.makedirs(output_folder_path, exist_ok=True)

    print (f'Folder create for output at {output_folder_path}')


    # "input" 폴더
    input_folder_path = f"{external_folder_path}/Datasets/1_example"
    input_npy=np.load(f"{input_folder_path}/random.npy")

    print (f'input_npy file read from {input_folder_path}/random.npy')
    print (input_npy)
    plt.imsave( output_folder_path+ '/example.png', input_npy, cmap='gray')
