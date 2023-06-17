import os
import shutil


def move_to_old():
    # defining source and destination directories
    src_dir = "input"
    dst_dir = "input_old"

    # create the destination directory if it doesn't exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # get a list of all files in the source directory
    files = os.listdir(src_dir)

    # loop through all the files in the source directory
    for file_name in files:
        # construct full file path
        src_file_path = os.path.join(src_dir, file_name)

        # If file with the same name exists in the destination directory,
        # append a number in brackets to the filename until a unique name is found
        if os.path.isfile(os.path.join(dst_dir, file_name)):
            # split the filename into name and extension
            base_name, ext = os.path.splitext(file_name)
            counter = 1
            while os.path.isfile(os.path.join(dst_dir, f"{base_name}({counter}){ext}")):
                counter += 1
            file_name = f"{base_name}({counter}){ext}"

        dst_file_path = os.path.join(dst_dir, file_name)

        # move the file to the destination directory
        shutil.move(src_file_path, dst_file_path)
