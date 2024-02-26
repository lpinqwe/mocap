import os

import cv2


class Writer:
    photo_dir_path = r"C:\Users\vwork\PycharmProjects\droneDetector_V1\dataset\photos"
    csv_file_path = r"C:\Users\vwork\PycharmProjects\droneDetector_V1\dataset\coords.txt"
    file = None

    def __init__(self, path_photo_dir='', csv_path_file=''):
        if (path_photo_dir != ''):
            self.photo_dir_path = path_photo_dir
        if (csv_path_file != ''):
            self.csv_file_path = csv_path_file
        self.file = open(self.csv_file_path, 'a')
        os.chdir(self.photo_dir_path)

    def write(self, coords, photo):
        print(type(self.file))
        print(str(coords))
        self.file.write(str(coords)+"\n")
        cv2.imwrite(f"img_{str(coords)}.jpg", photo)

        pass
