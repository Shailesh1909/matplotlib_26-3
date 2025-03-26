# 5. Top 5 Best-Selling Products (Bar Chart)
import matplotlib.pyplot as plt

products = ["Laptop", "Phone", "Shoes", "Watch", "Bag"]
units_sold = [150, 200, 250, 180, 220]
 
plt.figure(figsize=(8,5))
plt.barh(products, units_sold, color='cyan')
plt.xlabel("Units Sold")
plt.ylabel("Products")
plt.title("Top 5 Best-Selling Products")
plt.savefig("E_barchart2.png")
plt.show()
