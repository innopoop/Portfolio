from PIL import Image, ImageFilter
from random import *

# RGB values for recoloring.
darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)



image = input("What image file do you want filtered?\n")
pic_filter = input("What type of filter do you want? (recolor, blur)\n")
# Import image.
my_image = Image.open(image) #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
def blur():
    blur_img = my_image.filter(ImageFilter.GaussianBlur(5))
    blur_img.show()
    blur_img.save("blurred.jpg","jpeg")
def recolor(color1,color2,color3,color4):
    image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
    image_list = list(image_list)
    for pixel in image_list:
        intensity = sum(pixel)
        if intensity < 182:
            recolored.append(color1)
        elif intensity in range(182,364):
            recolored.append(color2)
        elif intensity in range(364,546):
            recolored.append(color3)
        elif intensity >= 546:
            recolored.append(color4)

def display(name):
    new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
    new_image.putdata(recolored) #Adds the data from the recolored list to the image.
    new_image.show() #show the new image on the screen
    new_image.save( name, "jpeg") #save the new image as "recolored.jpg"
def please():
    rgb_list = []
    for i in range(4):
        x = randrange(255)
        y = randrange(255)
        z = randrange(255)
        rgb = (x,y,z)
        rgb_list.append(rgb)
    recolor(rgb_list[0],rgb_list[1],rgb_list[2],rgb_list[3])

if pic_filter.lower() == "recolor":
    color = input("What mode of recolor do you want? (obamicon or random)\n")
    if color.lower() == "obamicon":
        recolor(darkBlue,red,lightBlue,yellow)
        display("recolored.jpg")
    elif color.lower() == "random":
        please()
        display("randRecolored.jpg")
elif pic_filter.lower() == "blur":
    blur()


"""
for pixel in image_list:
    intensity = sum(pixel)
    if intensity < 182:
        recolored.append(darkBlue)
    elif intensity >= 182 and intensity < 364:
        recolored.append(red)
    elif intensity >= 364 and intensity < 546:
        recolored.append(lightBlue)
    elif intensity >= 546:
        recolored.append(yellow)

"""
