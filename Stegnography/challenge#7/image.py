from PIL import Image

# https://www.bertnase.de/npiet/npiet-execute.php
# to compile the image just go there ^^^^

# (255,192,192)
# (255,255,192)
# (192,255,192)
# (192,255,255) 
# (255,192,255) 
# (255,0,0)
# (255,255,0) 
# (0,255,0) 
# (0,255,255)
# (0,0,255) 
# (192,0,192) 
# (0,0,0)
# (255,255,255)

#list of colors that piet can interpretate
list_of_color = [(255,192,192),(255,255,192),(192,255,192),(192,255,255), (255,192,255) ,(255,0,0),
(255,255,0),(0,255,0),(0,255,255),(0,0,255),(192,0,192),(0,0,0),(255,255,255)]

#list of colors found in the png that is not in the piet vocabulary
list_of_color_not_in_languaje = []

#opens the image
image1 = Image.open('not_art.png')

size = width,height = image1.size

print(list(image1.getdata())[0])
#loops the image and saves the colors that are not in the piet vocabulary
for color in list(image1.getdata()):
	# if it is, dont save it, if it is already in the blacklist, dont save it again
	if color in list_of_color or color in list_of_color_not_in_languaje:
		continue
	else:
		list_of_color_not_in_languaje.insert(0,color)

#this is the new image
new_image = image1
#this is the data of the new image
new_image_data = []

#it loops for the color in the png again...
for color in list(image1.getdata()):
	# if the color is in the black list, then set it to black
	if(color in list_of_color_not_in_languaje):
		new_image_data += [(0,0,0)]
	# if not, then save it
	else:
		new_image_data += [color]

# insert the pixels data into the new image
new_image.putdata(new_image_data)
# show the image
new_image.show()
#finaly save it
new_image.save('new1.png')

#print (list_of_color_not_in_languaje)(0,0,0))
#print(new_image_data)

new_new_image_data = []
new_new_image = Image.new ("RGB", size)


for color in new_image_data:
	if color == (0,0,0):
		continue
	else:
		new_new_image_data += [color]
		print ('#%02x%02x%02x' % color)

new_new_image.putdata(new_new_image_data)
new_new_image.show()