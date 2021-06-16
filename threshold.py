#! /bin/python
import sys
from pathlib import Path
import PIL
from PIL import Image
import PIL.ImageEnhance
from PIL import ImageChops
from PIL import ImageOps
from PIL import ImageFilter as pilif
import numpy as np


inputFolder1 = sys.argv[1]
outputFolder = sys.argv[2]

# print(inputFolder1)


p1 = Path(inputFolder1).glob("*.png")
for path in p1:

    im = Image.open(path).convert("L")
    print(path)

    def contrast(im, val): return PIL.ImageEnhance.Contrast(
        im).enhance(val)

    def brightness(im, val): return PIL.ImageEnhance.Brightness(
        im).enhance(val)
 # Looks better if darken, then contrast
    pim = contrast(brightness(im, 0.1), 3).filter(pilif.FIND_EDGES).filter(
        pilif.SMOOTH_MORE).filter(pilif.ModeFilter).filter(pilif.DETAIL)
    out = ImageChops.lighter(im, pim)
    out.save(outputFolder + "/" + path.name)
