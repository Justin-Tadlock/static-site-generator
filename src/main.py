import os
import shutil

def delete_files(destination):
    print(f'deleting files from {destination}')
    files = os.listdir(destination)
    curr_dir = os.path.abspath(destination)
    for f in files:
        f_path = os.path.join(curr_dir, f)
        if os.path.isdir(f_path):
            delete_files(f_path)
            shutil.rmtree(f_path)
        else:
            print(f'removing {f} from {curr_dir}')
            os.remove(f_path)

def copy_files(source, destination):
    print(f'copying files from {source} to {destination}')
    files = os.listdir(source)
    curr_dir = os.path.abspath(source)
    for f in files:
        f_path = os.path.join(curr_dir, f)
        dest_path = os.path.join(destination, f)

        if os.path.isdir(f_path):
            if not os.path.exists(dest_path):
                print(f'making {dest_path}')
                os.mkdir(dest_path)
            copy_files(f_path, dest_path)
        else:
            print(f'copying {f} to {dest_path}')
            shutil.copy(f_path, dest_path)

def copy_static_files(source, destination):
    delete_files(destination)
    
    copy_files(source, destination)

def main():
    curr_dir = os.path.abspath(os.path.curdir)
    copy_static_files(os.path.join(curr_dir, 'static'), os.path.join(curr_dir, 'public'))

if __name__ == "__main__":
    main()