import numpy as np 
import statistics

def mean_blur_filter(img, kernel_size):
    pad_size = kernel_size // 2
    pd_img = np.pad(img, pad_size, 'reflect')
    
    windows = np.lib.stride_tricks.sliding_window_view(pd_img, (kernel_size, kernel_size))
    
    output = windows.mean(axis=(-2, -1))
    
    return output.astype(np.uint8)


def median_filter(img, kernel_size):
    pad_size = kernel_size // 2
    pd_img = np.pad(img, pad_size, 'reflect')
    
    windows = np.lib.stride_tricks.sliding_window_view(pd_img, (kernel_size, kernel_size))
    
    output = np.median(windows, axis=(-2, -1))
    
    return output.astype(np.uint8)

def gaussian_blur_filter(img, kernel_size, sigma=1):
    pad_size = kernel_size // 2
    
    kernel = np.zeros((kernel_size, kernel_size))
    for x in range(-pad_size, pad_size + 1):
        for y in range(-pad_size, pad_size + 1):
            value = np.exp(-(x**2 + y**2) / (2 * sigma**2))
            kernel[x + pad_size][y + pad_size] = value
    
    kernel = kernel / np.sum(kernel)
    
    pd_img = np.pad(img, pad_size, 'reflect')
    output = np.zeros(img.shape)
    H, W = img.shape
    
    for i in range(H):
        for j in range(W):
            I = i + pad_size
            J = j + pad_size
            total = 0
            for k in range(-pad_size, pad_size + 1):
                for l in range(-pad_size, pad_size + 1):
                    pixel_value = int(pd_img[I + k][J + l])
                    weight = kernel[k + pad_size][l + pad_size]
                    total = total + pixel_value * weight
            output[i][j] = total
    
    return output.astype(np.uint8)

def laplacian_filter(img):
    pad_size = 1
    pd_img = np.pad(img , pad_size , "reflect")
    output = np.zeros(img.shape)
    kernel = np.array([[0 , -1 , 0] , [-1 , 4 , -1] , [0 , -1, 0]])
    H , W = img.shape

    for i in range(H) : 
        for j in range(W) :
            I = i + pad_size
            J = j + pad_size
            laplacian_value = 0
            for k in range(-pad_size, pad_size + 1):
                for l in range(-pad_size, pad_size + 1):
                    pixel_value = int(pd_img[I + k][J + l])
                    weight = kernel[k + pad_size][l + pad_size]
                    laplacian_value = laplacian_value + pixel_value * weight
            
            original_pixel = int(pd_img[I][J])
            sharpened_value = original_pixel + laplacian_value
            output[i][j] = np.clip(sharpened_value, 0, 255)

    return output.astype(np.uint8)
    


