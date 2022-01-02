from PIL import Image, ImageFont, ImageDraw

### VAIRABLES #################################################################
theme_color = (235,235,235)
title_copy = """
THE ART OF WORLDLY WISDOM
"""
author_copy = """
BALTASAR GRACIAN
"""

spine_copy = "THE ART OF WORLDY WISDOM     BALTASAR GRACIAN"

copyright_text = """COPYRIGHT 2022. 
ALL RIGHTS RESERVED. 
FKM BOOKS"""
back_copy = """
The Art of Worldly Wisdom, in Spanish Oráculo Manual 
y Arte de Prudencia, was written in 1647 by Baltasar 
Gracián y Morales, better known as Baltasar Gracian. 
It's a collection of 300 maxims on various topics, each 
with a commentary, provide advice and guidance on 
how to live fully, advance socially, and be a better 
person in the world.

"""

FRONT_font1 = ImageFont.truetype('Montserrat-Bold.otf',size=100) # can also use Arial
FRONT_font2 = ImageFont.truetype('Montserrat-Medium.otf',size=100) # can also use Arial
FRONT_font3 = ImageFont.truetype('Montserrat-Bold.otf',size=70) # can also use Arial
sidefont = ImageFont.truetype('Montserrat-Bold.otf',size=70)
sidefont_lower = ImageFont.truetype('Montserrat-Bold.otf',size=50)
BACK_font = ImageFont.truetype('Montserrat-Medium.otf',size=55)
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
y_start = 550
text = img_draw.text((dpi_total_width/2+dpi_spine_width/2+70, y_start), title_copy, font=FRONT_font1, fill='black')
text = img_draw.text((dpi_total_width/2+dpi_spine_width/2+70, y_start+110), author_copy, font=FRONT_font2, fill='black')
text = img_draw.text((dpi_total_width-550, 80), "a fkm classic", font=FRONT_font3, fill='black')


# image
img = Image.open("output.png")
img = img.resize((int(dpi_total_width/2-dpi_spine_width/2), int(dpi_total_width/2-dpi_spine_width/2)))
blank_image.paste(img,(int(dpi_total_width/2+dpi_spine_width/2),dpi_total_height - int(dpi_total_width/2-dpi_spine_width/2)))


# Back cover text
img_draw.multiline_text((150, 1000), back_copy, font=BACK_font, fill='black', spacing=16)
img_draw.multiline_text((150, 2550), copyright_text, font=CRfont, fill='black', spacing=16)


# create spine text
f = ImageFont.load_default()
txt = Image.new('RGBA', (3300, 72))  # dimensions of layer for sideways text
d = ImageDraw.Draw(txt)
d.text((0, 0), spine_copy, font=sidefont, fill=(0,0,0,255))
w_left = txt.rotate(90, expand=1)  # expand: expands the output to be large enough to hold the rotated image
w_right = txt.rotate(-90, expand=1)
blank_image.paste(w_right, (1864, 160), w_right)

f = ImageFont.load_default()
txt = Image.new('RGBA', (3300, 72))  # dimensions of layer for sideways text
d = ImageDraw.Draw(txt)
d.text((0, 0), "FKM BOOKS", font=sidefont_lower, fill=(0,0,0,255))
w_left = txt.rotate(90, expand=1)  # expand: expands the output to be large enough to hold the rotated image
w_right = txt.rotate(-90, expand=1)
blank_image.paste(w_right, (1855, 2350), w_right)

# save image
blank_image.save('Book_Jacket.jpg')

