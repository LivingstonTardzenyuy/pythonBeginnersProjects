#resizing image

#we are going to use pillow so install

#import pillow

#open image we want to resize using python

#print the current size of the image

#specify the size we wanna chagne it to

#save the new resize image

from PIL import Image       #PIL means pillow and we want to take only image

def resize_image(size_one, size_two):
    # image_name=input("Enter your image with it extension: ")
    image=Image.open(r'one.jpg')

    print(f"Current size: {image.size}")




    resized_image=image.resize((size_one,size_two))
    resized_image.save('Livingston.jpeg')

size_one=int(input("Enter the x coordinate"))
size_tow=int(input("Enter the y coordinate"))
resize_image(size_one, size_tow)