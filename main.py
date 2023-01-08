import pandas as pd
import os

test_data_dir = "data/ISIC_2019_Test_Input/"
train_data_dir = "data/ISIC_2019_Training_Input/"
img_paths = ["data/ISIC_2019_Test_Input/" + os.listdir(test_data_dir)[i] for i in range(len(test_data_dir))]

print(img_paths[0])
print("Hello there")