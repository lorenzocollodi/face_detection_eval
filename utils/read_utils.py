def read_file_key(file_path, key):
    imgs = {}
    name = None
    faces = []
    num_faces = 0
    read_faces = False
    for line in open(file_path, 'r'):
        if line.startswith(key):
            read_faces = True
            name = line.rstrip()
        elif read_faces:
            num_faces = int(line.rstrip())
            if num_faces == 0:
                imgs[name] = []
            read_faces = False
        elif num_faces:
            faces += [[int(elem) for elem in line.rstrip().split(' ')[:4]]]
            num_faces -= 1
            if not num_faces:
                imgs[name] = faces
                faces = []
    return imgs