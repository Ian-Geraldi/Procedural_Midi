import os
import shutil


def move_to_old():
    # defining source and destination directories
    src_dir = "input"
    dst_dir = "input_old"

    if not os.path.exists(src_dir):
        raise Exception("Source directory does not exist")
    # create the destination directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # get a list of all files in the source directory
    files = os.listdir(src_dir)

    # loop through all the files in the source directory
    for file_name in files:
        # construct full file path
        src_file_path = os.path.join(src_dir, file_name)
        dst_file_path = os.path.join(dst_dir, file_name)

        # move the file to the destination directory
        shutil.move(src_file_path, dst_file_path)
