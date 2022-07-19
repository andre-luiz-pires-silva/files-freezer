#!/usr/bin/env python3
import argparse
import logging
import os
import subprocess
import time
from datetime import datetime

import files_handler

parser = argparse.ArgumentParser(description='A test program.')
parser.add_argument("--media", help="Media location")
parser.add_argument("--storage-path", help="Path where the files will be copied to")
args = parser.parse_args()
media_location = args.media
storage_path = args.storage_path

working_dir = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    format='%(asctime)s %(message)s', level=logging.DEBUG,
    handlers=[
        logging.FileHandler(f"{working_dir}/media_bkp.log"),
        logging.StreamHandler()
    ]
)

logging.debug(f"Starting media backup")
logging.debug("Working directory %s", working_dir)


time_seconds = int(time.time())
bkp_folder = f"{storage_path}/{datetime.now().strftime('%Y/%m/%d-%m-%Y_%H_%M_%S')}"
files_count = files_handler.count_files(media_location)
logging.debug(f"Copying {files_count} files from '{media_location}' to '{bkp_folder}'")
files_handler.copy_all(media_location, bkp_folder, lambda src, dst: logging.debug('Copying %s', src))


logging.debug(f"umount '{media_location}'")
p = subprocess.Popen(f"umount '{media_location}'", stdout=subprocess.PIPE, shell=True)
p.communicate()


logging.debug("Finish!")
