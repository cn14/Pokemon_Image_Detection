from pathlib import Path
from keras.preprocessing import image
import matplotlib.pyplot as plt
import os

p = Path("./Datasets")

dirs = p.glob("*")

# for d in dirs:
#     print(d)

image_data =[]
labels=[]

labels_dict = {
    "Pikachu":0,
    "Bulbausar":1,
    "Chamender":2
}
label2pokemon = {
    0:"Pikachu",1:"Bulbausar",2:"Chamender"
}

for folder_dir in dirs:
    label = str(folder_dir).split("/")[-1]
    
    cnt=0
    print(folder_dir)
    
    for img_path in folder_dir.glob("*.jpg"):
        img= image.load_img(img_path,target_size=(100,100))
        img_array = image.img_to_array(img)
        image_data.append(img_array)
        labels.append(labels_dict[label])
        cnt+=1
    print(cnt)
    
    import numpy as np
    X=np.array(image_data)
    Y=np.array(labels)

print(X.shape)
print(Y.shape)

def drawImg(img,label):
    plt.imshow(img)
    plt.title(label2pokemon[label])
    plt.show()


for i in range(20):
    r=np.random.randint(400)
    drawImg(X[r]/255,Y[r])
