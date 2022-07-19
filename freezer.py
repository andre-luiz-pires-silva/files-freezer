import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("config.ini")
    images_path = config.get("core", "ImagesPath")
    print(f"Images Path: {images_path}")
