import cv2
import numpy as np
from tkinter import Tk, filedialog

# Function to upload and edit the image
def upload_and_edit():
    # Open file dialog to select an image
    Tk().withdraw()  # Hide main Tkinter window
    file_path = filedialog.askopenfilename(title="Select an Image",
                                           filetypes=[("Image Files", ".jpg;.png;*.jpeg")])
    if not file_path:
        print("No file selected!")
        return

    # Read the image
    image = cv2.imread(file_path)
    if image is None:
        print("Error: Unable to load the image!")
        return

    # Resize image
    resized = cv2.resize(image, (500, 500))

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Adjust contrast & brightness
    alpha, beta = 1.5, 50  # Alpha (1.0-3.0), Beta (0-100)
    contrast = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Copy image for drawing
    image_copy = image.copy()

    # Add text
    cv2.putText(image_copy, "Edited Image", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draw a rectangle
    cv2.rectangle(image_copy, (50, 50), (300, 300), (255, 0, 0), 2)

    # Save edited image
    edited_path = "edited_image.jpg"
    cv2.imwrite(edited_path, image_copy)
    print(f"Edited image saved as {edited_path}")

    # Display images
    cv2.imshow("Original", image)
    cv2.imshow("Resized", resized)
    cv2.imshow("Grayscale", gray)
    cv2.imshow("Contrast Adjusted", contrast)
    cv2.imshow("Edited", image_copy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function
upload_and_edit()