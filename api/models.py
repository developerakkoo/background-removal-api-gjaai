import sys
from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import os
from pathlib import Path

from rembg import remove
import cv2
import numpy as np



# Create your models here.
class uploadimage(models.Model):
    title=models.CharField(max_length=50)
    height=models.CharField(max_length=500),
    width=models.CharField(max_length=500),
    images=models.ImageField('images/')

    def save(self, *args, **kwargs):
        BASE_DIR = Path(__file__).resolve().parent.parent

        MEDIA_ROOT = os.path.join(BASE_DIR,'images')

        # print(self.images)
        # print(path)
        im = Image.open(self.images)
        path = os.path.join(r"./images",str(self.images))
        # input = cv2.imread("./images/bg.jpg")  

        input = cv2.imread(path)
        print(input)
        if input is not None:

            io = BytesIO()
            imgTempResize = im.resize((300, 300))
            print("IMG TEMP")
            # imgArray = np.array(imgTempResize) # converted to array
            imgTemp = remove(input) # passed aray to remove
            print(imgTemp)
            
            imgTempResize = Image.fromarray(imgTemp) # convert back to image
            imgTempResize = im.convert("RGB")
            # print(imgTempResize)
            
            imgTempResize.save(io, format="PNG", quality=85)
            io.seek(0)
            self.images = InMemoryUploadedFile(io, 'ImageField', "%s.jpg" %self.images.name.split('.')[0] , 'image/jpg', sys.getsizeof(io), None, None)
        
        # if input is None:
        #     print("Input value is None")

        # else:
        #     print(input)
        #     output = remove(input)
        #     print(output)
        #     if output is None:
        #         print("Output value is None")
                
        #     else:
        #         image = self.images.name
        #         bgpath = os.path.join(r"./images/", image)
        #         self.images = cv2.imwrite(bgpath, output)


        # print("Uploading after scannning")
        # print(self.images)
        # print(os.path.join(r"./images",str(self.images)))
        super(uploadimage, self).save(*args, **kwargs)



def __str__(self):
    return self.product_name