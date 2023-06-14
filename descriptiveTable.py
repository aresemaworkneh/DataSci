import pandas as pd
import webbrowser

# Read the dataset
data = pd.read_csv(r"C:\Users\aworkn1\Downloads\DataMining\electricardata.csv")

# Convert columns to numeric type
data = data.apply(pd.to_numeric, errors='coerce')

# Calculate mean, median, and standard deviation
minimum_value = data.min()
maximum_value = data.max()
range_value = maximum_value.sub(minimum_value).fillna('')
count = data.count()
sum_value = data.sum()
mean_value = data.mean()
median_value = data.median()
mode_value = data.mode().iloc[0]

# Create the stats table
stats_table = pd.DataFrame({
    'Minimum': minimum_value,
    'Maximum': maximum_value,
    'Range': range_value,
    'Count': count,
    'Sum': sum_value,
    'Mean': mean_value,
    'Median': median_value,
    'Mode': mode_value
})

# Apply styling to the table
styled_table = stats_table.style.set_table_styles([
    {'selector': 'th', 'props': [('font-family', 'sans-serif'), ('padding', '12px 15px'), ('background-color', '#009879'), ('text-align', 'left'), ('color', '#ffffff'), ('font-weight', 'bold'),]},
    {'selector': 'tr:nth-child(odd)', 'props': [('font-family', 'sans-serif'), ('background-color', '#e6e6e6')]},
    {'selector': 'tr:nth-child(even)', 'props': [('font-family', 'sans-serif'), ('background-color', '#f3f3f3')]},
    {'selector': 'td', 'props': [('font-family', 'sans-serif'), ('text-align', 'center')]},
    {'selector': 'caption', 'props': [('font-family', 'sans-serif'), ('caption-side', 'bottom'), ('text-align', 'right')]}
])

# Save the styled table to an HTML file
styled_table_html = styled_table.render()
with open('descriptive_stats.html', 'w') as file:
    file.write(styled_table_html)

# Open the HTML file in a new tab
new_tab = webbrowser.open_new_tab('descriptive_stats.html')
