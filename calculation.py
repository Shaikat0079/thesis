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


# Here I've Added the output of the First iteration

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

print("=======================================================")
print("=======================================================")
print("=======================================================")
print("=======================================================")
print("2nd Iteration")
print("=======================================================")
print("=======================================================")
print("=======================================================")
print("=======================================================")
img6 = cv2.imread("noisedesktop2.jpg")
img7 = cv2.imread("desktop_average2.jpg")
img8 = cv2.imread("desktop_bilateral2.jpg")
img9 = cv2.imread("desktop_gaussian2.jpg")
img10 = cv2.imread("desktop_median2.jpg")


# Mean square error

mse_skimg6 = metrics.mean_squared_error(ref_img, img6)
print("MSE: based on scikit-image = ", mse_skimg6)
mse_skimg7 = metrics.mean_squared_error(ref_img, img7)
print("MSE: based on scikit-image Average_Filtering = ", mse_skimg7)
mse_skimg8 = metrics.mean_squared_error(ref_img, img8)
print("MSE: based on scikit-image Bilateral_Filtering = ", mse_skimg8)
mse_skimg9 = metrics.mean_squared_error(ref_img, img9)
print("MSE: based on scikit-image Gaussian_Filtering = ", mse_skimg9)
mse_skimg10 = metrics.mean_squared_error(ref_img, img10)
print("MSE: based on scikit-image Median_Filtering = ", mse_skimg10)
# mse_skimg6 = metrics.mean_squared_error(ref_img, ref_img)
# print("MSE: based on scikit-image No_Filtering = ", mse_skimg6)


print('=======================================================')
print('=======================================================')
print('=======================================================')
print('=======================================================')

# Peak Signal Noise Ratio

psnr_skimg6 = metrics.peak_signal_noise_ratio(ref_img, img6)
print("PSNR: based on scikit-image = ", psnr_skimg6)
psnr_skimg7 = metrics.peak_signal_noise_ratio(ref_img, img7)
print("PSNR: based on scikit-image Average_Filtering= ", psnr_skimg7)
psnr_skimg8 = metrics.peak_signal_noise_ratio(ref_img, img8)
print("PSNR: based on scikit-image Bilateral_Filtering= ", psnr_skimg8)
psnr_skimg9 = metrics.peak_signal_noise_ratio(ref_img, img9)
print("PSNR: based on scikit-image Gaussian_Filtering= ", psnr_skimg9)
psnr_skimg10 = metrics.peak_signal_noise_ratio(ref_img, img10)
print("PSNR: based on scikit-image Median_Filtering= ", psnr_skimg10)


print('=======================================================')
print('=======================================================')
print('=======================================================')
print('=======================================================')

# Normalized Root Mean Square Error

nrmse_skimg6 = metrics.normalized_root_mse(ref_img, img6)
print("NRMSE: based on scikit-image = ", nrmse_skimg6)
nrmse_skimg7 = metrics.normalized_root_mse(ref_img, img7)
print("NRMSE: based on scikit-image Average_Filtering= ", nrmse_skimg7)
nrmse_skimg8 = metrics.normalized_root_mse(ref_img, img8)
print("NRMSE: based on scikit-image Bilateral_Filtering= ", nrmse_skimg8)
nrmse_skimg9 = metrics.normalized_root_mse(ref_img, img9)
print("NRMSE: based on scikit-image Gaussian_Filtering= ", nrmse_skimg9)
nrmse_skimg10 = metrics.normalized_root_mse(ref_img, img10)
print("NRMSE: based on scikit-image Median_Filtering= ", nrmse_skimg10)

# Here I've Added the output of the Second iteration

"""
 MSE: based on scikit-image =  198.4908977777417
MSE: based on scikit-image Average_Filtering =  14.537066317881463
MSE: based on scikit-image Bilateral_Filtering =  25.508968504732227
MSE: based on scikit-image Gaussian_Filtering =  15.486681599145891
MSE: based on scikit-image Median_Filtering =  12.309358558643044
=======================================================
=======================================================
=======================================================
=======================================================
PSNR: based on scikit-image =  25.153397648092604
PSNR: based on scikit-image Average_Filtering=  36.50603589180272
PSNR: based on scikit-image Bilateral_Filtering=  34.06387463283601
PSNR: based on scikit-image Gaussian_Filtering=  36.23121991370222
PSNR: based on scikit-image Median_Filtering=  37.228449384564904
=======================================================
=======================================================
=======================================================
=======================================================
NRMSE: based on scikit-image =  0.1093573469492722
NRMSE: based on scikit-image Average_Filtering=  0.029594843883289448
NRMSE: based on scikit-image Bilateral_Filtering=  0.039203434529377024
NRMSE: based on scikit-image Gaussian_Filtering=  0.030546176177642135
NRMSE: based on scikit-image Median_Filtering=  0.027232993268903518

 """
