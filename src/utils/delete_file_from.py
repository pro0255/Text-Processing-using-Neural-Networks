import os

def delete_file_from(path):
    if os.path.exists(path):
        os.remove(path)
        print(f'Deleting file {path}')
    else:
        print(f'File {path} do not exists')