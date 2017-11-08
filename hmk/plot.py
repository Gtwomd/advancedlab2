import numpy as np
import matplotlib.pyplot as plt

def f(Y, r1=2.5e-2, X=7.22e-2):
	return cosofarctan(r1/Y)*np.power(sinofarctan(r1/Y),2)*bottomsinterm(Y,r1,X)
def cosofarctan(X):
	return np.power(1 + X**2, -0.5)
def sinofarctan(X):
	return X*np.power(1 + X**2, -0.5)
def bottomsinterm(Y,r1,X):
	a = r1*(X+Y)*np.power(X*Y-r1**2,-1)
	return np.power(0.5*(1 - cosofarctan(a)),-2)
Y = np.linspace(1e-2, 20e-2, 100)
fig,ax = plt.subplots()
ax.plot(Y,f(Y))
ax.set_xlabel('$Y$ (cm)')
ax.set_ylabel('$f(Y)$', rotation=0)
plt.show()