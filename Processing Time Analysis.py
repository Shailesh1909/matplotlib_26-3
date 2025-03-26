# 3. Visa Processing Time (Line Chart)
import matplotlib.pyplot as plt


visa_types = ["Tourist", "Business", "Student", "Work"]
processing_days = [10, 15, 30, 45]
 
plt.figure(figsize=(8,5))
plt.plot(visa_types, processing_days, marker='o', linestyle='-', color='purple')
plt.xlabel("Visa Type")
plt.ylabel("Processing Time (Days)")
plt.title("Average Visa Processing Time by Type")
plt.grid(True)
plt.savefig("E_linechart.png")
plt.show()