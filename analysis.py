
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')

# Basic analysis
print("Total Revenue:", df['Revenue'].sum())
print("Average Price:", df['Price'].mean())

# Revenue by product
rev_product = df.groupby('Product')['Revenue'].sum()
print(rev_product)

# Visualization
rev_product.plot(kind='bar')
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.savefig("revenue_by_product.png")
plt.show()
