import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
import cv2
import json

# Load CSV
df = pd.read_csv('updated_annotations_file.csv')

# Loop through each row
for _, row in df.iterrows():
    # Read image
    img_path = row['img']
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Parse the keypoints
    keypoints = json.loads(row['kp-1'])
    
    # Plot the image and keypoints
    fig, ax = plt.subplots(1, figsize=(12, 9))  # You can adjust the figure size as needed
    ax.imshow(img)
    
    for point in keypoints:
        x = point['x'] * point['original_width'] / 100  # Convert percentage to absolute
        y = point['y'] * point['original_height'] / 100
        label = point['keypointlabels'][0]  # Assuming there's only one label per point

        circle = patches.Circle((x, y), radius=5, color='red')  # You can adjust the radius and color
        ax.add_patch(circle)
        ax.text(x + 5, y, label, color='white', fontsize=12, bbox=dict(facecolor='red', edgecolor='red', boxstyle='round'))
    
    plt.show()
