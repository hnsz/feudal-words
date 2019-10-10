#!/usr/bin/python
from functools import reduce

import numpy
from PIL import Image
import os

def incBuckets(l, s):
    newlist = []
    start = 0

    for subrange in range(s, len(l), s):
        chunk = l[start:subrange]
        newlist.append(sum(chunk))

        start = subrange
    return newlist


histogram = []
basename_f = "x{:02d}y{:02d}{:s}"
uri_f = "https://raw.githubusercontent.com/hnsz/feuddle/outputimages/squares/{:s}"
mdtag_f = "![square {:d}]({:s})"

dest_dir_img    = "squares" 
dest_dir_hist   = "hist"
sqrt_nsquares = 15
nsquares = sqrt_nsquares * sqrt_nsquares
boardposition = 0, 274


offsetsx = [  0, 49,  96, 144, 192, 239, 287, 335, 382, 430, 478, 525, 573, 621, 668, 716]
marginsx = [  4,  3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3   ]

offsetsy = [274, 323, 370, 418, 466, 513, 561, 609, 656, 704, 752, 799, 847, 895, 942, 990]
marginsy = [  4,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3,   3  ]


readme_md = []
square_data = []
for y in range(0, sqrt_nsquares):
    for x in range(0, sqrt_nsquares):
        left    = offsetsx[x] + marginsx[x]
        upper   = offsetsy[y] + marginsy[y]
        right   = offsetsx[x + 1]
        lower   = offsetsy[y + 1]

        n, N = x + 1, y + 1

        square_data.append({
            "box": (left, upper, right, lower),
            "basename_img": basename_f.format(n, N, ".jpeg"),
            "basename_hist": basename_f.format(n, N, ".txt")
            })


        m = x + y * sqrt_nsquares + 1
        uri = uri_f.format(basename_f.format(n, N, ".jpeg"))
        mdtag_img = mdtag_f.format(m, uri)
        readme_md.append(mdtag_img)

    readme_md.append("")



im = Image.open("wordfeud.jpg")

for m in range(0, nsquares):
        box         = square_data[m]["box"]
        histpath    = dest_dir_hist + "/" + square_data[m]["basename_hist"]
        imgpath     = dest_dir_img + "/" + square_data[m]["basename_img"]

        imcpy = im.crop(box)
        imcpy.save(imgpath)

        histogram = imcpy.histogram()
        histo_r = incBuckets(list(histogram[0:256]), 8)
        histo_g = incBuckets(list(histogram[256:512]),8)
        histo_b = incBuckets(list(histogram[512:768]), 8)

        hist_fout = open(histpath, "w")
        print(histo_r, file=hist_fout)
        print(histo_g, file=hist_fout)
        print(histo_b, file=hist_fout)
        hist_fout.close()










fout = open("README.md", "w")

print("\n".join(readme_md), file=fout )




#//each value/ bin sum the values


#hist_img.



