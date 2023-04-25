import os
import cv2
import numpy as np
from google.cloud import vision

# Set the Google Cloud Vision API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

# Define a function to scan a receipt or invoice
def scan(image_path):
# Read the image
    image = cv2.imread(image_path)

# Create a Vision client
    vision_client = vision.ImageAnnotatorClient()

# Convert the image to a bytestring
    image_bytes = cv2.imencode('.jpg', image)[1].tostring()

# Create a request object
    request = vision_client.text_detection(image=image_bytes)

# Run the request
    response = vision_client.execute(request)

# Extract the text from the response
    text = response.text_annotations[0].description

# Print the text
    print(text)

# Define a function to take a picture of a receipt or invoice
def take_picture():
# Capture the image from the camera
    image = cv2.imshow('Take a picture', cv2.imread('capture.png'))

# Wait for the user to press a key
    cv2.waitKey(0)

# Save the image
    cv2.imwrite('capture.png', image)

# Scan the image
    scan('capture.png')

# Define a function to upload a picture of a receipt or invoice
def upload_picture():
# Get the image path from the user
    image_path = input('Enter the image path: ')

# Scan the image
    scan(image_path)

# Main function
if __name__ == '__main__':
# Choose an option
    print('What would you like to do?')
    print('1. Scan a receipt or invoice')
    print('2. Take a picture of a receipt or invoice')
    print('3. Upload a picture of a receipt or invoice')

# Get the user's choice
    choice = int(input('Enter your choice: '))

# Do the corresponding action
    if choice == 1:
        scan('RECEIPT_IMAGE.jpg')
    elif choice == 2:
        take_picture()
    elif choice == 3:
        upload_picture()