import os
import shutil


def count_files(path):
    return sum([len(files) for r, d, files in os.walk(path)])


def copy_all(from_path, to_path, listener_fn):
    def copy_fn(src, dst):
        listener_fn(src, dst)
        shutil.copy2(src, dst)

    shutil.copytree(from_path, to_path, copy_function=copy_fn)
