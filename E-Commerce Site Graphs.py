# E-Commerce Site Graphs
# 4. Sales Trends Over 6 Months (Line Chart)
import matplotlib.pyplot as plt

# months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# applications = [120, 150, 180, 200, 170, 190]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [20000, 25000, 30000, 28000, 35000, 40000]
 
plt.figure(figsize=(8,5))
plt.plot(months, sales, marker='o', linestyle='-', color='orange')
plt.xlabel("Months")
plt.ylabel("Sales Revenue ($)")
plt.title("E-Commerce Sales Trends Over 6 Months")
plt.grid(True)
plt.savefig("Linechart.png")
plt.show()


