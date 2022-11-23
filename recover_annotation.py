from pathlib import Path
import cv2 as cv
import random
import os



if __name__ == "__main__":
    dictionary = {}
    imgs = list(os.listdir("/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/Pose/Extreme"))
    imgs += list(os.listdir("/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/Pose/Normal"))
    lines = open("/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/new_annotation.txt", 'r').readlines()
    name = 2
    for line in lines:
        if name == 0:
            dictionary[last_name] = line.rstrip()
            name = 2
        elif name == 1:
            name -= 1
        else:
            last_name = line.rstrip()
            name = 1
    names = list(dictionary.keys())
    new_file = []
    for name in names:
        filename = name.split('/')[-1]
        if filename in imgs:
            if os.path.exists("/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/Pose/Extreme/"+filename):
                new_file.append("Pose/Extreme/"+filename+'\n')
            else:
                new_file.append("Pose/Normal/" + filename+'\n')
            new_file.append('1'+'\n')
            new_file.append(dictionary[name]+'\n')

    open("annotated_pose.txt", 'w').writelines(new_file)
    print(new_file)

