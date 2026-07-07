from  utils.image_io import load_image, save_image
from algorithms.spatial import mean_blur_filter, median_filter, laplacian_filter, gaussian_blur_filter
from algorithms.edge_detection import sobel_edge_detection , prewitt_edge_detection
img  = load_image("examples/test.jpg")

img_mean = mean_blur_filter(img , 5)
img_median = median_filter(img , 5)
img_gauss = gaussian_blur_filter(img , 5 , 1 )
img_laplace = laplacian_filter(img)
img_sobel_ed = sobel_edge_detection(img)
img_prewitt_ed = prewitt_edge_detection(img)

#save_image("examples/test_mean.jpg" , img_mean)
#save_image("examples/test_median.jpg" , img_median)
#save_image("examples/test_gauss.jpg" , img_gauss)
#save_image("examples/test_laplace.jpg" , img_laplace)
save_image("examples/test_sed.jpg" , img_sobel_ed)
save_image("examples/test_ped.jpg" , img_prewitt_ed)