import matplotlib.pyplot as plt
import numpy as np
import sklearn.linear_model

from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

data1 =  np.loadtxt("1.txt")
data2 =  np.loadtxt("2.txt")



X_train = data1
y_train= data2



# X_train = np.random.rand(2000).reshape(1000,2)*60
# y_train = (X_train[:, 0]**2)+(X_train[:, 1]**2)
# X_test = np.random.rand(200).reshape(100,2)*60
# y_test = (X_test[:, 0]**2)+(X_test[:, 1]**2)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_train[:,0], X_train[:,1], y_train, marker='.', color='red')
ax.set_xlabel("f")
ax.set_ylabel("n")
ax.set_zlabel("p")

model = sklearn.linear_model.LinearRegression()
model.fit(X_train, y_train)
# y_pred = model.predict(X_test)

# print("MAE: {}".format(np.abs(y_test-y_pred).mean()))
# print("RMSE: {}".format(np.sqrt(((y_test-y_pred)**2).mean())))

coefs = model.coef_
intercept = model.intercept_
xs = np.tile(np.arange(7), (7,1))
ys = np.tile(np.arange(7), (7,1)).T
zs = xs*coefs[0]+ys*coefs[1]+intercept
print("Equation: p = {:.2f} + {:.2f}f + {:.2f}n".format(intercept, coefs[0],
                                                          coefs[1]))

ax.plot_surface(xs,ys,zs, alpha=0.5)
plt.show()
