import os
import pandas as pd

# Specify the folder path
folder_path = 'C:/Users/kyu11/Documents/GitHub/python/23.01.28/23.05.15/23.05.16'

# Get all file paths in the folder
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        file_paths.append(os.path.join(root, file))

# Create a DataFrame from the file paths
df = pd.DataFrame({'File Path': file_paths})

# Display the DataFrame
print(df)