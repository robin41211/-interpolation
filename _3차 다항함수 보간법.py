import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

data = np.loadtxt("ThermistorMotor.csv",delimiter=',',dtype = np.float64,skiprows=1)
x_ori = data[:,0]
y_ori = data[:,2]                                               #엑셀 데이터 첫번째 행 제외하고 x,y각각 배열

print(data)
x_data=x_ori
y_data=y_ori
plt.subplot(3,1,1)
plt.scatter(x_data,y_data)
plt.plot(x_data,y_data)                                         # 선형 보간 그래프, 해당 그래프를 통해 x의 특이점 찾음

###########################################################################################

y_f=interpolate.interp1d(x_data,y_data,'cubic',fill_value="extrapolate")      #'cubic'을 'linear'로 대체하면 선형에 대한 보간 함수 출력 구할 수 있음


########################################################################################
x_1 = np.linspace(0,4095,50,endpoint=True)      
y_1 = y_f(x_1)
plt.subplot(3,1,2)
plt.scatter(x_1,y_1)
############################################
x = np.linspace(0,4095,4096,endpoint=True)      
y = y_f(x)

plt.subplot(3,1,3)
plt.scatter(x,y)
plt.show()
print(np.round_(y_f(4.12), decimals = 2))
