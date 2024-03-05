import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import numpy.linalg as la
import processingFigure as proc

filename = data['params']['name']
A, ymat = proc.permuteImage(filename)
