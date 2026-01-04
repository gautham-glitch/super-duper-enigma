import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(url)
df = df.drop(['MODELYEAR', 'MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE',], axis = 1)
df = df.drop(['CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB',],axis=1)

X = df.iloc[:,[0,1]].to_numpy()
y = df.iloc[:,[2]].to_numpy()

from sklearn import preprocessing
standard_scalar = preprocessing.StandardScaler()
x_scalar = standard_scalar.fit_transform(X)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_scalar, y, test_size = 0.2, random_state = 42)

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit(x_train,y_train)
print(f"coeff = {reg.coef_}\nintercept = {reg.intercept_}")

means_ = standard_scalar.mean_
std_devs_ = np.sqrt(standard_scalar.var_)

coef_original = reg.coef_ / std_devs_
intercept_original = reg.intercept_ - np.sum((means_ * reg.coef_) / std_devs_)

print ('Coefficients: ', coef_original)
print ('Intercept: ', intercept_original)

X_train_1 = x_train[:,0]

regressor_1 = linear_model.LinearRegression()
regressor_1.fit(X_train_1.reshape(-1,1),y_train)
coef_1 =  regressor_1.coef_
intercept_1 = regressor_1.intercept_

print ('Coefficients: ',coef_1)
print ('Intercept: ',intercept_1)

plt.scatter(X_train_1, y_train,  color='blue')
plt.plot(X_train_1, coef_1[0] * X_train_1 + intercept_1, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")