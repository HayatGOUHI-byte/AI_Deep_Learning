import cv2

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur to smoothen the image
    blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
    
    # Apply thresholding to segment the image
    _, thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Perform any additional preprocessing steps if needed
    
    return thresholded_image

# Example usage:
image_path = "example.jpg"
processed_image = preprocess_image(image_path)

# Display the processed image
cv2.imshow("Processed Image", processed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
