import pandas as pd
import matplotlib.pyplot as plt 


# Read a DataFrame from a CSV file.
df = pd.read_csv('W09water.csv')

# Define a vertical bar plot from the DataFrame.
df.plot.bar(x='column_name_1', y='column_name_2')

# Draw and show all defined plots.
plt.show()