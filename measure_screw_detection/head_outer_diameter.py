import cv2
from image_white_background import output_path


#pixels轉換直徑變數
pixels_to_diamter_parameter=0.001276


# Read the image
#img = cv2.imread('5.png')
img=cv2.imread(output_path)

# Resize the image to double its size
img = cv2.resize(img, (0,0), fx=2, fy=2)


# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using the Canny algorithm
edges = cv2.Canny(blur, 50, 150)

# Find contours in the image
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the largest area
max_contour = max(contours, key=cv2.contourArea)

# Get the bounding rectangle of the contour
x, y, w, h = cv2.boundingRect(max_contour)

# Calculate the diameter of the screw head
diameter = w

#print(diameter)

diameter_transfer_to_cm=diameter*pixels_to_diamter_parameter #pixels轉換真實直徑，有一點誤差，也會因為照片和鏡頭距離的大小影響pixels


diameter_str = f'{diameter_transfer_to_cm:.3f}'


# Draw the bounding rectangle on the original image
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Add text to the image with the diameter
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, f'Diameter: {diameter_str} cm', (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

#print(f"螺絲直徑 {'{:.3f}'.format(diameter*0.0012767)} cm")

# Display the result
cv2.imshow('Screw Head', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
