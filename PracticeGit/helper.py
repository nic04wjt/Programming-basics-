# =====================================================================
# HOW TO START A VIRTUAL ENVIRONMENT & INSTALL LIBRARIES (In your Terminal):
# 
# 1. Create the environment:  python -m venv env
# 2. Activate it:
#    - Windows:               env\Scripts\activate
#    - Mac/Linux:             source env/bin/activate
# 3. Install libraries:       pip install pandas numpy matplotlib
# =====================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. PANDAS: Load the file
def load_csv(dataset):
    return pd.read_csv(dataset)

# 2. NUMPY: Convert data and run math operations
def process_data(df, column_name):
    # Convert the column into a numpy array
    y_array = df[column_name].to_numpy()
    
    # Numpy Operation 1: Fix broken/missing data by turning NaNs into 0
    y_cleaned = np.nan_to_num(y_array)
    
    # Numpy Operation 2 & 3: Print quick statistics
    print(f"Max Value: {np.max(y_cleaned)}")
    print(f"Average Value: {np.mean(y_cleaned)}")
    
    return y_cleaned

# 3. MATPLOTLIB: Plot the data
def plot_data(df, x_column, y_array):
    plt.plot(df[x_column], y_array)
    plt.show()

# ==========================================
# HOW TO RUN IT IN PYTHON:
# ==========================================
# df = load_csv("data.csv")
# y_data = process_data(df, "Prices")
# plot_data(df, "Dates", y_data)
