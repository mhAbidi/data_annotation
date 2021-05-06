import cv2
import numpy as np
import os
import csv
from tqdm import tqdm
import time
# Picture path
"""
Data Annotation Software:


This software is as is and to be used at
users risk.
In case of data corruption; the user is
responsible.


This script is for the annotation of straight.
horizontal lines over images.

Enter  the  path  where  images  are  stored.

You will then be showed images in a new window.

Simply click where you want the annotation line.

If you click somewhere by mistake; simply ignore
it and click at the correct spot.

After the position is satisfactory,
press any key to move to the next image.






Press CTRL+C to stop execution.






"""




#path = input("Enter Path::")
path = r"C:\Users\user\Desktop\Neosoft\Dhanraj Task\hussain\script_demo"

files = os.listdir(path)
directory = path.split("\\")[-1]
label_file = directory+"_labelled.csv"
ya = 0
for item in files:
    if item[-4:] not in ['.jpg', '.bmp','.png','jpeg']:
        files.remove(item)
        
try:
    with open(os.path.join(path,label_file),mode = "r") as labels:
        csv_file = csv.reader(labels)
        for line in csv_file:
            try:
                files.remove(line[0])
            except:
                pass
except:
    pass

for item in files:
    if ".csv" or ".py" in item:
        files.remove(item)

def append_annotation(file_name, list_of_elements):
    with open(file_name, 'a+', newline='') as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(list_of_elem)

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            xy = "%d,%d" % (x, y)
            global ya
            ya = y
            h,w, ch = img.size
            cv2.line(img, (0, y),(w, y), (0, 0, 255), thickness=5)
            cv2.imshow("image", img)
    
    
try:
    if len(files) == 0:
        raise Exception
    for img in tqdm(files):
        t = time.time()
        img_name = img
        img = cv2.imread(img)
        height , width, channels = img.shape
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
        cv2.imshow("image", img)
        cv2.waitkey(0)
        print(time.time()-t)
        append_annotations(label_file,[img_name, "Person", "0; {}; {}; {}".format(ya,w,ya)])

    print("All files done.\nCheck the annotations file for corrections.")    
except KeyboardInterrupt:
    print("Your Progess has been saved")
except Exception:
    print("All files of this folder are annotated.")

input("Execution Stopped.\nPress Enter to exit")    
        


