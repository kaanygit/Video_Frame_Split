import cv2
import os

# Define the folder containing videos
video_folder = "Video-Path"

# Define the output folder for images (modify as needed)
output_folder = "Output-Path"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through all files in the video folder
for filename in os.listdir(video_folder):
    if filename.endswith("Video-Format"):  # Check for video format files only
        # Full video path
        video_path = os.path.join(video_folder, filename)

        # Create video capture object
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error opening video: {video_path}")
            continue  # Skip to next video if opening fails

        currentframe = 0

        # Get the base name of the video file
        video_name = os.path.splitext(filename)[0]

        while True:
            # Read a frame
            ret, frame = cap.read()

            if not ret:
                break  # Reached the end of the video

            # Create image filename with frame number and video name
            image_name = os.path.join(output_folder, f"{video_name}_frame_{currentframe}.jpg")
            print(f"Creating image: {image_name}")

            # Save the frame as an image
            cv2.imwrite(image_name, frame)

            currentframe += 1

        # Release video capture object
        cap.release()

print("Frame extraction completed!")
