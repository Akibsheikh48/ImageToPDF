import os
from PIL import Image

class ImageToPDF(object):
    def __init__(self, image_path):
        self.image_path = image_path

        self.file_name = str(image_path.split("\\")[-1])

    def convert(self):
        try:
            new_file = os.path.join(self.image_path.replace(self.file_name.split(".")[-1], "pdf"))
            image_file = Image.open(self.image_path)
            result = image_file.convert("RGB")
            result.save(new_file)
            print("convertion successful...")
        except:
            print("convertion unsuccessful...")


if __name__ == '__main__':
    image = input(r"Drag image here>>>")
    ImageToPDF(image).convert()