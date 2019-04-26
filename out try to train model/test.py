#!/usr/bin/env python
# coding: utf-8

# ## import required libraries

# In[1]:


import numpy as np
from scipy.misc import imresize
from moviepy.editor import VideoFileClip
from keras.models import load_model


# In[ ]:


#load keras model
model = load_model('movieColor.h5')


# In[ ]:


#processing that will be done per frame
def color(frame):
    #resizing image to match size of input image inside model
    resizedImage = imresize(frame,(256,256))
    resizedImage = np.array(resizedImage)
    resizedImage = resizedImage[None,:,:]
    
    # Make prediction with neural network (un-normalize value by multiplying by 255)
    prediction = model.predict(resizedImage)*255
    
    # Re-size image we will consider output image to be in 720p
    result = imresize(prediction, (720, 1280, 3))
    
    return result
    
    


# In[ ]:


# output video after processing
outputVideo = 'out.mp4'

# reading input video
movie = VideoFileClip(".mp4")

# call function color for each fram in movie
vid_clip = movie.fl_image(color)
vid_clip.write_videofile(outputVideo, audio=True)

