
# coding: utf-8

# In[101]:


import face_recognition
import os
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
folder="./known/"
image = face_recognition.load_image_file(folder+"abhi(0).jpg")
encoding = face_recognition.face_encodings(image)[0]
encoding= np.array(encoding)
encoding=np.reshape(encoding,(128,1))
print(encoding.shape)
encodings=[]
for filename in os.listdir(folder):
    img=cv2.imread(os.path.join(folder,filename))
    encode=face_recognition.face_encodings(img)[0]
    encode= np.array(encode)
    encode=np.reshape(encode,(128,1))
    print(encode.shape)
    encodings.append(encode)
encodings= np.array(encodings)
#encode=np.reshape(encode,(128,1)) 
#print(encodings)
encodings=np.squeeze(encodings)
angle=cosine_similarity(encoding.T,encodings)

