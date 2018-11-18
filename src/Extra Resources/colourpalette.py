# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 11:34:31 2018

@author: Jin
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import itemfreq
from sklearn.cluster import KMeans
from collections import Counter
import webcolors

img = cv2.imread('download.jpg')

arr = np.float32(img)
pixels = arr.reshape((-1, 3))

palette = np.uint8(centroids)
quantized = palette[labels.flatten()]
quantized = quantized.reshape(img.shape)

dominant_color = palette[np.argmax(itemfreq(labels)[:, -1])]


l = []
final_colour = ''

def get_dominant_color(image, k=4, image_processing_size = None):
    #resize image if new dims provided
    if image_processing_size is not None:
        image = cv2.resize(image, image_processing_size, 
                            interpolation = cv2.INTER_AREA)
    
    #reshape the image to be a list of pixels
    image = image.reshape((image.shape[0] * image.shape[1], 3))

    #cluster and assign labels to the pixels 
    clt = KMeans(n_clusters = k)
    labels = clt.fit_predict(image)

    #count labels to find most popular
    label_counts = Counter(labels)
    
    #subset out most popular centroid
    first_colour = clt.cluster_centers_[label_counts.most_common(3)[0][0]]
    second_colour = clt.cluster_centers_[label_counts.most_common(3)[1][0]]
    third_colour = clt.cluster_centers_[label_counts.most_common(3)[2][0]]
    
    dominant_colour = [[first_colour[2],first_colour[1],first_colour[0]],[second_colour[2],second_colour[1],second_colour[0]],\
                       [third_colour[2],third_colour[1],third_colour[0]]]
    
    print([first_colour[2],first_colour[1],first_colour[0]],[second_colour[2],second_colour[1],second_colour[0]],\
                       [third_colour[2],third_colour[1],third_colour[0]])
    #return list(dominant_colour)
    
    for i in dominant_colour:
        actual_name, closest_name = get_colour_name(i)
        if actual_name:
            final_color = actual_name
        else:
            final_color = closest_name
        l.append(final_color)
    
    print(l)


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

get_dominant_color(img)
    