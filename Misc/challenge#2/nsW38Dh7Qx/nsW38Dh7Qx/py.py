from PIL import Image
from PIL import ImageFilter

new_image_data = Image.new('L', (640, 360),(0))
data = list(new_image_data.getdata())
new_image_data.show()


for i in range(0,300):
	im = Image.open('nsW38Dh7Qx'+str(i)+'.jpg')
	images_data = im.getdata()
	for color in range(0,len(list(im.getdata()))):
		print(images_data[color])
		data[color] = data[color] + images_data[color]

new_image_data.putdata(data)
new_image_data.show()
#image1 = Image.open('image_name.extension')