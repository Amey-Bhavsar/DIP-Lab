import numpy as np 
import statistics

def mean_blur_filter(img, kernel_size):
    pad_size = kernel_size // 2
    pd_img = np.pad(img , pad_size, 'reflect')
    output = np.zeros(img.shape)
    H, W = img.shape
    for i in range(H):
        for j in range(W):
            I = i + pad_size
            J = j + pad_size
            sum = 0
            for k in range(I - kernel_size//2 , I + kernel_size//2 + 1):
                for l in range(J - kernel_size//2, J + kernel_size//2 + 1):
                    sum = sum + pd_img[k][l]
            
            mean = sum / (kernel_size *kernel_size)
            output[i][j] = mean
           
    return output.astype(np.uint8)

def median_filter(img, kernel_size):
    pad_size = kernel_size // 2
    pd_img = np.pad(img , pad_size, 'reflect')
    output = np.zeros(img.shape)
    H, W = img.shape
    for i in range(H):
        for j in range(W):
            I = i + pad_size
            J = j + pad_size
            window =[]
            for k in range(I - kernel_size//2 , I + kernel_size//2 + 1):
                for l in range(J - kernel_size//2, J + kernel_size//2 + 1):
                    window.append(pd_img[k][l])
            output[i][j] = statistics.median(window)
           
    return output.astype(np.uint8)


