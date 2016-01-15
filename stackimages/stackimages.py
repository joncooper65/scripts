from PIL import ImageChops
import Image
import glob

files = glob.glob("./img*.jpg")
finalimage = Image.open(files[0])
for i in range(1,len(files)):
    currentimage=Image.open("./"+files[i])
    finalimage=ImageChops.lighter(finalimage, currentimage)
finalimage.save("output.jpg","JPEG")
