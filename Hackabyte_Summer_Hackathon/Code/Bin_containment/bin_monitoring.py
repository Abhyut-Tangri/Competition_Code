import random
import time
import cv2
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Function to capture an image using the camera
def capture_bin_image():
    # Initialize the camera
    camera = cv2.VideoCapture(0)
    # Set the camera resolution
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # Capture an image
    ret, image = camera.read()
    # Save the captured image to a file
    image_path = 'capture.png'
    cv2.imwrite(image_path, image)
    # Release the camera resource
    camera.release()
    # Return the path to the captured image
    return image_path

# Function to load an image from a specified path
def load_image(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    # Check if the image was loaded correctly
    if image is None:
        print("Error: Image not loaded correctly.")
    # Return the loaded image
    return image

# Function to log the current bin level and plastic type data to a local file
def log_data_locally(current_level, plastic_type):
    # Open the log file in append mode
    with open('bin_data_log.txt', 'a') as log_file:
        # Write the bin level and plastic type to the log file
        log_file.write(f"Bin Level: {current_level}%, Plastic Type: {plastic_type}\n")
    # Print a confirmation message
    print(f"Logged data locally: Bin Level: {current_level}%, Plastic Type: {plastic_type}")

# Function to detect plastic using Azure Custom Vision
def detect_plastic(image_path):
    # Set up the credentials for Azure Custom Vision
    credentials = ApiKeyCredentials(in_headers={'Prediction-Key': '2324ec2b7a8d4701b31acd750c4c3765'})
    # Initialize the prediction client
    predictor = CustomVisionPredictionClient('https://westus2.api.cognitive.microsoft.com/', credentials)
    
    # Open the image file in binary mode
    with open(image_path, mode='rb') as captured_image:
        # Use the predictor to detect objects in the image
        results = predictor.detect_image('c34c1e8b-7f04-47cd-9449-59e886d411d6', 'BottleChecked2', captured_image)

    # Iterate over the predictions
    for prediction in results.predictions:
        # Check if the prediction probability is greater than 0.2
        if prediction.probability > 0.2:
            return True  # Plastic detected
    return False  # No plastic detected

# Function to choose between capturing an image or uploading an image
def choose_image_source():
    # Prompt the user to choose the image source
    choice = input("Choose image source: (1) Capture from camera (2) Upload image: ")
    if choice == '1':
        # Capture an image using the camera
        return capture_bin_image()
    elif choice == '2':
        # Prompt the user to enter the path to the image
        image_path = input("Enter the path to the image (use raw string format, e.g., r'C:\\path\\to\\image.jpg'): ")
        # Ensure the input is treated as a raw string literal
        return fr"{image_path}"
    else:
        # Handle invalid choices (breaks)
        exit()

# Main function to monitor the bin
def bin_monitoring_process():
    while True:
        # Choose the image source (capture or upload)
        image_path = choose_image_source()
        # Load the image
        image = load_image(image_path)
        
        # If the image is not loaded correctly, continue to the next iteration
        if image is None:
            continue
        
        # Simulate getting the current bin level
        current_level = random.randint(0, 100)
        # Detect if there is any plastic in the image
        plastic_detected = detect_plastic(image_path)

        if plastic_detected:
            # If plastic is detected, log the data and print a message
            print("Recyclable plastic has been scanned.")
            plastic_type = "Plastic"  # You can refine this based on your detection model
            log_data_locally(current_level, plastic_type)
        
        if current_level > 75:
            # If the bin level is greater than 75%, print an alert message
            print("Alert: Bin is almost full. Collection needed.")
        else:
            # Otherwise, print that the bin status is okay
            print("Bin status is okay.")

        # Wait for 5 minutes before the next iteration
        time.sleep(5 * 60)

# Entry point of the script
if __name__ == "__main__":
    # Start the bin monitoring process
    bin_monitoring_process()
