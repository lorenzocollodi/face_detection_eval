import os

def get_data():
    os.system()

def main():
    for file in os.listdir("Annotation"):
        for img in list(open(os.path.join("Annotation", file), 'r').readlines())[::3]:
            os.system(f"mv Data/{img.split('/')[-1].rstrip()} Data/{img.rstrip()}")

if __name__ == "__main__":
    main()