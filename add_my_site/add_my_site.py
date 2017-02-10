from PIL import Image, ImageDraw, ImageFont

def add_my_site(img):
	draw = ImageDraw.Draw(img)
	width, height = img.size 
	myfont = ImageFont.truetype('/System/Library/Fonts/Helvetica.dfont', size = 150)
	fillcolor = '#FFFFFF'
	draw.text((width * 0.55, height * 0.9375), 'https://ipreacher.github.io/', font = myfont, fill = fillcolor)
	img.save('result.jpg', 'jpeg')
	return 0

if __name__ == '__main__':
	image = Image.open('/Users/wonderful/Desktop/test.JPG')
	add_my_site(image)