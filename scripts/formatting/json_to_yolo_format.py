import json
import os

def transform_annotation(data):
    transformed_annotations = {}

    # Map image id to file name and dimensions for easy lookup
    image_id_to_details = {img['id']: (img['file_name'], img['width'], img['height']) for img in data['images']}

    for anno in data['annotations']:
        # Extract bounding box data and normalize
        x, y, bbox_width, bbox_height = anno['bbox']
        image_name, img_width, img_height = image_id_to_details[anno['image_id']]
        
        x_center = x + bbox_width / 2
        y_center = y + bbox_height / 2
        
        x_center /= img_width
        y_center /= img_height
        bbox_width /= img_width
        bbox_height /= img_height

        # Extract and normalize keypoints data
        keypoints = anno['keypoints']
        normalized_keypoints = []

        # Normalize every 3 values in keypoints as <x, y, visibility>
        for i in range(0, len(keypoints), 3):
            x_k = keypoints[i] / img_width
            y_k = keypoints[i+1] / img_height
            visibility = 2  # Always set visibility to 2
            normalized_keypoints.extend([x_k, y_k, visibility])

        # Construct new format with at most 6 decimal places
        new_format = ['0', 
                      "{:.6f}".format(x_center), 
                      "{:.6f}".format(y_center), 
                      "{:.6f}".format(bbox_width), 
                      "{:.6f}".format(bbox_height)]
        new_format.extend(["{:.6f}".format(val) for val in normalized_keypoints])

        # Determine the corresponding file name
        file_name = image_name.replace('.png', '')
        transformed_annotations[file_name] = " ".join(new_format)

    return transformed_annotations


def main(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as f:
        data = json.load(f)

    # Transform annotations
    transformed_annotations = transform_annotation(data)

    # Ensure output directory exists
    if not os.path.exists('annotations/output'):
        os.makedirs('annotations/output')

    # Write transformed annotations to separate text files
    for file_name, annotation in transformed_annotations.items():
        with open(f'annotations/output/{file_name}.txt', 'w') as out_file:
            out_file.write(annotation)


# Entry point
if __name__ == "__main__":
    json_file_path = "annotations/annotations-4.json"
    main(json_file_path)
