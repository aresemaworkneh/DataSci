import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
data = pd.read_csv(r"C:\Users\aworkn1\H:\DataMining\electricardata.csv")

# Replace "?" with NaN
data.replace("?", np.nan, inplace=True)

# Convert columns to appropriate data types
numeric_columns = ["Mpg", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration"]
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric)

# Check the distribution of the target variable
print(data['Mpg'].describe())

# Fill missing values with the median of the respective columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numeric_columns])

# Fit KMeans
kmeans = KMeans(n_clusters=6, random_state=42)
kmeans.fit(scaled_data)

# Add the cluster labels for each data point to the dataframe
data['Cluster'] = kmeans.labels_
data['MPG'] = data['Mpg']  # Add a separate column for MPG

# Plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=data, x='Mpg', y='Horsepower', hue='Cluster', palette='deep')
plt.title('Clustering Results of Mpg vs Horsepower')
plt.show()
