# HackabytesSummerHackathon

To run my EcoVision project, ensure you have Python 3.7 installed on your machine. Install the necessary Python libraries by opening a terminal or command prompt and running pip install opencv-python azure-cognitiveservices-vision-customvision msrest.

For the Bin Containment component, which monitors bin fill levels and detects plastic types using a camera, navigate to the directory containing bin_containment.py and run python bin_containment.py. Follow the prompts to either capture an image using the camera or upload an image for analysis.

The Sort Plant component captures images of items on a conveyor belt, identifies and sorts plastic types using Azure Custom Vision. Navigate to the directory containing sort_plant.py and run python sort_plant.py. Follow the prompts to either capture an image using the camera or upload an image for analysis.

The Recycling App provides a user interface for logging recycling activities, tracking rewards, and accessing educational content. Navigate to the directory containing recycling_app.py and run python recycling_app.py. Interact with the app's GUI to log activities and access features.

The Blockchain component records recycling data securely using cryptographic hashes. Navigate to the directory containing blockchain.py and run python blockchain.py. The script will continuously record recycling data to the blockchain at regular intervals.

The Upcycling Hub facilitates upcycling workshops and creative reuse of plastic waste. Navigate to the directory containing upcycling_hub.py and run python upcycling_hub.py. Follow the prompts to collect plastic waste and participate in upcycling activities.

Ensure all required libraries are installed before running any scripts. Verify that your Azure Custom Vision credentials and project details are correctly configured in the scripts. Make sure your camera is connected and working if you choose to capture images, and check the paths to any uploaded images to ensure they are correct.

If you encounter issues with missing libraries, make sure to install them using pip install (library_name). Ensure your camera is properly connected and accessible, adjusting permissions if necessary. Verify that your Azure Custom Vision credentials are correct and that your subscription is active. Following these instructions will allow you to run each component of the EcoVision project and interact with its features.

Once Again thank you for considering my project
-Abhyut Tangri
