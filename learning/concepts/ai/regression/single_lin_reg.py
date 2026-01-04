import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(url)
cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]

X = cdf.FUELCONSUMPTION_COMB.to_numpy()
y = cdf.CO2EMISSIONS.to_numpy()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(X_train.reshape(-1,1),y_train)

print(reg.coef_[0])
print(reg.intercept_)

plt.scatter(X_train, y_train,  color='blue')
plt.plot(X_train, reg.coef_ * X_train + reg.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
y_test_ = reg.predict(X_test.reshape(-1,1))


print("Mean absolute error: %.2f" % mean_absolute_error(y_test, y_test_))
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_test_))
print("Root mean squared error: %.2f" % np.sqrt(mean_squared_error(y_test, y_test_)))
print("R2-score: %.2f" % r2_score(y_test, y_test_))