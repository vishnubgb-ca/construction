import os
import xml.etree.ElementTree as ET
import shutil

# Dictionary mapping class numbers to class names
class_names = {
    0: 'Hardhat',
    1: 'Mask',
    2: 'NO-Hardhat',
    3: 'NO-Mask',
    4: 'NO-Safety Vest',
    5: 'Person',
    6: 'Safety Cone',
    7: 'Safety Vest',
    8: 'machinery',
    9: 'vehicle'
}
folder = ["train","valid","test"]
cwd = os.getcwd()
# Path to the labels folder containing the text files
#labels_folder = "/home/ubuntu/construction dataset/css-data/test/labels/"

# Path to the annotations folder where XML files will be stored
#annotations_folder = "/home/ubuntu/construction dataset/css-data/test/annotations/"
for currfolder in folder:
    
    labels_folder = os.path.join(cwd,f"css-data/{currfolder}/labels/")
    annotations_folder = os.path.join(cwd,f"css-data/{currfolder}/annotations/")

    # Create annotations folder if it doesn't exist
    if not os.path.exists(annotations_folder):
        os.makedirs(annotations_folder)

    # Iterate over each text file in the labels folder
    for file_name in os.listdir(labels_folder):
        if file_name.endswith(".txt"):
            # Read the contents of the text file
            with open(os.path.join(labels_folder, file_name), "r") as file:
                lines = file.readlines()

            # Create XML structure
            root = ET.Element("annotation")
            for line in lines:
                values = line.strip().split()
                class_number = int(values[0])
                class_name = class_names.get(class_number)
                if class_name is not None:
                    obj = ET.SubElement(root, "object")
                    ET.SubElement(obj, "name").text = class_name
                    ET.SubElement(obj, "x-center").text = values[1]
                    ET.SubElement(obj, "y-center").text = values[2]
                    ET.SubElement(obj, "width").text = values[3]
                    ET.SubElement(obj, "height").text = values[4]

            # Create XML tree
            tree = ET.ElementTree(root)

            # Write XML tree to file
            xml_file_name = file_name.replace(".txt", ".xml")
            xml_file_path = os.path.join(annotations_folder, xml_file_name)
            tree.write(xml_file_path)

# Move XML files to annotations folder
    for file_name in os.listdir(labels_folder):
        if file_name.endswith(".xml"):
            shutil.move(os.path.join(labels_folder, file_name), annotations_folder)



#import os
#
## Path to the folder
#folder_path = "/home/ubuntu/construction dataset/css-data/test/annotations/"  # Change this to the path of your folder
#
## List all files in the folder
#files = os.listdir(folder_path)
#
## Count the number of files
#num_files = len(files)
#
#print("Number of files in the folder:", num_files)