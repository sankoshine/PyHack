from PIL import Image, ImageFont, ImageDraw
image = Image.open("b.jpg")
draw = ImageDraw.Draw(image)
x, y = image.size
font = ImageFont.truetype("mononoki.ttf", x//3)
draw.text((x/2, 0), "SA", font=font, fill="red")
image.show()
image.save("n.jpg")