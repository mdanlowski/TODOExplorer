import sys
import os
from pathlib import Path

def excluded_filetypes():
    return [\
    ".pyc", ".pyo", ".exe", ".dll", ".obj", ".o", ".a", ".lib", ".so", ".dylib",\
     ".ncb", ".sdf", ".suo", ".pdb", ".idb", ".DS_Store", ".class", ".psd", ".db", \
     ".sublime-workspace", ".cache", ".keep", ".jpeg", ".jfif", ".exif", ".tiff",\
     ".gif", ".bmp", ".png", ".ppm", ".pgm", ".pbm", ".pnm", ".webp", ".hdr", ".heif",\
     ".bpg", ".cgm", ".svg", ".ttf", ".log"]


def excluded_folders(): ### @TODO
    return [\
    "node_modules"]


def prepare_files(paths):
    # return some files
    files = []
    ix = 1
    for path in paths:
        fext = path[path.rfind('.'):]

        if fext not in excluded_filetypes() and ix > 0:
            f = open(path, 'r')
            files.append(f)

        ix += 1
            
    return files
			

def prepare_tree():
    root_path = ''
    paths = []
    # if len(optional_root_path) < 1 and len(sys.argv) > 1:
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
    else:
        root_path = os.getcwd()

    print(root_path)

    for r, d, p in os.walk(root_path):
        paths += [os.path.join(r, x) for x in p if (x[x.rfind('.'):].lower() not in excluded_filetypes() and x.rfind('.') > 0 )]
    
    for p in paths:
        p = Path(p)

    return paths