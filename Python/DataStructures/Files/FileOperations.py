import os, shutil

def mirrorFolder(source, dest):
    for path, dirs, files in os.walk(source):
        touch_folder(dest+path.split(source,1)[-1])
         
def move_folder(source, dest):
    return shutil.move(source, dest)
    
def move_file(source, dest):
    return shutil.move(source, dest)
    
def copy_file(source, dest):
    return shutil.copyfile(source, dest)
            
def copy_folder(source, dest):
    return shutil.copytree(source, dest)

def pwd():
    return os.path.dirname(os.path.abspath(__file__))

def exists(path):
    return os.path.exists(path)
        
def move(src, dest):
    return shutil.move(src, dest)
        
def touch_file(path):
    return open(path, 'a').close()

def touch_folder(path):
    return os.makedirs(path)
            
def write_text(path, text):
    with open(path, 'w') as file:
        file.write(text)

def is_readable(path):
    return os.access(path, os.F_OK)

def is_writeable(filePath):
    return os.access(path, os.W_OK)
    
def listdir(path):
    return os.listdir(path)

def remove_extraneous(itemlist):
    for a in ['Thumbs.db', '.DS_Store', 'Desktop.ini']:
        itemlist.remove(a)
    return itemlist
    
