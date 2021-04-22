import cv2
import numpy as np


def area_fill(image, coordinates_list):
    height, width, channel = image.shape
    fill_img = np.zeros(shape=(height, width, channel), dtype=np.uint8)  # 全黑的背景图

    # 进行轮廓填充
    for coordinates in coordinates_list:
        fill_img = cv2.fillConvexPoly(fill_img, coordinates, (255, 255, 255))
    return fill_img


def get_coordinates_list(file_path):
    coordinates_list = []

    f = open(file_path)
    lines = f.readlines()
    for line in lines:
        str_list = line.split()
        h1 = int(float(str_list[0]))
        w1 = int(float(str_list[1]))
        h2 = int(float(str_list[2]))
        w2 = int(float(str_list[3]))
        h3 = int(float(str_list[4]))
        w3 = int(float(str_list[5]))
        h4 = int(float(str_list[6]))
        w4 = int(float(str_list[7]))
        coordinates = np.array([[h1, w1], [h2, w2], [h3, w3], [h4, w4]])
        coordinates_list.append(coordinates)
    return coordinates_list


img = cv2.imread('demo.jpg')
coordinates_list = get_coordinates_list(file_path='demo.txt')


threshold_img = area_fill(img, coordinates_list)
cv2.imwrite('res.jpg', threshold_img)
