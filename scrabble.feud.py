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

for N in range(0, nsquares):
    for n in range(0,nsquares):
        topleft = offsetx + n * outersq + margin, offsety + N * outersq + margin
        bottomright = topleft[0] + innersq, topleft[1] + innersq
        box = topleft + bottomright

        pathout = "square{:02d}x{:02d}.jpeg".format(n +1, N +1)
        imcpy = im.crop(box)
        imcpy.save(pathout)



