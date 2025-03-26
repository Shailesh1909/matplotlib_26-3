# 6. Orders by Category (Pie Chart)

import matplotlib.pyplot as plt
categories = ["Electronics", "Clothing", "Home Appliances", "Books", "Accessories"]
orders = [300, 500, 200, 150, 250]
colors = ["blue", "green", "red", "purple", "orange"]
 
plt.figure(figsize=(6,6))
plt.pie(orders, labels=categories, autopct="%1.1f%%", colors=colors, startangle=90)
plt.title("Orders by Category")
plt.savefig("E_Piechart2.png")
plt.show()