import cv2
import os

def extract_frames(video_path, output_folder, target_fps=5):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video using OpenCV
    cap = cv2.VideoCapture(video_path)

    # Get the original video's FPS
    original_fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Calculate the frame skip (how many frames to skip to achieve the target_fps)
    frame_skip = original_fps // target_fps

    frame_count = 0
    saved_frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save only if the current frame is a multiple of frame_skip
        if frame_count % frame_skip == 0:
            output_path = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.png")
            cv2.imwrite(output_path, frame)
            saved_frame_count += 1

        frame_count += 1

    cap.release()
    print(f"Saved {saved_frame_count} frames to {output_folder}")

if __name__ == "__main__":
    video_path = "data/videos/SLS_only_skate.mov"
    output_folder = "data/sls/output_frames"
    extract_frames(video_path, output_folder)
