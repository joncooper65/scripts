from PIL import ImageChops
import Image
import glob
import numpy as np

#Use this for pulling out the max value of a pixel across images
#It will produce star trails from night timelapse frames
def maxStack():
	files = glob.glob("./img*.jpg")
	finalimage = Image.open(files[0])
	for i in range(1,len(files)):
		  currentimage=Image.open("./"+files[i])
		  finalimage=ImageChops.lighter(finalimage, currentimage)
	filename = "stackmax.jpg"
	finalimage.save(filename,"JPEG")
	return filename


#Get the max across all images in the folder and multiply to enhance
def stackMaxAndStretch():
	filename = maxStack()
	#Enhance a single image
	temp = np.asarray(Image.open(filename))
	temp = temp.astype('uint32')

	#Remove r, g or b values that are below a threshold perhaps?
#	temp[temp<5]=0

	#Amplify (stretch) any r, g or b values that aren't zero
	temp = temp * 10

	#Trim r, g or b values to 255 since that's the max value allowed when we convert to data type uint8
	temp[temp>255]=255

	#Show it
	tempImg = Image.fromarray(temp.astype('uint8'))
	tempImg.show()
	tempImg.save("stretched.jpg","JPEG")

#Add a set of images together
def stackAdd():
	images = glob.glob("./img*.jpg")
	first = True
	for img in images:
		temp = np.asarray(Image.open(img))
		temp = temp.astype('uint32')
		if first:
			result = temp
			first = False	
		else:
			result = result + temp
	resultImg = Image.fromarray(result.astype('uint8'))
	resultImg.show()

#Use this for pulling out the max value of a pixel across images, and save an image with each iteration
#This can be used to animate a star trail
def maxStackCollectAll():
	files = glob.glob("././IMG*.*.JPG")
	files.sort()
	finalimage = Image.open(files[0])
	for i in range(0,len(files)):
		print str(i) + " of " + str(len(files))
		currentimage=Image.open("./"+files[i])
		finalimage=ImageChops.lighter(finalimage, currentimage)
		filename = "stackmax" + str(i).zfill(3) +".jpg"
		finalimage.save(filename,"JPEG")

maxStackCollectAll()

