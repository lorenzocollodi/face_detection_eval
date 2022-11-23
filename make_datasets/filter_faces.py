from pathlib import Path

input_files = ["/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/UFDD-annotationfile/UFDD_split/UFDD_val_bbx_gt.txt", "/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/wider_face_split/wider_face_val_bbx_gt.txt"]


if __name__ == "__main__":
    cnt = 0
    with open("/Users/lorenzocollodi/Desktop/Tesi Sant'Anna/Eval/Data/new_annotation.txt", 'w') as wfile:
        for file in input_files:
            lines = []
            for line in open(file, 'r').readlines():
                lines.append(line)
            a = True
            idx = 0
            while a:
                faces = int(lines[idx+1])
                if faces == 1:
                    if  int(lines[idx+2].split(' ')[2])**2 + int(lines[idx+2].split(' ')[3])**2 > 10000:
                        wfile.writelines(lines[idx:idx+3])
                        cnt += 1
                idx += 2+faces
                if len(lines) == idx:
                    a = False
    print(cnt)