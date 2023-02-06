from PIL import Image

# Open the image file
img = Image.open("/home/patali/Trial_ROOM/test.jpg")

# Get the size of the image
width, height = img.size

# Loop through all pixels
red_hex_values = []
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        # If the red value is the maximum of the three color channels, then the pixel is red

        hex_value = '{:02x}'.format(r)
        red_hex_values.append(hex_value)

print(red_hex_values)
