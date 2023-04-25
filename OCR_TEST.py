import cv2
import pytesseract
import json

# Preprocess the image
def preprocess(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply a Gaussian blur to remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Apply adaptive thresholding to binarize the image
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh

# Extract text from the image
def extract_text(image):
    # Apply OCR to the image
    text = pytesseract.image_to_string(image)
    return text

# # Parse the extracted text to extract relevant information
# def parse_text(text):
#     # Use NLP techniques to identify relevant information
#     # ...
#     return data_dict

# Return the extracted data in JSON format
def return_json(data_dict):
    # Convert the data dictionary to JSON format
    json_data = json.dumps(data_dict, indent=4)
    return json_data

# Main function to process the receipt image and return data in JSON format
def process_receipt_image(image):
    # Preprocess the image
    preprocessed_image = preprocess(image)
    # Extract text from the image
    text = extract_text(preprocessed_image)
    # Parse the extracted text to extract relevant information
    #data_dict = parse_text(text)
    # Return the extracted data in JSON format
    json_data = return_json(text)
    return json_data


img_path = 'RECEIPT_IMAGE.jpg'
src = cv2.imread(img_path)

print(process_receipt_image(src))

