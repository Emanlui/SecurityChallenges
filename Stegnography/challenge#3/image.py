from PIL import Image

image1 = Image.open('bluepane0.bmp')
image2 = Image.open('bluepane1.bmp')
image3 = Image.open('bluepane2.bmp')
image4 = Image.open('solved.bmp')

size = width,height = image1.size

new = Image.new('RGB', size)

img1 = image1.load()
img2 = image2.load()
img3 = image3.load()
img4 = image4.load()

data = new.load()

for x in range(width):
	for y in range(height):
			one = img1[x,y]
			two = img2[x,y]
			three = img3[x,y]
			fourth = img4[x,y]

			new_color = (three[0] or fourth[0],three[1] or fourth[1],three[2] or fourth[2])

			data[x,y] = new_color


new.save('new.jpg')
new.show() 