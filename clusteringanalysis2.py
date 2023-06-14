import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the data
data = pd.read_csv(r"C:\Users\aworkn1\Downloads\DataMining\electricardata.csv")

# Replace "?" with NaN
data.replace("?", np.nan, inplace=True)

# Convert columns to appropriate data types
numeric_columns = ["Mpg", "Cylinders", "Displacement", "Horsepower", "Weight", "Acceleration"]
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric)

# Fill missing values with median of the column
data["Horsepower"] = data["Horsepower"].fillna(data["Horsepower"].median())

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[numeric_columns])

# Perform Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=6)
cluster_labels = hierarchical.fit_predict(scaled_data)

# Add the cluster labels for each data point to the dataframe
data['Cluster'] = cluster_labels

# Plot
plt.figure(figsize=(12, 8))
sns.scatterplot(data=data, x='Mpg', y='Horsepower', hue='Cluster', palette='deep')
plt.title('Hierarchical Clustering Results')
plt.show()
