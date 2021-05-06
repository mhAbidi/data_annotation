import cv2
import numpy as np
import os
import csv
from tqdm import tqdm
import time
import pandas as pd
# Picture path
info="""
Data Annotation Software:

This software is as is and to be used at users risk.
In case of data corruption; the user is responsible.

This script is for the annotation of straight horizontal lines over images.
Enter  the  path  where  images  are  stored.
You will then be showed images in a new window.
Simply click where you want the annotation line.
If you click somewhere by mistake; simply ignore it and click at the correct spot.
If you close the image without clicking; 0,0,width,0 is annoted.
After the position is satisfactory, press any key to move to the next image.

Directly close the shell to stop execution.

The script will continue where you left off.


Cheers!



Press Enter to start.


"""
os.system("cls")
input(info)
os.system("cls")


path = input("Enter Path::")
#class_name = input("Enter Class Name:")
files = os.listdir(path)
directory = path.split("\\")[-1]
label_file = directory+"_labelled.csv"
ya = 0

check_df = True


if os.path.exists(os.path.join(path, label_file)):
    df = pd.read_csv(os.path.join(path, label_file))
else:
    check_df = False


def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                xy = "%d,%d" % (x, y)
                global ya
                ya = y
                h,w,ch = img.shape
                cv2.line(img, (0, y), (w, y), (0, 0, 255), thickness=1)
                cv2.imshow("image", img)

        
def append_annotation(file_name, list_of_elements):
    with open(file_name, 'a+', newline='') as file:

        writer = csv.writer(file, delimiter=",")
        writer.writerow(list_of_elements)

   
        
try:
    if len(files) == 0:
        raise Exception('All files are done')
     
    for img in tqdm(files):
        if img[-4:] in ['.jpg', '.bmp','.png','jpeg']:
            if "csv" in img:
                continue
            if check_df:
                if img in df.to_string():
                    continue
            img_name = img
            img = cv2.imread(os.path.join(path,img))
            h,w,ch = img.shape
            cv2.namedWindow("image")
            cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
            cv2.imshow("image", img)
            cv2.waitKey(0)
            y = ya
            append_annotation(label_file,[img_name, "Person", "0; {}; {}; {}".format(ya,w,ya)])

    print("All files done.\nCheck the annotations file for corrections.")    
except KeyboardInterrupt:
    print("Your Progess has been saved")
except Exception as e:
    print(e)
    print("All files of this folder are annotated.")
cv2.destroyAllWindows()
input("Execution Stopped.\nPress Enter to exit")    
        


