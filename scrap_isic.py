import pandas as pd
import numpy as np
from tqdm import tqdm

# to plot histogram of colum mel_thick_mm
import matplotlib.pyplot as plt
import seaborn as sns

# if we have any login account we could add the login credentials, it says it could return more data (premium?)

df = pd.read_csv("./Scrap ISIC/metadata.csv", low_memory=False)
data = df.head()

outdir = "./images"

# check number of rows
print(df.shape[0])

df = df.dropna(subset=['mel_class', 'mel_thick_mm'])

# delete invasice melanoma
df = df[df['mel_class'] == 'invasive melanoma']

cont_with_len = df.shape[0] 

# if thickness is grater than 5mm, delete
threshold = 5
df = df[df['mel_thick_mm'] <= threshold]

print("Number of melanoma cases with thickness as data: ", cont_with_len)

# make bins each 0.1mm
sns.histplot(df['mel_thick_mm'], bins=threshold*10, kde=True)
plt.show()

# hist to show the 
print(df.head())

# get unique thickness
folders = df['mel_thick_mm'].unique()

# use command line to download images
import os
os.chdir('./Scrap ISIC')

for folder_name in tqdm(folders):
    path = outdir + '/' + str(folder_name)

    if not os.path.exists(path):
        os.makedirs(path)

    # get all images with the same thickness
    images = df[df['mel_thick_mm'] == folder_name]
    ids = ' OR isic_id:'.join(images['isic_id'])
    ids =  'isic_id:' + ids

    os.system(f"isic.exe image download --search \"{ids}\" {path}")
