from PIL import ImageChops
import Image
import glob
import numpy as np

def maxStack():
	#Use this for pulling out the max value of a pixel across images
	files = glob.glob("./img*.jpg")
	finalimage = Image.open(files[0])
	for i in range(1,len(files)):
		  currentimage=Image.open("./"+files[i])
		  finalimage=ImageChops.lighter(finalimage, currentimage)
	filename = "stackmax.jpg"
	finalimage.save(filename,"JPEG")
	return filename

doOne = True
if doOne:
	#For fun get the max across all images in the folder
	filename = maxStack()
	#Enhance a single image
	temp = np.asarray(Image.open(filename))
	temp = temp.astype('uint32')

	#Remove r, g or b values that are below a threshold perhaps?
#	temp[temp<5]=0

	#Amplify any r, g or b values that aren't zero
	temp = temp * 10

	#Trim r, g or b values to 255 since that's the max value allowed when we convert to data type uint8
	temp[temp>255]=255

	#Show it
	tempImg = Image.fromarray(temp.astype('uint8'))
	tempImg.show()
	tempImg.save("stretched.jpg","JPEG")
else:
	#Stack a set of images
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

