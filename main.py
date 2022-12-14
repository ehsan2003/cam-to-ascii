import os
from PIL import Image

# import timeit
import ascii
# def run(image):
#     ascii.do(image,350)
# def runner(path):
#     image = None
#     image = Image.open(path)

# runner("/tmp/img")

# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    im_pil = Image.fromarray(img)
    res = ascii.do(im_pil,200)
    os.system('clear')
    print(res)

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
