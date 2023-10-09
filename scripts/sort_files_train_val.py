import os
import shutil
import random

# Paths
output_labels_path = "output/"
images_full_path = "datasets/sls/imagesfull/"
labels_train_path = "datasets/sls/labels/train/"
labels_val_path = "datasets/sls/labels/val/"
images_train_path = "datasets/sls/images/train/"
images_val_path = "datasets/sls/images/val/"

# List all the .txt files in the output folder
txt_files = [f for f in os.listdir(output_labels_path) if f.endswith('.txt')]

# Shuffle the list of txt files
random.shuffle(txt_files)

# 80-20 split
num_train = int(0.8 * len(txt_files))
train_txt_files = txt_files[:num_train]
val_txt_files = txt_files[num_train:]

# Move the .txt files and corresponding images to train or val folder
for txt_file in train_txt_files:
    shutil.move(os.path.join(output_labels_path, txt_file), os.path.join(labels_train_path, txt_file))
    # Image file with same name but .png extension
    img_file = txt_file.replace('.txt', '.png')
    shutil.move(os.path.join(images_full_path, img_file), os.path.join(images_train_path, img_file))

for txt_file in val_txt_files:
    shutil.move(os.path.join(output_labels_path, txt_file), os.path.join(labels_val_path, txt_file))
    img_file = txt_file.replace('.txt', '.png')
    shutil.move(os.path.join(images_full_path, img_file), os.path.join(images_val_path, img_file))
