from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageEnhance

### VAIRABLES #################################################################
theme_color = ('black')
text_copy = """
THE ART OF 
WORLDLY WISDOM 

Baltasar Gracian"""

spine_copy = "THE ART OF WORLDLY WISDOM - Baltasar Gracian"

copyright_text = """COPYRIGHT 2021. 
ALL RIGHTS RESERVED. 
KEMPTONMOONEY.COM"""
back_copy = """


"""

FRONT_font = ImageFont.truetype('Montserrat-ExtraBold.otf',size=140) # can also use Arial
sidefont = ImageFont.truetype('Montserrat-ExtraBold.otf',size=70)
BACK_font = ImageFont.truetype('Montserrat-Bold.otf',size=55)
CRfont = ImageFont.truetype('Montserrat-Bold.otf',size=40)

pages = 150
letters_per_line = 7
############## CALCS #############################################################################
resolution = 300
height = 9
width = 6
edge_bleed = .125
spine_margins = .065
margin_per_page = .0025

spine_width = margin_per_page * pages
total_height = height + (2 * edge_bleed)
total_width = (2 * width) + spine_width + (2 * edge_bleed)
print(spine_width)
print(total_height)
print(total_width)

dpi_total_height = int(total_height * resolution)
dpi_total_width = int(total_width * resolution)
dpi_spine_width = int(spine_width * resolution)

############## GENERATOR #############################################################################
blank_image = Image.new('RGB', (dpi_total_width, dpi_total_height), theme_color) # first numbers are coordinates, second are RBG color
img_draw = ImageDraw.Draw(blank_image)

# guideline
#img_draw.line((dpi_total_width/2, 0, dpi_total_width/2, dpi_total_height), width=1, fill='blue')
#img_draw.line((dpi_total_width/2-dpi_spine_width/2, 0, dpi_total_width/2-dpi_spine_width/2, dpi_total_height), width=1, fill='blue')
#img_draw.line((dpi_total_width/2+dpi_spine_width/2, 0, dpi_total_width/2+dpi_spine_width/2, dpi_total_height), width=1, fill='blue')

# Front cover text
text = img_draw.text((dpi_total_width/2+dpi_spine_width/2+138, 150), text_copy, font=FRONT_font, fill='white')

# image
img = Image.open("design.png")
img = img.resize((int(dpi_total_width/2-dpi_spine_width), int(dpi_total_width/2-dpi_spine_width)))
blank_image.paste(img,(2005,dpi_total_height - int(dpi_total_width/2-dpi_spine_width)))

blank_image.paste(img,(0,0))

# Back cover list
img_draw.multiline_text((150, 100), back_copy, font=BACK_font, fill='white', spacing=16)
img_draw.multiline_text((150, 2550), copyright_text, font=CRfont, fill='white', spacing=16)


# create spine text
f = ImageFont.load_default()
txt = Image.new('L', (3300, 72))  # dimensions of layer for sideways text
d = ImageDraw.Draw(txt)
d.text((0, 0), spine_copy, font=sidefont, fill='white')
w_left = txt.rotate(90, expand=1) # expand: expands the output to be large enough to hold the rotated image
w_right = txt.rotate(-90, expand=1)
blank_image.paste(w_right, (1864, 225), w_right)

f = ImageFont.load_default()
txt = Image.new('L', (3300, 72))  # dimensions of layer for sideways text
d = ImageDraw.Draw(txt)
d.text((0, 0), "FKM BOOKS", font=sidefont, fill='white')
w_left = txt.rotate(90, expand=1)  # expand: expands the output to be large enough to hold the rotated image
w_right = txt.rotate(-90, expand=1)
blank_image.paste(w_right, (1864, 2250), w_right)

# save image
blank_image.save('Book_Jacket.jpg')

