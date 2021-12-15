#! /usr/bin/env python3

import math
import sys

from PIL import Image, ImageFilter
from numpy import asarray
import numpy as np

# Ensure correct usage
if len(sys.argv) != 2:
    sys.exit("Usage: python max_pooling.py filename")

# Open image
image = Image.open(sys.argv[1]).convert("RGB")

image_array = asarray(image)

M, N = image_array.shape[:2]
K = 2
L = 2

MK = M // K
NL = N // L

reduced = image_array[:MK*K, :NL*L].reshape(MK, K, NL, L).max(axis=(1, 3))

pooled = Image.fromarray(reduced)

# Show resulting image
pooled.show()
