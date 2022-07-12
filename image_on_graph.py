#taken from github

import sys, matplotlib
from matplotlib import pyplot, cbook
imgf = cbook.get_sample_data('grace_hopper.jpg')
img = pyplot.imread(imgf)
pyplot.imshow(img)


pyplot.show()
