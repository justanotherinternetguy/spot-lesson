from PIL import Image

# Load the original PNG image
original_image = Image.open('tag25_09_00000.png')

# Define the desired upscale factor
upscale_factor = 100  # Replace with the desired value

# Calculate the new width and height
new_width = original_image.width * upscale_factor
new_height = original_image.height * upscale_factor

# Perform the upscale using the 'NEAREST' resampling method for a lossless result
upscaled_image = original_image.resize((new_width, new_height), resample=Image.NEAREST)

# Save the upscaled image as a new PNG file
upscaled_image.save('upscaled_image.png')
