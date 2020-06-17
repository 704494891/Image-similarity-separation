import cv2
import os
from skimage.metrics import structural_similarity as ssim
import shutil
from skimage.metrics import peak_signal_noise_ratio as psnr

dir_target_img = "/home/gsh/PythonProjects/PycharmProjects/cloud_dibang/delet_same_img/the_2020-06-16_img/target"  # 被用来对比的模版图文件夹
dir_test_img = '/home/gsh/PythonProjects/PycharmProjects/cloud_dibang/delet_same_img/the_2020-06-16_img/all_img'  # 被用来检测分类的图片数据集文件夹
dir_trash_img = "/home/gsh/PythonProjects/PycharmProjects/cloud_dibang/delet_same_img/the_2020-06-16_img/trash"  # 长宽比不符合的垃圾图被存入的文件夹
dir_other_img = "/home/gsh/PythonProjects/PycharmProjects/cloud_dibang/delet_same_img/the_2020-06-16_img/others"  # 长宽一致的其他图像被保存的文件夹
dir_useful_img = "/home/gsh/PythonProjects/PycharmProjects/cloud_dibang/delet_same_img/the_2020-06-16_img/useful"  # 留下来有用的图存储的文件夹

def delate_laji(dir_test_img, dir_trash_img):
    test_img_name_list = os.listdir(dir_test_img)
    for j in range(len(test_img_name_list)):
        test_img = cv2.imread(os.path.join(dir_test_img, test_img_name_list[j]), 0)
        if (720, 1280) != test_img.shape:
            shutil.move(os.path.join(dir_test_img, test_img_name_list[j]),
                        os.path.join(dir_trash_img, test_img_name_list[j]))

def similarity_classification(dir_target_img, dir_test_img, dir_useful_img, dir_other_img, weight=15):
    target_img_name_list = os.listdir(dir_target_img)
    test_img_name_list = os.listdir(dir_test_img)

    for j in range(len(test_img_name_list)):
        print("第%d张图"% j)
        test_img = cv2.imread(os.path.join(os.path.join(dir_test_img, test_img_name_list[j])), 0)
        test_img = test_img[290:719, 0:1280]

        flag = 0
        for i in range(len(target_img_name_list)):
            target_img = cv2.imread(os.path.join(dir_target_img , target_img_name_list[i]), 0)
            target_img = target_img[290:719, 0:1280]
            cor_psnr = psnr(target_img, test_img)
            if cor_psnr > weight:
                flag = 1
                shutil.copyfile(
                    os.path.join(dir_test_img, test_img_name_list[j]),os.path.join(dir_useful_img, test_img_name_list[j]) )
                print("想死")
        if flag == 0:
            shutil.copyfile(os.path.join(dir_test_img, test_img_name_list[j]),os.path.join(dir_other_img, test_img_name_list[j]))


if __name__ == '__main__':
    # delate_laji(dir_test_img, dir_trash_img)
    similarity_classification(dir_target_img, dir_test_img, dir_useful_img, dir_other_img, weight=15)
