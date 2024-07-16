import cv2
import numpy as np
import os
import csv

def calculate_length_width(contours):
    lengths = []
    widths = []
    for contour in contours:
        rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        width = round(np.linalg.norm(box[0] - box[1]),2)
        height =round(np.linalg.norm(box[1] - box[2]),2)
        lengths.append(max(width, height))
        widths.append(min(width, height))
    return lengths, widths

# Path to the directory containing images
image_dir = r'C:\Users\Pratyush Ranjan\Desktop\DS203\Assignment 7\E7-images(Unique)'

# Initialize the CSV file for writing
output_csv_file = "image_features.csv"
with open(output_csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['File Name', 'Length', 'Width'])  # Header row

    # Loop through all images in the directory
    for filename in os.listdir(image_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Check if the file is an image
            image_path = os.path.join(image_dir, filename)
            image = cv2.imread(image_path)

            # Convert the image to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Apply Canny edge detection (optional)
            edges = cv2.Canny(gray, 30, 150)

            # Find contours
            contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Calculate length and width of tight-fitting bounding box
            lengths, widths = calculate_length_width(contours)

            # Write the results to the CSV file
            for length, width in zip(lengths, widths):
                writer.writerow([filename, length, width])

print("Image features saved to", output_csv_file)
