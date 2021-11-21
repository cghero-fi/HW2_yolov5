import os
import scipy.io
import pandas as pd
import numpy as np
from PIL import Image
import json

labels = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
}

img_dir = "./train/train/"
ana_txt_save_path = "labels/"
if not os.path.exists(ana_txt_save_path):
    os.makedirs(ana_txt_save_path)
import mat73


def convert(size, box):
    dw = 1.0 / (size[0])
    dh = 1.0 / (size[1])
    x = box[0] + box[2] / 2.0
    y = box[1] + box[3] / 2.0
    w = box[2]
    h = box[3]

    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


mat = mat73.loadmat("./train/train/digitStruct.mat")
print(len(mat["digitStruct"]["bbox"]))
print(len(mat["digitStruct"]["name"]))
print(type(mat["digitStruct"]["bbox"][0]))
print(type(mat["digitStruct"]["bbox"][0]["height"]))
for i in range(len(mat["digitStruct"]["name"])):
    now_name = str(mat["digitStruct"]["name"][i])
    image = Image.open(img_dir + now_name)
    width, height = image.size
    label_name = now_name.split(".")[0] + ".txt"
    print(str(label_name))
    f_txt = open(os.path.join(ana_txt_save_path, label_name), "w")
    bbox_dict = mat["digitStruct"]["bbox"][i]
    if isinstance(bbox_dict["height"], list):
        bbox_num = len(mat["digitStruct"]["bbox"][i]["height"])
        for j in range(bbox_num):
            h = int(bbox_dict["height"][j].tolist())
            w = int(bbox_dict["width"][j].tolist())
            l = int(bbox_dict["label"][j].tolist())
            lf = int(bbox_dict["left"][j].tolist())
            t = int(bbox_dict["top"][j].tolist())
            box = convert((width, height), (float(lf), float(t), float(w), float(h)))
            if l == 10:
                l = 0
            labels[str(l)] += 1
            f_txt.write("%s %s %s %s %s\n" % (str(l), box[0], box[1], box[2], box[3]))
    else:
        h = int(bbox_dict["height"].tolist())
        w = int(bbox_dict["width"].tolist())
        l = int(bbox_dict["label"].tolist())
        lf = int(bbox_dict["left"].tolist())
        t = int(bbox_dict["top"].tolist())
        box = convert((width, height), (float(lf), float(t), float(w), float(h)))
        labels[str(l)] += 1
        f_txt.write("%s %s %s %s %s\n" % (str(l), box[0], box[1], box[2], box[3]))
    f_txt.close()
print(labels)
