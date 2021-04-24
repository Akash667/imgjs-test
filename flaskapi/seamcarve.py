import cv2
import numpy as np
import os
import errno
from os import path
from glob import glob
import matplotlib as mpl
import matplotlib.pyplot as plt
import time


def cal_img_energy(image):
    image = image.astype('float32')
    energy = np.absolute(cv2.Sobel(image, -1, 1, 0)) + \
        np.absolute(cv2.Sobel(image, -1, 0, 1))
    energy_map = np.sum(energy, axis=2)
    return energy_map


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


def find_min_seam(energy_map_forward, backtrack):
    shape = m, n = energy_map_forward.shape
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


# example to reduce a defined number of pixels in an image
# the range for the for loop will be the number of these pixels.
# For each pixel to be removed:
# 1-Calculate energy of image
# 2-Calculate seam cost forward
# 3-Find minimum seam
# 4-Draw seam
# 5-Remove seam and traverse pixels left
t0 = time.time()
path = os.path.join(os.getcwd(), 'fig5')  # replace fig5 with the actual path
img = np.copy(fig5)
for c in range(350):  # 350 denotes the amount of pixels to be reduced from the image
    energy_map = calc_img_energy(img)
    energy_map_forward, backtrack = calc_seam_cost_forward(energy_map)
    (min_seam, cost) = find_min_seam(energy_map_forward, backtrack)
    bgr_img_with_seam = draw_seam(img, min_seam)
    # can remove this to not store every seam image
    cv2.imwrite('%s%s.png' % (path, c), bgr_img_with_seam)
    img = remove_seam(img, min_seam)
# output image stored seprately
cv2.imwrite('%sfig5_resized.png' % (path), img)
t1 = time.time()
total = t1-t0
# ISSUE!!! takes upto 4-5 minutes to remove 100 pixels
print("Total Time: %d" % total)


# Shows the resized image
blue, green, red = cv2.split(img)
rgb_img = np.dstack([red, green, blue])
plt.imshow(rgb_img)
plt.axis("off")
plt.title("Figure Resized")

# example to add pixels

# read the image


fig8 = cv2.imread('fig8.png', cv2.IMREAD_COLOR)
rgb_fig8 = cv2.cvtColor(fig8, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_fig8)
plt.axis("off")
plt.title("Original Figure 8 Image")
print("Figure Shape: %s" % (fig8.shape,))


num_pixels_to_increase = 120  # Increase image by this this number of pixels
a = np.arange(0, fig8.shape[1], 1)
b = np.expand_dims(a, axis=0)
pixels_kept = np.repeat(b, fig8.shape[0], axis=0)
pixels_removed = np.zeros((fig8.shape[0], num_pixels_to_increase), dtype=int)
img = np.copy(fig8)


t0 = time.time()
for c in range(num_pixels_to_increase):
    # Find seam to remove
    energy_map = calc_img_energy(img)
    energy_map_forward, backtrack = calc_seam_cost_forward(energy_map)
    (min_seam, cost) = find_min_seam(energy_map_forward, backtrack)
    # Remove minimum seam from ndarray that tracks image reductions and add to list of pixels removed
    rows, cols, _ = img.shape
    mask = np.ones((rows, cols), dtype=np.bool)
    for i in range(0, rows):
        j = min_seam[i]
        mask[i, j] = False
    # Remove seam from image
    pixels_removed[:, c] = pixels_kept[mask == False].reshape((rows,))
    pixels_kept = pixels_kept[mask].reshape((rows, cols - 1))
    img = remove_seam(img, min_seam)

pixels_removed.sort(axis=1)
img = np.copy(fig8)
for c in range(num_pixels_to_increase):
    img = insert_seam(img, pixels_removed[:, c])
    pixels_removed[:, c + 1:] = pixels_removed[:, c + 1:] + 1

t1 = time.time()
total = t1-t0
print("Total Time: %d" % total)


# output the image
path = os.path.join(os.getcwd(), 'images/fig8out/')
blue, green, red = cv2.split(img)
rgb_img = np.dstack([red, green, blue])
plt.imshow(rgb_img)
plt.axis("off")
plt.title("Figure 8 Resized")
print("Figure 8 Resized Shape: %s" % (rgb_img.shape,))

cv2.imwrite('%s%s.png' % (path, 'resize_1'), img)
