import numpy as np 

def apply_to_color(func, img , *args):
    if img.ndim != 3:
        raise ValueError("apply_to_color expects a color image with shape (H, W, 3), but got a grayscale image.")
    R_channel = img[:,:,0]
    G_channel = img[: , : , 1]
    B_channel = img[:,: ,2]

    r_out = func(R_channel, *args)
    g_out = func(G_channel, *args)
    b_out = func(B_channel, *args)
    
    output = np.dstack((r_out, g_out, b_out))
    return output.astype(np.uint8)