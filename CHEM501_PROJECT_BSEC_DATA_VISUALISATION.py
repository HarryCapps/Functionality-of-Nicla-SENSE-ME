import pandas as pd   
import numpy as np   
import matplotlib.pyplot as plt   

# Define the data   
data_set_1 = {   

    "Minutes": [   

        0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9,   

        9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5, 14, 14.5, 15, 15.5, 16, 16.5,   

        17, 17.5, 18, 18.5, 19, 19.5, 20, 20.5, 21, 21.5, 22, 22.5, 23, 23.5, 24,   

        24.5, 25, 25.5, 26, 26.5, 27, 27.5, 28, 28.5, 29, 29.5, 30, 30.5, 31, 31.5,   

        32, 32.5, 33, 33.5, 34, 34.5, 35, 35.5, 36, 36.5, 37, 37.5, 38, 38.5, 39,   

        39.5, 40, 40.5, 41, 41.5, 42, 42.5, 43, 43.5, 44, 44.5, 45, 45.5, 46, 46.5,   

        47, 47.5, 48, 48.5, 49, 49.5, 50, 50.5, 51, 51.5, 52, 52.5, 53, 53.5, 54,   

        54.5, 55, 55.5, 56, 56.5, 57, 57.5, 58, 58.5, 59, 59.5, 60   

    ],   

    "IAQ": [   

        25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 27, 29, 35, 39,   

        52, 46, 50, 54, 50, 41, 30, 39, 49, 41, 35, 39, 33, 41, 32, 32, 32, 45, 38,   

        42, 38, 35, 0, 0, 0, 0, 0, 0, 32, 43, 43, 58, 62, 93, 87, 106, 102, 97, 107,   

        101, 103, 98, 105, 103, 90, 85, 88, 93, 95, 105, 94, 88, 85, 91, 91, 81, 74,   

        75, 79, 96, 107, 93, 95, 94, 92, 91, 112, 96, 91, 91, 87, 76, 97, 106, 111,   

        137, 103, 83, 89, 93, 103, 100, 85, 91, 102, 98, 92, 99, 104, 100, 102, 125,   

        99, 96, 102, 95, 87, 86, 74, 90, 104, 91   

    ],   

    "Accuracy": [   

        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,   

        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1   

    ]   

}   

# DataFrame Creation   
df = pd.DataFrame(data_set_1)    
# Colour mapping Defined  
color_map = {0: 'red', 1: 'blue', 2: 'green', 3: 'orange'}   
  
# Calculate the line of best fit   
x = df["Minutes"]   
y = df["IAQ"]   
coefficients = np.polyfit(x, y, 1)  # 1 indicates a linear fit   
line_of_best_fit = np.poly1d(coefficients)   
y_fit = line_of_best_fit(x)     

# Plotting the data with connecting lines and the line of best fit   
fig, ax = plt.subplots(figsize=(12, 6))   

# Plot the original data with connecting lines   
for acc in df["Accuracy"].unique():   

    subset = df[df["Accuracy"] == acc]   

    ax.plot(subset["Minutes"], subset["IAQ"],   

            color=color_map[acc], label=f"Accuracy {acc}", marker='o')   
  
# Plot the line of best fit   
ax.plot(x, y_fit, color="black", linestyle="--", label="Line of Best Fit")   

# Adding labels, legend, and grid   
ax.set_title("IAQ vs. Time with Line of Best Fit", fontsize=14)   
ax.set_xlabel("Minutes", fontsize=12)   
ax.set_ylabel("IAQ (Index Air Quality)", fontsize=12)   
ax.legend(title="Accuracy Levels", fontsize=10)   
plt.grid(True)   
plt.tight_layout()   
  
# Show the plot   
plt.show() 

 
