import pandas as pd

# Load the two CSV files into pandas DataFrames
csv_file1 = r"image_features.csv"
csv_file2 = r"image_cluster_labels.csv"

df1 = pd.read_csv(csv_file1)
df2 = pd.read_csv(csv_file2)

# Merge the DataFrames based on the common feature (image name)
merged_df = pd.merge(df1, df2, on='File Name', how='outer')

# Write the merged DataFrame to a new CSV file
merged_csv_file = "merged_csvCNN.csv"
merged_df.to_csv(merged_csv_file, index=False)

print("Merged CSV file saved as", merged_csv_file)
