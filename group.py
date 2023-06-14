import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\aworkn1\Downloads\DataMining\electricardata.csv")

# Extract the required data columns
x = data['Year']
y = data['Mpg']

# Create a line graph
plt.plot(x, y)
plt.xlabel('Year')
plt.ylabel('MPG')
plt.title('MPG Over Time')
plt.grid(True)
plt.show()
