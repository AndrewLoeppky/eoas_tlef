import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 10., 0.04)
ytan = np.tan(theta)
ytanM = np.ma.masked_where(np.abs(ytan)>20., ytan)

plt.figure()
plt.plot(theta, ytanM)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)

plt.savefig('plotLimits3.pdf')

plt.show()