import numpy as np
import pylab as pl
x = [5000,6000,7000,8000,9000]
y = [65,78,88,89,93]
pl.plot(x,y)

x1 = [7000,8000,9000,10000,11000]
y2 = [65,75,85,86,90]
pl.plot(x1,y2)
pl.xlabel('voltaje [V]')
pl.ylabel('eficiencia [%]')
pl.savefig('temp01.png')
