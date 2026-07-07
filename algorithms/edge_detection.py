import numpy as np
import math


def sobel_edge_detection(img) :
    pad_size = 1 
    pd_img = np.pad(img , pad_size ,"reflect")
    output = np.zeros(img.shape)
    H ,W = img.shape
    Gx = np.array([[-1 , 0 , 1] , [-2 , 0 , 2] , [-1 , 0 , 1]])
    Gy = np.array([[-1 , -2 , -1] , [0 , 0 , 0] , [1 , 2 , 1]])
    for i in range(H) :
        for j in range(W) :
            I = i + pad_size
            J = j + pad_size
            gx_value = 0
            gy_value = 0
            for k in range(-pad_size, pad_size + 1):
                for l in range(-pad_size, pad_size + 1):
                    pixel_value = int(pd_img[I + k][J + l])
                    gx_value = gx_value + pixel_value * Gx[k + pad_size][l + pad_size]
                    gy_value = gy_value + pixel_value * Gy[k + pad_size][l + pad_size]
            output[i][j] = np.clip(math.sqrt(gx_value*gx_value + gy_value*gy_value) , 0 , 255) 
    return   output.astype(np.uint8)      

def prewitt_edge_detection(img) :
    pad_size = 1 
    pd_img = np.pad(img , pad_size ,"reflect")
    output = np.zeros(img.shape)
    H ,W = img.shape
    Gx = np.array([[-1 , 0 , 1] , [-1 , 0 , 1] , [-1 , 0 , 1]])
    Gy = np.array([[-1 , -1 , -1] , [0 , 0 , 0] , [1 , 1 , 1]])
    for i in range(H) :
        for j in range(W) :
            I = i + pad_size
            J = j + pad_size
            gx_value = 0
            gy_value = 0
            for k in range(-pad_size, pad_size + 1):
                for l in range(-pad_size, pad_size + 1):
                    pixel_value = int(pd_img[I + k][J + l])
                    gx_value = gx_value + pixel_value * Gx[k + pad_size][l + pad_size]
                    gy_value = gy_value + pixel_value * Gy[k + pad_size][l + pad_size]
            output[i][j] = np.clip(math.sqrt(gx_value*gx_value + gy_value*gy_value) , 0 , 255) 
    return   output.astype(np.uint8) 
