import os
import shutil
import csv

# Function to move images to cluster subfolders based on cluster labels
def move_images_to_clusters(image_folder_path, csv_file_path):
    # Create cluster subfolders
    for i in range(desired_number_of_clusters):
        cluster_folder_path = os.path.join(image_folder_path, f"Cluster_{i}")
        os.makedirs(cluster_folder_path, exist_ok=True)

    # Read CSV file
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            file_name = row[0]
            cluster_label = row[-1]  # Assuming cluster label is in the last column
            source_path = os.path.join(image_folder_path, file_name)
            destination_path = os.path.join(image_folder_path, f"Cluster_{cluster_label}", file_name)
            shutil.move(source_path, destination_path)

# Example usage
image_folder_path = r"C:\Users\Pratyush Ranjan\Desktop\DS203\Assignment 7\E7-images-Real"
csv_file_path = r"image_features_with_labels.csv"
desired_number_of_clusters = 3

move_images_to_clusters(image_folder_path, csv_file_path)
