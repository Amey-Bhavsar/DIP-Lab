import numpy as np 

def apply_to_color(func, img , *args):
    R_channel = img[:,:,0]
    G_channel = img[: , : , 1]
    B_channel = img[:,: ,2]

    r_out = func(R_channel, *args)
    g_out = func(G_channel, *args)
    b_out = func(B_channel, *args)
    
    output = np.dstack((r_out, g_out, b_out))
    return output.astype(np.uint8)