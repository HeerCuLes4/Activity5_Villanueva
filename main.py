import cv2 as cv
import numpy as np

img =cv.imread("book.jpeg")

if(len(img.shape)<2):
    print ('\nImage type: Grayscale image')
    exit()
elif len(img.shape)==3:
    print('\nImage type: Colored Image')


maxheight = 1920
maxwidth = 1080
minheight = 480
minwidth = 360
size = 1500000

print ("\nImage dimension limit: max = 1920 x 1080 and min = 480x 360")
imgheight = img.shape[0]
imgwidth = img.shape[1]

print("Current loaded image dimension:",imgheight,"x",imgwidth)
if((imgheight <=maxheight and imgheight >=minheight)and (imgwidth <= maxwidth and imgwidth >= minwidth)):
    print("Current loaded image  is within the bounderies!")
else:
    print("Current loaded image is not  in the bounderies!")

print("\nSet size:",size)
imgsize = img.size
print("Current loaded image size:",imgsize)
if (imgsize < size):
    print("Current loaded image has lower pixel count than the set image size!")
else:
    print("Current loaded image has higher pixel count than the set image size!")



print("\Current loaded image datatype:", img.dtype)


print("\nAccess a pixel value using item method")
a,b,c = input("Enter row, column and channel: ").split()
row1,column1,channel1 = [int(a),int(b), int(c)]
res = img.item(row1,column1,channel1)
print("Result:", res)


print("\nModify a pixel value using itemset method")
x,y = input("Enter row and column: ").split()
blue = int(input("Enter changes in blue channel: "))
green = int(input("Enter changes in green channel: "))
red = int (input("Enter changes in red channel: "))
print("\nResult")
row2,column2 = [int(x), int(y)]
img.item(row2,column2,0)
img.item(row2,column2,1)
img.item(row2,column2,2)
res1 = img[row2,column2]
print("Before: ", res1)
img.itemset((row2,column2,0), blue)
img.itemset((row2,column2,1), green)
img.itemset((row2,column2,2), red)
res2 = img[row2,column2]
print("After:",res2,"\n")
