#!/usr/bin/python
from PIL import Image

offsetx = 4
offsety = 278 
nsquares = 15
lengthboard = 712
###  705 / 15 = 47
outersq = lengthboard / nsquares
innersq = 45
margin = (outersq - innersq  )
print(outersq)
print(innersq)
print(margin)
im = Image.open("wordfeud.jpg")

for y in range(0, nsquares):
    for x in range(0,nsquares):
        topleft = offsetx + x * outersq + margin, offsety + y * outersq + margin
        bottomright = topleft[0] + innersq, topleft[1] + innersq
        box = topleft + bottomright

        n, N = x + 1, y + 1
        pathout = "squares/x{:02d}y{:02d}.jpeg".format(n, N)
        imcpy = im.crop(box)
        imcpy.save(pathout)


md_out = []
for y in range(0, nsquares):
    for x in range(0,nsquares):
       
        n, N, S = x + 1, y + 1, x + y * nsquares + 1

        uri = "https://raw.githubusercontent.com/hnsz/feuddle/master/squares/x{:02d}y{:02d}.jpeg".format(n, N)
        mdtag_f = "![square {:d}]({:s})"
        mdimg = mdtag_f.format(S, uri)
        
        md_out.append(mdimg)

    md_out.append("")




fout = open("README.md", "w")
print("\n".join(md_out), file=fout )

    
