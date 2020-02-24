from PIL import Image

img = Image.new('RGB', (640, 360),(255, 255, 255))
pixels=img.load()

for i in range(300):
	im = Image.open('nsW38Dh7Qx'+str(i)+'.jpg')
	pix = im.load()
	for p in range(640):
		for q in range(360):
			pixel_value=pix[p,q]
			if(pixel_value>249 and pixel_value<=256):
				pixels[p,q]=0
	im.close()

img.save('answer.jpg')
