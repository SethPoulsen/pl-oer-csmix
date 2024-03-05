
import numpy as np
import numpy.linalg as la

x_ = la.solve(A,ymat.flatten())
xmat = x_.reshape(ymat.shape)

# possible wrong answer
xwrong = x_.reshape(ymat.shape,order='F')

ywrong = ymat.flatten(order='F')
z = la.solve(A, ywrong)
xwrong2 = z.reshape(ymat.shape)

xwrong3 = z.reshape(ymat.shape,order='F')


