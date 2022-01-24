import os
import python_minifier
from shutil import copyfile
from pathlib import Path
from .ignore import get_list

def directory(src, dst):
    
    ## Format paths
    src = os.path.abspath(src)+os.sep
    dst = os.path.abspath(dst)+os.sep

    ## Get a list of files to be ignored
    ignore = get_list('{}/.ppmignore'.format(src))

    ## Create a loop from src directory
    for root, dirs, files in os.walk(src, topdown=True):

        ## Don't need absolute path
        curdir = root.replace(os.path.normpath(src), '')

        curdir_list = curdir.split('\\')

        ## Ignore in root
        if os.path.normpath('/{}'.format(curdir_list[0])) in ignore:
            continue

        ## Static path ignore
        if os.path.normpath(curdir) in ignore:
            continue

        ## Wildcard ignores
        should_skip = False
        for sub in curdir_list:
            if os.path.normpath('*/{}').format(sub) in ignore:
                should_skip = True
                continue
        if should_skip:
            continue

        ## Generate directory
        newdir = os.path.abspath(dst) + curdir
        if not os.path.exists(newdir) and os.path.isdir(Path(newdir).parent.absolute()):
            os.mkdir(newdir)

        ## Create loop from files in folder
        filedir = os.path.abspath(src) + curdir
        for file in os.listdir(filedir):
            if not os.path.isdir(os.path.join(filedir, file)) and os.path.isdir(Path(newdir).parent.absolute()):
                filename = os.fsdecode(file)

                ## Ignore in root
                if filedir == os.path.abspath(src) + os.sep:
                    if filename in ignore:
                        continue

                ## Static path ignore
                print(os.path.normpath(curdir)[1:] + os.sep + filename)
                print(ignore)
                if os.path.normpath(curdir)[1:] + os.sep + filename in ignore:
                    continue

                ## Wildcard ignores
                if '*{}'.format(filename) in ignore:
                    continue

                ## If Python file, minify
                if filename.endswith(".py"):
                    
                    with open(filedir + os.sep + filename) as f:
                        minified = python_minifier.minify(f.read())

                    with open(newdir + os.sep + filename, 'w') as f:
                        f.write(minified)
                    continue
                    
                ## If not Python file, just copy
                copyfile(filedir + os.sep + filename, newdir + os.sep + filename)