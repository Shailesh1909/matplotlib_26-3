import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
applications = [120, 150, 180, 200, 170, 190]

# Create a bar chart
plt.figure(figsize=(10, 5))
plt.bar(months, applications, color='skyblue')

# Add titles and labels
plt.xlabel("Month")
plt.ylabel("Number of Applications")
plt.title("Visa Applications Per Month")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()

 