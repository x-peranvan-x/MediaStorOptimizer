import os
import cv2
import glob
from skimage.metrics import structural_similarity as ssim
import shutil
#import argparse
#import inquirer
#import pytermgui
import pyfiglet
f = pyfiglet.figlet_format('MediaStorOptimizer',width=110)
print(f)
#Global Variables
IMAGE_FILES=[".jpeg",".jpg",".gif",".png",".tga"]
COMPARISONS=[]

'''
To-Do
---------
- Look into doing the glob work using shutil or os; that way you don't need to import it
- Make this to an interactive CLI
    Let the user choose which directory they want to be in, based off current directory 
    Let people choose the directories that they want to use
- Add video editing, to crop out sections
- Optimize the image reading line (CTRL-F READ IMAGES) 
- Try to make the image similarity process asynchronous, so that multiple images can be procesed at once
    You need to figure out how to pick which images will be used for this
        I guess from the first image comparison, if it's not within a valid threshold then they are not the same and so the image it compare itself to can be used for comparisons with other images
        MAX 5 processes
- Add code to make/move the similar images to a different folder
    Maybe at the end of the entire image comparison process, the user can individually go through each similar image or it can just keep the first image that was the same


'''
def resize_images(imageA, imageB):
    # Get the dimensions of the images
    heightA, widthA = imageA.shape
    heightB, widthB = imageB.shape
    # Determine the new dimensions
    new_height = min(heightA, heightB)
    new_width = min(widthA, widthB)
    # Resize the images to the new dimensions
    resized_imageA = cv2.resize(imageA, (new_width, new_height))
    resized_imageB = cv2.resize(imageB, (new_width, new_height))
    return resized_imageA, resized_imageB


def calculate_ssim(imageA, imageB):
    # Compute the Structural Similarity Index (SSIM) between the two images
    score, _ = ssim(imageA, imageB, full=True)
    return score

def compareImage(img1,img2):
    image1 = cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
    #resize image
    image1, image2 = resize_images(image1, image2)
    # Compute the SSIM
    similarity = calculate_ssim(image1, image2)
    print(f"({img2}) Similarity (SSIM): {similarity}")
    return similarity


def main():
    print("Successfully Imported All Libraries")
    print("Reading Files in ",os.getcwd())
    print("Collecting all images in current directory\n")

    #READ IMAGES
    images = []
    for i in IMAGE_FILES:
        readImgs=glob.glob(f"*{i}")
        for g in readImgs:
            print(g)
            images.append(g)

    #Compare Images
    threshold=float(input("Enter the threshold for Image Similarity: "))
    print("\nComparing 2 images")
    for i in images[:-1]:
        simImages=[]
        print(i)
        print("----------------")
        for j in images[images.index(i)+1::]:
            sim_Value=compareImage(i,j)
            if sim_Value>threshold:
                if len(simImages)==0:
                    simImages.append(i)
                    images.remove(i)

                simImages.append(j)
        print()
        if not(not simImages):
            COMPARISONS.append(tuple(simImages))
    del images
    for i in COMPARISONS:
        #Make this better later; I don't want to name each folder
        name=input("Enter Folder name")
        os.mkdir(f"{name}")
        for j in i:
            try:
                shutil.move(j,name)
            except:
                print("Unexpected Error")
                break
        print("Successfully Moved the Files")
        
main()