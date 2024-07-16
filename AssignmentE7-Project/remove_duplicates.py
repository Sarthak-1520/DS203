import os
import hashlib

def remove_duplicate_images(image_folder_path):
    # Dictionary to store hash values and corresponding file paths
    hash_dict = {}

    # Iterate through each image file in the directory
    for filename in os.listdir(image_folder_path):
        file_path = os.path.join(image_folder_path, filename)

        # Calculate hash value for the image file
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()

        # Check if the hash value already exists in the dictionary
        if file_hash in hash_dict:
            # Duplicate found, delete the file
            print(f"Removing duplicate image: {filename}")
            os.remove(file_path)
        else:
            # Add the hash value and file path to the dictionary
            hash_dict[file_hash] = file_path

    print("Duplicate images removed.")

# Example usage
image_folder_path = "C:\\Users\\Pratyush Ranjan\\Desktop\\DS203\\Assignment 7\\E7-images"
remove_duplicate_images(image_folder_path)
