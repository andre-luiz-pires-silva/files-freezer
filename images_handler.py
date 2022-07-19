import math
import os
from PIL import Image

SUMMARY_IMAGE_CELL_SIZE = 50


def create_summary_image(source_path, target_file_path):
    print("Creating summary image")
    image_files = os.listdir(source_path)
    image_files_count = len(image_files)
    summary_size = math.ceil(math.sqrt(image_files_count)) * SUMMARY_IMAGE_CELL_SIZE

    target_image = Image.new("RGB", (summary_size, summary_size))
    position = None
    for file_name in image_files:
        if not position:
            position = (0, 0)
        else:
            x = 0 if position[0] >= summary_size - SUMMARY_IMAGE_CELL_SIZE else position[0] + SUMMARY_IMAGE_CELL_SIZE
            y = position[1] if x > 0 else position[1] + SUMMARY_IMAGE_CELL_SIZE
            position = (x, y)

        image = Image.open(f"{source_path}/{file_name}")
        image = image.resize((SUMMARY_IMAGE_CELL_SIZE, SUMMARY_IMAGE_CELL_SIZE))
        target_image.paste(image, position)

    target_image.save(target_file_path)

if __name__ == '__main__':
    create_summary_image("/home/apires/alps/files-freezer/images-sample", "/home/apires/alps/files-freezer/test.jpg")