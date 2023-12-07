import os
from PIL import Image, ImageSequence
import numpy as np


# Load the images
frames = []
score_duration=[]
for i in range(25):
    score = -1
    filename = str(i)+"_"+str(score)+".png"
    while os.path.isfile(filename):
        with open(filename) as img:
            img = Image.open(filename)
            frames.append(img)
            # img.close()
            score -= 1
            filename = str(i)+"_"+str(score)+".png"
            score_duration.append(0)
    filename = str(i)+"_win.png"
    img = Image.open(filename)
    frames.append(img)
    score_duration.append(i)

for i in range(len(score_duration)):
    if score_duration[i]==0:
        score_duration[i]= 100
    else:
        score_duration[i]= 400
print(score_duration)
# Set the options
duration = 100  # duration of each frame in milliseconds
loop = 0  # number of loops (0 for infinite loop)
optimize = True  # enable GIF optimization

# Convert the images to GIF
frames[0].save("animation.gif", format="GIF", append_images=frames[1:], save_all=True, duration=score_duration, loop=loop, optimize=optimize)