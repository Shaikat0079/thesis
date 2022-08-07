import cv2
from skimage import metrics


ref_img = cv2.imread("desktop.jpg")
img1 = cv2.imread("noisedesktop.jpg")
img2 = cv2.imread("desktop_average.jpg")
img3 = cv2.imread("desktop_bilateral.jpg")
img4 = cv2.imread("desktop_gaussian.jpg")
img5 = cv2.imread("desktop_median.jpg")


# Mean square error

mse_skimg1 = metrics.mean_squared_error(ref_img, img1)
print("MSE: based on scikit-image = ", mse_skimg1)
mse_skimg2 = metrics.mean_squared_error(ref_img, img2)
print("MSE: based on scikit-image Average_Filtering = ", mse_skimg2)
mse_skimg3 = metrics.mean_squared_error(ref_img, img3)
print("MSE: based on scikit-image Bilateral_Filtering = ", mse_skimg3)
mse_skimg4 = metrics.mean_squared_error(ref_img, img4)
print("MSE: based on scikit-image Gaussian_Filtering = ", mse_skimg4)
mse_skimg5 = metrics.mean_squared_error(ref_img, img5)
print("MSE: based on scikit-image Median_Filtering = ", mse_skimg5)
# mse_skimg6 = metrics.mean_squared_error(ref_img, ref_img)
# print("MSE: based on scikit-image No_Filtering = ", mse_skimg6)


print('=======================================================')
print('=======================================================')
print('=======================================================')
print('=======================================================')

# Peak Signal Noise Ratio

psnr_skimg1 = metrics.peak_signal_noise_ratio(ref_img, img1)
print("PSNR: based on scikit-image = ", psnr_skimg1)
psnr_skimg2 = metrics.peak_signal_noise_ratio(ref_img, img2)
print("PSNR: based on scikit-image Average_Filtering= ", psnr_skimg2)
psnr_skimg3 = metrics.peak_signal_noise_ratio(ref_img, img3)
print("PSNR: based on scikit-image Bilateral_Filtering= ", psnr_skimg3)
psnr_skimg4 = metrics.peak_signal_noise_ratio(ref_img, img4)
print("PSNR: based on scikit-image Gaussian_Filtering= ", psnr_skimg4)
psnr_skimg5 = metrics.peak_signal_noise_ratio(ref_img, img5)
print("PSNR: based on scikit-image Median_Filtering= ", psnr_skimg5)


print('=======================================================')
print('=======================================================')
print('=======================================================')
print('=======================================================')

# Normalized Root Mean Square Error

nrmse_skimg1 = metrics.normalized_root_mse(ref_img, img1)
print("NRMSE: based on scikit-image = ", nrmse_skimg1)
nrmse_skimg2 = metrics.normalized_root_mse(ref_img, img2)
print("NRMSE: based on scikit-image Average_Filtering= ", nrmse_skimg2)
nrmse_skimg3 = metrics.normalized_root_mse(ref_img, img3)
print("NRMSE: based on scikit-image Bilateral_Filtering= ", nrmse_skimg3)
nrmse_skimg4 = metrics.normalized_root_mse(ref_img, img4)
print("NRMSE: based on scikit-image Gaussian_Filtering= ", nrmse_skimg4)
nrmse_skimg5 = metrics.normalized_root_mse(ref_img, img5)
print("NRMSE: based on scikit-image Median_Filtering= ", nrmse_skimg5)


# Here I've Added the output for First iteration

""" MSE: based on scikit-image =  2392.208961043001
MSE: based on scikit-image Average_Filtering =  93.94648762870547
MSE: based on scikit-image Bilateral_Filtering =  442.56392640794525
MSE: based on scikit-image Gaussian_Filtering =  144.15111267709776
MSE: based on scikit-image Median_Filtering =  171.32418395864593
=======================================================
=======================================================
=======================================================
=======================================================
PSNR: based on scikit-image =  14.342812479828794
PSNR: based on scikit-image Average_Filtering=  28.401998130677292
PSNR: based on scikit-image Bilateral_Filtering=  21.67104349379809
PSNR: based on scikit-image Gaussian_Filtering=  26.54262361887987
PSNR: based on scikit-image Median_Filtering=  25.79261688979681
=======================================================
=======================================================
=======================================================
=======================================================
NRMSE: based on scikit-image =  0.37964459739899575
NRMSE: based on scikit-image Average_Filtering=  0.07523465632016421
NRMSE: based on scikit-image Bilateral_Filtering=  0.1632922876152887
NRMSE: based on scikit-image Gaussian_Filtering=  0.0931937241309786
NRMSE: based on scikit-image Median_Filtering=  0.10159843154493951 """
