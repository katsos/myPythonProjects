import os

def rename_files():
    file_list = os.listdir(r".\files")

    os.chdir(r".\files")

    for filename in file_list:
        os.rename(filename, filename.translate(None,"0123456789"))

    os.chdir(r"..")

# main
rename_files()
