from  utils.image_io import load_image, save_image
from algorithms.spatial import mean_blur_filter, median_filter, laplacian_filter, gaussian_blur_filter
from algorithms.edge_detection import sobel_edge_detection , prewitt_edge_detection
from algorithms.segmentation import global_thresholding
from algorithms.color_utils import apply_to_color


#img  = load_image("examples/test.jpg" )
color_img = load_image("examples/test.jpg" , False)
img = load_image("examples/test.jpg")

img_mean = apply_to_color(mean_blur_filter, color_img, 5)
img_median = apply_to_color(median_filter, color_img, 5)
img_gauss = apply_to_color(gaussian_blur_filter, color_img, 5 , 1)
img_laplace = apply_to_color(laplacian_filter, color_img)
#img_sobel_ed = apply_to_color(sobel_edge_detection, color_img)
#img_prewitt_ed= apply_to_color(prewitt_edge_detection, color_img)
#img_threshold = apply_to_color(global_thresholding, color_img, 100)
#img_mean = mean_blur_filter(img , 5)
#img_median = median_filter(img , 5)
#img_gauss = gaussian_blur_filter(img , 5 , 1 )
#img_laplace = laplacian_filter(img)
img_sobel_ed = sobel_edge_detection(img)
img_prewitt_ed = prewitt_edge_detection(img)
img_threshold = global_thresholding(img , 100)

save_image("examples/test_mean.jpg" , img_mean)
save_image("examples/test_median.jpg" , img_median)
save_image("examples/test_gauss.jpg" , img_gauss)
save_image("examples/test_laplace.jpg" , img_laplace)
save_image("examples/test_sed.jpg" , img_sobel_ed)
save_image("examples/test_ped.jpg" , img_prewitt_ed)
save_image("examples/test_threshold.jpg" , img_threshold)