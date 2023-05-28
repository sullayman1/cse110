from PIL import Image


# # milestone requirements
# image_beach = Image.open('beach.jpg')
# pixels_beach = image_beach.load()

# for x in range (0, 5):
#     print(pixels_beach[100+x,200])
#     pixels_beach[100+x, 200] = (0, 0, 0)

# image_beach.show()

# Final Requirements

image_foreground = Image.open('cactus.jpg')
image_background = Image.open('beach.jpg')
image_combined = Image.new('RGB', image_foreground.size)

(width, height) = image_foreground.size
pixels_foreground = image_foreground.load()
pixels_background = image_background.load()
pixels_new_image = image_combined.load()

for y in range (0, height):
    for x in range (0, width):
        (r, g, b) = pixels_foreground[x,y]
        if (g > 150) and (r < 150 and b < 150):
            pixels_new_image[x,y] = pixels_background[x,y]
        else:
            pixels_new_image[x,y] = pixels_foreground[x,y]

image_combined.save('combined.jpg')
image_combined.show()