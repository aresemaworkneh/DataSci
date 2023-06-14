import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv(r"C:\Users\aworkn1\Downloads\DataMining\electricardata.csv")

# Filter out non-numeric columns
numeric_data = data.select_dtypes(include=[float, int])

# Calculate correlations
correlation_matrix = numeric_data.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Create a heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Correlation Matrix")
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the dataset
data = pd.read_csv(r"C:\Users\aworkn1\Downloads\DataMining\electricardata.csv")

# Filter out non-numeric columns
numeric_data = data.select_dtypes(include=[float, int])

# Calculate correlations
correlation_matrix = numeric_data.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Create a heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Correlation Matrix")
plt.show()
