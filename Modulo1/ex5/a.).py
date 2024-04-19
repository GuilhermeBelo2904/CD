import os
from PIL import Image
import random
import sys
sys.path.insert(1, os.path.join(os.getcwd(), "Modulo1"))
from Utils import get_test_file_names

class Rectangle:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def isEmpty(self):
        return self.width == 0 or self.height == 0    
    
    
def create_key(width, height):
     return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(width * height)]

def isInAreaToEncrypt(pixel, rectangle):
    return rectangle.x <= pixel % rectangle.width < rectangle.x + rectangle.width and rectangle.y <= pixel // rectangle.width < rectangle.y + rectangle.height
    
def vernam_cipher(pixels, pre_shared_key, rectangle=Rectangle()):
    if len(pixels) != len(pre_shared_key):
        print("Error: The number of pixels" + "(" + str(len(pixels)) + ")" + " and the number of keys" + "(" + str(len(pre_shared_key)) + ")" + " are different.")
        return []
    
    encrypted_pixels = []

    if rectangle.isEmpty():
        for i in range(len(pixels)):
            pixel_img = pixels[i]
            pixel_key = pre_shared_key[i]
            
            encrypted_pixel = (pixel_img[0] ^ pixel_key[0], pixel_img[1] ^ pixel_key[1], pixel_img[2] ^ pixel_key[2])
            encrypted_pixels.append(encrypted_pixel)    
    else:
        for i in range(len(pixels)):
            if isInAreaToEncrypt(i, rectangle):
                pixel_img = pixels[i]
                pixel_key = pre_shared_key[i]
                
                encrypted_pixel = (pixel_img[0] ^ pixel_key[0], pixel_img[1] ^ pixel_key[1], pixel_img[2] ^ pixel_key[2])
                encrypted_pixels.append(encrypted_pixel)
            else:
                encrypted_pixels.append(pixels[i])
                            
    return encrypted_pixels

def Vernam_Cipher_Menu(current_directory):
    while True:
        print("\nGrayscale Images or Color Images?")
        print("1 - Grayscale Images")
        print("2 - Color Images")
        print("E - Exit")
        
        option = input("Option: ")
        
        if option.upper() == 'E':
            print("\n\nExiting...\n")
            break
        elif not option.isdigit() or int(option) < 1 or int(option) > 2:
            print("\nInvalid option. Please choose a valid number.")
            continue 
        else:
            option = int(option)
            if option == 1:
                relative_path = os.path.join("Modulo1", "ex5", "Grayscale Images")
            elif option == 2:
                relative_path = os.path.join("Modulo1", "ex5", "Color Images")
                
            path = os.path.join(current_directory, relative_path)
            file_names = get_test_file_names(path)
            Vernam_Cipher_App(file_names, relative_path)
            
            
def Vernam_Cipher_App(file_names, relative_path):
    while True:
        print("\nChoose a file to encrypt or press 'E' to exit:")
        for i, file_name in enumerate(file_names):
            print(f"{i} - {file_name}")
        
        option = input("Option: ")
        if option.upper() == 'E':
            print("\n\nExiting...\n")
            break
        elif not option.isdigit() or int(option) < 0 and int(option) >= len(file_names):
            print("\nInvalid option. Please choose a valid number.")
            continue 
        else:
            option = int(option)
            f = os.path.join(relative_path, file_names[option])
            
            original_image = Image.open(f)
            original_image = original_image.convert("RGB")
            original_image.show()
            original_pixels = list(original_image.getdata())
            
            while True:
                print("\nDo you want to encrypt the whole image or a specific area?")
                print("1 - Whole Image")
                print("2 - Specific Area")
                
                option = input("Option: ")
                if option == '1':
                    areaToEncrypt = Rectangle()
                    break
                elif option == '2':
                    print("\nImage " + file_name + " has width " + str(original_image.width) + " and height " + str(original_image.height) + ".")
                    print("Please provide the coordinates and dimensions of the area to encrypt: ")
                    x = int(input("X: "))
                    if x < 0 or x >= original_image.width:
                        print("\nInvalid X value. Image width: " + str(original_image.width) + ". Please choose a valid number.")
                        continue
                    y = int(input("Y: "))
                    if y < 0 or y >= original_image.height:
                        print("\nInvalid Y value. Image height: " + str(original_image.height) + ". Please choose a valid number.")
                        continue
                    width = int(input("Width: "))
                    if width <= 0 or width > original_image.width - x:
                        print("\nInvalid width value. Image width: " + str(original_image.width) + ". Please choose a valid number.")
                        continue
                    height = int(input("Height: "))
                    if height <= 0 or height > original_image.height - y:
                        print("\nInvalid height value. Image height: " + str(original_image.height) + ". Please choose a valid number.")
                        continue
                    
                    areaToEncrypt = Rectangle(x, y, width, height)
                    break
                else:
                    print("\nInvalid option. Please choose a valid number.")
                    continue
                
            print("Encrypting the image...")
            pre_shared_key = create_key(original_image.width, original_image.height)
            encrypted_pixels = vernam_cipher(original_pixels, pre_shared_key, areaToEncrypt)

            encrypted_image = Image.new(original_image.mode, original_image.size)
            encrypted_image.putdata(encrypted_pixels)
            encrypted_image.show()
            
            while True: 
                print("\nDo you want to decrypt the image?")
                print("1 - Yes")
                print("2 - No")
                
                option = input("Option: ")
                if option == '1':
                    print("Decrypting the image...")
                    decrypted_pixels = vernam_cipher(encrypted_pixels, pre_shared_key, areaToEncrypt)
                    
                    decrypted_image = Image.new(original_image.mode, original_image.size)
                    decrypted_image.putdata(decrypted_pixels)
                    decrypted_image.show()
                    break
                elif option == '2':
                    break
                else:
                    print("\nInvalid option. Please choose a valid number.")
                    continue
                                  
    
# ------------------------Test------------------------

# Get the current directory
current_directory = os.getcwd()
Vernam_Cipher_Menu(current_directory)