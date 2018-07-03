
import numpy as np

class labelMaker:
	n=1
	def __init__(self,n):
		self.n=n

	"""def makeLabels(self,data): #here we recive a column matrix with the all data close prices
		labels = np.arange(data.size-1, dtype=float) #mirar si se puede hacer esto sin crearla antes
		for i in range(0, data.size-1):
			benefit = data[i+1] - data[i]
			labels[i] = benefit

		return labels""" #este seria para utilizar como labels la diferencia de precio de un dia para otro


	def makeLabels(self,data):
		labels = np.arange(data.size-60, dtype=float)
		for i in range(60, data.size):
			labels[i-60] = data[i]

		return labels # de esta forma las labels son el precio maximo que se alcanza el dia siguiente
