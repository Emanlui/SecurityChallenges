from PIL import Image
from PIL import ImageFilter

#										hsl (0-120 ; 120-240; 240-360 this is the color,
#											 saturation is a percentage 100%,
#											 brightness is a percentage 50%)
new_image = Image.new ("RGB", new_size, "rgb (255,255,255)")

#
image1 = Image.open('image_name.extension')
image2 = Image.open('image_name.extension')

# create a tuple with the width and height of the image
size = width,height = image1.size

# merge two images into one, the float means the percentage of every image blending
# if it is 0.0 the image1 is only shown, if it is 1.0 image2 is only shown, so 0.5 is the merge
# both images must have same size and mode (RGB)
Image.blend(image1, image2, 0.5).show()

# it merge two images with composition settings
Image.composite(image1, image2, image2).show()

# changes the channel to a new one
image1.convert("L").show()

# it crops an image
image1.crop( (10,10,10,10) ).show

# it sets a filter to the image, it also uses the imagefilter library
image.filter( ImageFilter.DETAIL ).show()
# save an image
new.save('new.jpg')

# show an image
new.show()

# prints the pixel color of an image, it can be a slow
print image1.getpixel( (x,y) )

# gets all the pixel information of an image
image1.getdata()

# paste some image into a especific box
image.paste(some_image_or_color,(10,10,10,10))

# resize the image... 
image1.resize((x,y))

# rotate the image with degrees values
image1.rotate(90)


color_to_find = (0,0,0,0)
color_to_replace = (255,255,255,255)

rotated_image = image1.rotate(45)

new_image_data = []

# it changes the color found and replace it 
for color in list(image1.getdata()):
	if(color = color_to_find):
		new_image_data += [color_to_replace]
	else:
		new_image_data += [color]
#then it saves it into a new image
rotated_image.putdata(new_image_data)
rotated_image.show()

# save an image
image1.save("nombre_de_imagen.jpg")

# change a pixel color 
image1.putpixel((x,y), (r,g,b,a))

# is much faster than getPixel, putPixel
pixel_access_object = image1.load()
pixel_access_object [x,y] = (0,0,0,255)

# returns tuple of the image bands
r,g,b,a = image1.split()
# it merges the 3 bands and save it into the image
image1 = Image1.merge("RGB",(r,g,b))

# prints the mode of the image
print(image1.mode)



# delete variables to manage the memory 
del image1,image2,rotated_image