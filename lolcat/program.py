import os
import cat_service
import subprocess
import platform

def main():
    #print header
    #get or create output folder
    #download cats
    #display cats
    print_header()
    path = initialise_folder()
    download_cats(path)
    display_cats(path)

def print_header():
    print('----------------------')
    print('                      CAT FACTORY')
    print('----------------------')

def download_cats(folder):
    print('Contacting server to download some cats')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print ('Downloading cat ' + name)
        cat_service.get_cat(folder, name)

def initialise_folder():
    base = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base, folder)

    print(full_path)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print("Creating new directory at {}".format(full_path))
        os.mkdir(full_path)

    return full_path

def display_cats(folder):

    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['explorer', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os {}".format(platform.system()))
    

if __name__ == '__main__':
    main()