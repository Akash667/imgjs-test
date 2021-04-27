import cv2
import numba
import numpy as np
import os
import errno
from os import path
from glob import glob
import base64
from PIL import Image
from numba import jit
import uuid



def calc_img_energy(image):
    image = image.astype('float32')
    energy = np.absolute(cv2.Sobel(image, -1, 1, 0)) + \
        np.absolute(cv2.Sobel(image, -1, 0, 1))
    energy_map = np.sum(energy, axis=2)
    return energy_map


def calc_seam_cost_forward(energy_map):
    m, n = energy_map.shape
    shape = m, n
    e_map = np.copy(energy_map).astype('float32')
    backtrack = np.zeros(shape, dtype=int)
    for i in range(1, m):
        for j in range(0, n):
            if j == 0:
                min_idx = np.argmin(e_map[i - 1, j:j + 2])
                min_cost = e_map[i - 1, j + min_idx]
                e_map[i, j] += min_cost
                backtrack[i, j] = j + min_idx
            else:
                min_idx = np.argmin(e_map[i - 1, j - 1:j + 2])
                min_cost = e_map[i - 1, j + min_idx - 1]
                e_map[i, j] += min_cost
                backtrack[i, j] = j + min_idx - 1
    return (e_map, backtrack)


def find_min_seam(energy_map_forward, backtrack):
    m, n = energy_map_forward.shape
    shape = m, n
    seam = np.zeros(m, dtype=int)
    idx = np.argmin(energy_map_forward[-1])
    cost = energy_map_forward[-1][idx]
    seam[-1] = idx
    for i in range(m - 2, -1, -1):
        idx = backtrack[i + 1, idx]
        seam[i] = idx
    return seam, cost


def draw_seam(image, seam):
    rows = np.arange(0, seam.shape[0], 1)
    blue, green, red = cv2.split(image)
    blue[rows, seam] = 0
    green[rows, seam] = 0
    red[rows, seam] = 255
    img_with_seam = np.zeros((blue.shape[0], blue.shape[1], 3))
    img_with_seam[:, :, 0] = blue
    img_with_seam[:, :, 1] = green
    img_with_seam[:, :, 2] = red
    return img_with_seam


def remove_seam(image, seam):
    m, n, _ = image.shape
    out_image = np.zeros((m, n - 1, 3)).astype(dtype=int)
    for i in range(m):
        j = seam[i]
        out_image[i, :, 0] = np.delete(image[i, :, 0], j)
        out_image[i, :, 1] = np.delete(image[i, :, 1], j)
        out_image[i, :, 2] = np.delete(image[i, :, 2], j)
    return out_image


def insert_seam(image, seam):
    m, n, num_channels = image.shape
    out_image = np.zeros((m, n + 1, 3)).astype(dtype=int)
    for i in range(m):
        j = seam[i]
        for ch in range(num_channels):
            if j == 0:
                out_image[i, j, ch] = image[i, j, ch]
                out_image[i, j + 1:, ch] = image[i, j:, ch]
                out_image[i, j + 1, ch] = (int(image[i, j, ch]) +
                                           int(image[i, j + 1, ch])) / int(2)
            elif j + 1 == n:
                out_image[i, :j + 1, ch] = image[i, :j + 1, ch]
                out_image[i, j + 1, ch] = int(image[i, j, ch])
            else:
                out_image[i, :j, ch] = image[i, :j, ch]
                out_image[i, j + 1:, ch] = image[i, j:, ch]
                out_image[i, j, ch] = (
                    int(image[i, j - 1, ch]) + int(image[i, j + 1, ch])) / int(2)
    return out_image


def remove_vertical_seam(image):
    img = np.copy(image)
    energy_map = calc_img_energy(img)
    energy_map_forward, backtrack = calc_seam_cost_forward(energy_map)
    (min_seam, cost) = find_min_seam(energy_map_forward, backtrack)
    img = remove_seam(img, min_seam)
    return img, cost


def remove_horizontal_seam(image):
    img = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    energy_map = calc_img_energy(img)
    energy_map_forward, backtrack = calc_seam_cost_forward(energy_map)
    (min_seam, cost) = find_min_seam(energy_map_forward, backtrack)
    img = remove_seam(img, min_seam)
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return img, cost


def calc_seam_cost_forward(energy_map):
    shape = m, n = energy_map.shape
    e_map = np.copy(energy_map).astype('float32')
    backtrack = np.zeros(shape, dtype=int)
    for i in range(1, m):
        for j in range(0, n):
            if j == 0:
                min_idx = np.argmin(e_map[i - 1, j:j + 2])
                min_cost = e_map[i - 1, j + min_idx]
                e_map[i, j] += min_cost
                backtrack[i, j] = j + min_idx
            else:
                min_idx = np.argmin(e_map[i - 1, j - 1:j + 2])
                min_cost = e_map[i - 1, j + min_idx - 1]
                e_map[i, j] += min_cost
                backtrack[i, j] = j + min_idx - 1
    return (e_map, backtrack)

# takes input


def input_funct(figure, num_seams):

    rgb_figure = cv2.cvtColor(figure, cv2.COLOR_BGR2RGB)
    path = os.path.join(os.getcwd(), '')
    img = np.copy(figure)
    # print(type(img))
    
    for c in range(num_seams):
        energy_map = calc_img_energy(img)
        energy_map_forward, backtrack = calc_seam_cost_forward(energy_map)
        (min_seam, cost) = find_min_seam(energy_map_forward, backtrack)
        # bgr_img_with_seam = draw_seam(img, min_seam)
        img = remove_seam(img, min_seam)


    imageId = str(uuid.uuid4())
    # print(path)
    cv2.imwrite("{}{}".format(path,imageId+".jpg"), img)  # returns 3-D ndaraay

    # print(type(img))

    my_string = ""

    with open("./{}".format(imageId+".jpg"), "rb") as img_file:
        # print("file read")
        my_string = base64.b64encode(img_file.read())

    return my_string
    
    # convert to complete image using:
    # blue, green, red = cv2.split(img)

    # rgb_img = np.dstack([red, green, blue])

    # my_string = base64.b64encode(img)

    
    # imageData = Image.fromarray(img, 'RGB')


    # from io import BytesIO
    # buffered = BytesIO()
    # imageData.save(buffered, format="JPEG")
    # img_str = base64.b64encode(buffered.getvalue())
    # return base64.b64encode(rgb_img)  # returns image with rgb combined
    # # rgb_img is the final image
    # return my_string


def data_uri_to_cv2_img(uri):
    print(uri[:20])
    encoded_data = ""
    if uri[:5] != "data":
        encoded_data = uri
    else:
        encoded_data = uri.split(',')[1]

    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

# for test
if __name__=="__main__":
    figure = cv2.imread('1.jpg', cv2.IMREAD_COLOR)
    # print(figure)
    # num_seams = int(input("Enter the number of seams: "))
    result_image = input_funct(figure, 10) #gives a stacked 3-d ndarray as the result - is rgb_image
    # print(result_image)


def reduce_seams(dataURI, noOfSeams):

    result = input_funct(data_uri_to_cv2_img(dataURI), noOfSeams)

    return result

# if __name__=="__main__":
