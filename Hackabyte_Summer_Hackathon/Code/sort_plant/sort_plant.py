import cv2
import time
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

# Initialize the prediction client for Azure Custom Vision
credentials = ApiKeyCredentials(in_headers={'Prediction-Key': '2324ec2b7a8d4701b31acd750c4c3765'})
predictor = CustomVisionPredictionClient('https://westus2.api.cognitive.microsoft.com/', credentials)

# Function to capture an image using the camera
def capture_item_image():
    # Initialize the camera
    camera = cv2.VideoCapture(0)
    # Set the camera resolution
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    # Capture an image
    ret, image = camera.read()
    # Save the captured image to a file
    image_path = 'item_capture.png'
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

# Function to choose between capturing an image or uploading an image
def choose_image_source():
    # Prompt the user to choose the image source
    choice = input("Choose image source: (1) Capture from camera (2) Upload image: ")
    if choice == '1':
        # Capture an image using the camera
        return capture_item_image()
    elif choice == '2':
        # Prompt the user to enter the path to the image
        image_path = input("Enter the path to the image (use raw string format, e.g., r'C:\\path\\to\\image.jpg'): ")
        # Ensure the input is treated as a raw string literal
        return fr"{image_path}"
    else:
        # Handle invalid choices
        exit()

# Function to detect plastic type using Azure Custom Vision
def detect_plastic_type(image_path):
    # Open the image file in binary mode
    with open(image_path, mode='rb') as captured_image:
        # Use the predictor to detect objects in the image
        results = predictor.detect_image('c34c1e8b-7f04-47cd-9449-59e886d411d6', 'BottleChecked2', captured_image)
    
    # Print out the raw results for debugging
    
    
    for prediction in results.predictions:
        if prediction.probability > 0.2:
            return prediction.tag_name  # Return the detected plastic type
    return "Unknown"  # If no plastic is detected or confidence is low

# Function to sort the item based on the detected plastic type
def sort_item(plastic_type):
    # Implement your sorting logic here
    if plastic_type != "Unknown":
        print(f"Sorting successful")
    else:
        print("Sorting failed: Plastic type could not be identified.")

# Main process for sorting plant
def sorting_process():
    while True:
        # Choose the image source (capture or upload)
        image_path = choose_image_source()
        # Load the image
        image = load_image(image_path)
        
        # If the image is not loaded correctly, continue to the next iteration
        if image is None:
            continue
        
        # Detect the type of plastic in the image
        plastic_type = detect_plastic_type(image_path)
        # Sort the item based on the detected plastic type
        sort_item(plastic_type)

        # Wait for 1 second before processing the next item
        time.sleep(1)

# Entry point of the script
if __name__ == "__main__":
    # Start the sorting process
    sorting_process()
