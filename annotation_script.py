import cv2
import os
from tqdm import tqdm
import pandas as pd

info = """
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


# Capturesthe pointer location's Y coordinates
def process_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global ya
        ya = y
        h, w, ch = image.shape
        cv2.line(image, (0, y), (w, y), (0, 0, 255), thickness=1)
        cv2.imshow("image", image)


if __name__ == '__main__':
    ### Configs ###

    path = r"C:\Users\user\Desktop\Neosoft\Dhanraj Task\hussain\script_demo" # The path where the data is stored
    output_label_file = "script_demo_labelled.csv"  # Output file path

    files = os.listdir(path)
    ya = 0

    annotated_images = []
    if os.path.exists(output_label_file):
        df = pd.read_csv(output_label_file)
        annotated_images = list(set(df['file_name']))
    else:
        with open(output_label_file, 'w') as csv:
            csv.write("file_name,classes,coordinates\n")

    try:
        with open(output_label_file, 'a+') as csv:
            for img in tqdm(files):
                if img[-4:] in ['.jpg', '.bmp', '.png', 'jpeg'] and img not in annotated_images:
                    image = cv2.imread(os.path.join(path, img))
                    h, w, ch = image.shape
                    cv2.namedWindow("image")
                    cv2.setMouseCallback("image", process_mouse_click)
                    cv2.imshow("image", image)
                    cv2.waitKey(10000)  # 10 seconds waiting time for annotation
                    to_write = "{}, Person, 0; {}; {}; {}\n".format(img, ya, w, ya)
                    csv.write(to_write)

    except KeyboardInterrupt:
        print("Your Progess has been saved")

    cv2.destroyAllWindows()
    print("All Data successfully annotated.")
