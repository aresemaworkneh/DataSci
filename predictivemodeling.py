import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Read the dataset

data = pd.read_csv(r"C:\Users\aworkn1\Downloads\DataMining\electricardata.csv")
# Replace "?" with NaN
data.replace("?", np.nan, inplace=True)

# Drop rows with missing values
data.dropna(inplace=True)

# Select features and target variable
features = data[["Mpg", "Cylinders", "Displacement", "Weight", "Acceleration"]]
target = data['Horsepower']

# Convert columns to numeric type
features = features.apply(pd.to_numeric)
target = target.apply(pd.to_numeric)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Calculate mean squared error
mse = mean_squared_error(y_test, y_pred)

# Display the results in a table
results_table = pd.DataFrame({'Actual Horsepower': y_test, 'Predicted Horsepower': y_pred})
print(results_table)

# Plot a scatter plot of the actual vs. predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Horsepower')
plt.ylabel('Predicted Horsepower')
plt.title('Linear Regression Results')
plt.show()
