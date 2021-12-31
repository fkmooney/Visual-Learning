# chunking done mostly manually on front cover
from PIL import Image, ImageFont, ImageDraw

### VAIRABLES #################################################################
theme_color = ('black')
text_copy = """THE ART OF CONVERSATION BY MELVIN ALLFORMY"""
copyright_text = """COPYRIGHT 2019. 
ALL RIGHTS RESERVED. 
KEMPTONMOONEY.COM"""
back_copy = """
In his second book, The Art of Conversation, 
bestselling author and evil cartographer Melvin 
Allformy provides an easy to follow guide to 
help you improve your personal people skill 
through his patented process. This is also the 
book he used to try and overthrow the United 
States government in March 4th, 2013, commonly 
referred to as the attempted Coup of Modern and 
Contemporary Art in America (and Sculpture Gard-
en). This second edition includes a new foreword 
and epilogue by the publisher to provide context 
to the historic events of March 4th as well as 
Allformy’s original text so that future scholars 
and historians will be able to understand what 
drives this strange, deluded, megalomaniacal 
twit of a man and to ensure that there is never 
another Coup of Modern and Contemporary Art in 
America (and Sculpture Garden).

“This guy is a complete lunatic.”  
             - Confidential FBI Informant

“One of the best evil cartographers I’ve 
ever worked with.” 
             - Ludwig Wickedstein

“A real mensch.” 
             - Leonard Kravitz

“That @sshat still owes me money.” 
             - Anonymous Henchman

"""

FRONT_font = ImageFont.truetype('C:\Windows\Fonts\VeraMono-Bold.ttf',size=370) # can also use Arial
sidefont = ImageFont.truetype('C:\Windows\Fonts\LiberationMono-Bold.ttf',size=62)
BACK_font = ImageFont.truetype('C:\Windows\Fonts\LiberationMono-Bold.ttf',size=55)
CRfont = ImageFont.truetype('C:\Windows\Fonts\LiberationMono-Bold.ttf',size=40)

pages = 150
letters_per_line = 6
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

#text chunker
text_no_space = text_copy.replace(" ","") # use to elim spaces from cover
#text_no_space = text_copy # use if want spaces
title_len = len(text_no_space)
chunks = [text_no_space[i:i+letters_per_line] for i in range(0, len(text_no_space), letters_per_line)]
chunked = ('\n'.join(chunks))

############## GENERATOR #############################################################################
blank_image = Image.new('RGB', (dpi_total_width, dpi_total_height), theme_color) # first numbers are coordinates, second are RBG color
img_draw = ImageDraw.Draw(blank_image)

# guideline
img_draw.line((dpi_total_width/2, 0, dpi_total_width/2, dpi_total_height), width=1, fill='blue')
img_draw.line((dpi_total_width/2-dpi_spine_width/2, 0, dpi_total_width/2-dpi_spine_width/2, dpi_total_height), width=1, fill='blue')
img_draw.line((dpi_total_width/2+dpi_spine_width/2, 0, dpi_total_width/2+dpi_spine_width/2, dpi_total_height), width=1, fill='blue')

# Front cover text
text = img_draw.text((dpi_total_width/2+dpi_spine_width/2+220, 350), chunked, font=FRONT_font, fill='white')

# Back cover list
img_draw.multiline_text((150, 100), back_copy, font=BACK_font, fill='white', spacing=16)
img_draw.multiline_text((150, 2550), copyright_text, font=CRfont, fill='white', spacing=16)


# create spine text
f = ImageFont.load_default()
txt = Image.new('L', (3300, 50)) # dimensions of layer for sideways text
d = ImageDraw.Draw(txt)
d.text((0, 0), text_copy, font=sidefont, fill='white')
w_left = txt.rotate(90,  expand=1) # expand: expands the output to be large enough to hold the rotated image
w_right = txt.rotate(-90,  expand=1)
blank_image.paste(w_right, (1870, 530), w_right)

######## NEED ICON ON SPINE

# save image
blank_image.save('Book_Jacket_no_pic.jpg')

