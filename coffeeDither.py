#!/usr/bin/env python

# coffeeDither Rev 2
# Created by Akeeal Mohammed
# August 9th 2020
# License: GPLv3
# ------------
#| Change Log |
# ------------
# Rel 1: Initial release
import math
import string

from gimpfu import *
from array import array

def coffeeDither(image, layer):
	    
	pdb.gimp_image_undo_group_start(image)
	pdb.gimp_context_push()
	
	#####Create Overlay layers
	#visible_layer = pdb.gimp_layer_new_from_visible(image, image, "Middle Layer")

	#pdb.gimp_image_insert_layer(image, visible_layer, None, 0)
	#pdb.gimp_layer_set_mode(visible_layer,LAYER_MODE_OVERLAY)
	#pdb.gimp_desaturate_full(visible_layer, DESATURATE_LIGHTNESS) #Desaturate -> Desaturate -> mode Lightness HSL
	#pdb.gimp_drawable_invert(visible_layer, TRUE) #Invert image
	#pdb.plug_in_gauss(image, visible_layer, 50.0, 50.0, 1)#Filters -> Blur -> Gaussian Blur -> Blur Radius 50% RLE
	
	visible_layer1 = pdb.gimp_layer_new_from_visible(image, image, "Top Layer")
	pdb.gimp_image_insert_layer(image, visible_layer1, None, 0)
	pdb.gimp_layer_set_mode(visible_layer1,LAYER_MODE_OVERLAY)

	pdb.plug_in_unsharp_mask(image, visible_layer1, 0.671, 38.074, 0.063)#Sharpen(Unsharpen Mask) - Radius 3.000/ Amount 10.000 / Threshold 0.002
	
	pdb.gimp_image_convert_grayscale(image)#Greyscale
	pass
	
	#pdb.plug_in_photocopy(image, visible_layer1, 21.000, 1.000, 0.200, 0.500)#Photocopy - Mask Radius 3.000/ Sharpness 1.000 / PercentBlack 0.200/PercentWhite 0.500
	
	pdb.gimp_brightness_contrast(visible_layer1, 127, -75)
	#(-127 <= brightness andn contrast <= 127)
	
	pdb.plug_in_newsprint(image, visible_layer1, 4.5, 0, 100, 45, 0, 45, 0, 45, 0, 45, 0, 128)
	#(image, drawable, cell_width((0 <= cell-width <= 1500)), 
	#colorspace Separate to { GRAYSCALE (0), RGB (1), CMYK (2), LUMINANCE (3) } (0 <= colorspace <= 3), 
	#k_pullout, Percentage of black to pullout (CMYK only) (0 <= k-pullout <= 100)
	#gry_ang, 
	#gry_spotfnGrey/black spot function { DOTS (0), LINES (1), DIAMONDS (2), EUCLIDIAN-DOT aka Checkard(3), PS-DIAMONDS (4) } (0 <= gry-spotfn <= 4)
	#, red_ang, red_spotfn, grn_ang, grn_spotfn, blu_ang, blu_spotfn, 
	#oversample)how many times to oversample spot fn (0 <= oversample <= 128)
	

	pdb.gimp_image_flatten(image)#Flatten Image
	
	
 	pdb.gimp_context_pop()
	pdb.gimp_image_undo_group_end(image)
	pdb.gimp_displays_flush()
	
	
    #return
    
    
register(
	"coffeeDither",
	"Coffee Dither",
	"Make it easy Coffee Dither",
	"Akeeal Mohammed",
	"Akeeal Mohammed",
	"2020",
	"<Image>/READY PICTURE/STEP 2 = Effects for Laser/Coffee Dither",
	"*", # *=Any image can be worked on
    [    #The list below is the GUI 
        #(PF_INT, "number", "Number?", 50),
        #(PF_FLOAT, "angle", "Angle", 3.14159),
        # you can also use PF_INT8, PF_INT16, PF_INT32
        #(PF_STRING, "word", "Word", "Zebrafish!"),
        # PF_VALUE is another term for PF_STRING
        #(PF_TEXT, "text", "Some Text",
        #  "The quick red fox jumped over the lazy dog"),

        #(PF_COLOR, "bg-color", "Background", (1.0, 1.0, 1.0)),
        # or you can spell it PF_COLOUR

        #(PF_IMAGE, "image", "Input image", None),
        #(PF_LAYER, "layer", "Input layer", None),
        
        #(PF_CHANNEL, "channel", "Which channel", None),
        #(PF_DRAWABLE, "drawable", "Input drawable", None),

        #(PF_TOGGLE, "shadow", "Shadow?", 1),
        #(PF_BOOL,   "ascending", "_Ascending", True),
        #(PF_RADIO, "str", "Material Type", "jpg",
        #(("Script 1", "script1"), ("Script 2", "script2"), ("Script 3","script3"), 
        #("Script 4","script4"), ("Script 5","script5"), ("Script 6","script6"))),
        #(PF_OPTION, "option", "Option", 2, ("Mouse", "Cat", "Dog", "Horse")),

        #(PF_SPINNER, "size", "Pixel Size", 50, (1, 8000, 1)),
        #(PF_SLIDER, "opacity",  "Op_acity", 100, (0, 100, 1)),
        # (PF_ADJUSTMENT is the same as PF_SPINNER

        #(PF_FILE, "imagefile", "Image file", ""),
        #(PF_DIRNAME, "dir", "Directory", "/tmp"),

        #(PF_FONT, "font", "Font", "Sans"),
        #(PF_BRUSH, "brush", "Brush", None),
        #(PF_PATTERN, "pattern", "Pattern", None),
        #(PF_GRADIENT, "gradient", "Gradient", None),
        #(PF_PALETTE, "palette",  "Palette", ""),

        # New items that don't quite work yet:
        #(PF_VECTORS, "vectors", "Vectors", None),
        #(PF_DISPLAY, "display", "Display", None),
    ],
    [],
   
	coffeeDither)

main()
