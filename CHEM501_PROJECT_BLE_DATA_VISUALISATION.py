import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

# Define the dataset  

data_devices_set_1 = {  

    "Minutes": [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60],  

    "Total Devices": [20, 33, 38, 50, 50, 50, 50, 50, 50, 50, 50, 50]  

}  

# Create a DataFrame  
df_devices = pd.DataFrame(data_devices_set_1)  

# Calculate the line of best fit  
x_devices = df_devices["Minutes"]  
y_devices = df_devices["Total Devices"]  
coefficients_devices = np.polyfit(x_devices, y_devices, 1)  # Linear fit  
line_of_best_fit_devices = np.poly1d(coefficients_devices)  
y_fit_devices = line_of_best_fit_devices(x_devices)  

# Plotting the data and the line of best fit  
fig, ax = plt.subplots(figsize=(10, 6))  

# Plot the data points  
ax.plot(df_devices["Minutes"], df_devices["Total Devices"], color="blue", marker="o", label="Total Devices")  

# Plot the line of best fit  
ax.plot(x_devices, y_fit_devices, color="black", linestyle="--", label="Line of Best Fit")  

# Adding labels, legend, and grid  
ax.set_title("Total Devices vs. Time with Line of Best Fit", fontsize=14)  
ax.set_xlabel("Minutes", fontsize=12)  
ax.set_ylabel("Total Devices", fontsize=12)  
ax.legend(fontsize=10)  
plt.grid(True)  
plt.tight_layout()  

# Show the plot  
plt.show() 