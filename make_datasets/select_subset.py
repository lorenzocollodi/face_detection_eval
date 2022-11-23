from pathlib import Path
import cv2 as cv
import random
import os


dst_A = "Ethnics/African"
dst_S = "Accessories/No"
dst_D =  "Accessories/No"
annot_file = "annotated_ethnics.txt"

if __name__ == "__main__":
    dictionary = {}
    lines = open("/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/new_annotation.txt", 'r').readlines()
    name = 2
    for line in lines:
        if name == 0:
            dictionary[last_name] = line
            name = 2
        elif name == 1:
            name -= 1
        else:
            last_name = "Aggregated/"+line.rstrip()
            name = 1
    names = list(dictionary.keys())
    random.shuffle(names)
    new_file = []
    for name in names:
        path = f"{name.rstrip()}"
        print(path)
        img = cv.imread(path)
        cv.imshow("Window", img)
        key = cv.waitKey(-1)
        cv.destroyAllWindows()
        if key == ord('a'):
            name = (os.path.join(dst_A, name.rstrip().split('/')[-1]))
            if not(os.path.exists(name)):
                cv.imwrite(os.path.join(dst_A, name.rstrip().split('/')[-1]), img)
                new_file.append(name+'\n')
                new_file.append('1\n')
                new_file.append(dictionary[path])
        elif key == ord('s'):
            name = (os.path.join(dst_S, name.rstrip().split('/')[-1]))
            if not(os.path.exists(name)):
                cv.imwrite(os.path.join(dst_S, name.rstrip().split('/')[-1]), img)
                new_file.append(name+'\n')
                new_file.append('1\n')
                new_file.append(dictionary[path])
        elif key == ord('d'):
            name = (os.path.join(dst_D, name.rstrip().split('/')[-1]))
            if not(os.path.exists(name)):
                cv.imwrite(os.path.join(dst_D, name.rstrip().split('/')[-1]), img)
                new_file.append(name+'\n')
                new_file.append('1\n')
                new_file.append(dictionary[path])
        elif key == ord('n'):
            break
    open(annot_file, 'a').writelines(new_file)
