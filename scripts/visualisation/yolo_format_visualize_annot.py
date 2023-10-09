import cv2
import os

def visualize_txt_annotations(txt_path, img_path):
    # Read the image
    img = cv2.imread(img_path)
    height, width, _ = img.shape

    # Read the .txt file
    with open(txt_path, 'r') as f:
        line = f.readline().strip()
        data = line.split()

        # Extract bounding box data
        _, x_center_rel, y_center_rel, bbox_width_rel, bbox_height_rel, *keypoints_data = data

        x_center = int(float(x_center_rel) * width)
        y_center = int(float(y_center_rel) * height)
        bbox_width = int(float(bbox_width_rel) * width)
        bbox_height = int(float(bbox_height_rel) * height)

        top_left = (x_center - bbox_width // 2, y_center - bbox_height // 2)
        bottom_right = (x_center + bbox_width // 2, y_center + bbox_height // 2)

        # Draw bounding box
        cv2.rectangle(img, top_left, bottom_right, (255, 0, 0), 2)

        # Draw keypoints
        for i in range(0, len(keypoints_data), 3):
            x_k = int(float(keypoints_data[i]) * width)
            y_k = int(float(keypoints_data[i+1]) * height)
            cv2.circle(img, (x_k, y_k), 5, (0, 255, 0), -1)

    # Display the image
    cv2.imshow(os.path.basename(img_path), img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main(txt_file_path, img_file_path):
    visualize_txt_annotations(txt_file_path, img_file_path)

# Entry point
if __name__ == "__main__":
    txt_file_path = "output/frame_0030.txt"
    img_file_path = "datasets/sls/imagesfull/frame_0030.png"
    main(txt_file_path, img_file_path)
