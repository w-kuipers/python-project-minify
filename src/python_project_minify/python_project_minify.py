import os
import python_minifier
from ignore import get_list
import collections

def directory(src, dst):
    
    ## Format paths
    src = os.path.abspath(src)+os.sep
    dst = os.path.abspath(dst)+os.sep

    ## Get a list of files to be ignored
    ignore = get_list('{}/.ppmignore'.format(src))

    ## Create a loop from src directory
    for root, dirs, files in os.walk(src, topdown=True):

        ## Don't need absolute path
        curdir = root.replace(src, '')

        curdir_list = curdir.split('\\')

        ## ignore in roots
        if curdir_list[0] in ignore:
            continue

        ## Wildcard ignores
        should_skip = False
        for sub in curdir_list:
            if '*{}'.format(sub) in ignore:
                should_skip = True
                continue
        if should_skip:
            continue

        ## Generate directory
        newdir = os.path.abspath(dst)+os.sep + curdir
        if not os.path.exists(newdir):
            os.mkdir(newdir)

        ## Create loop from files in folder
        filedir = os.path.abspath(src)+os.sep + curdir
        for file in os.listdir(filedir):
            filename = os.fsdecode(file)
            if filename.endswith(".py"): 
                
                with open(filedir + os.sep + filename) as f:
                    minified = python_minifier.minify(f.read())

                with open(newdir + os.sep + filename, 'w') as f:
                    f.write(minified)
        
directory('C:/Users/wibo-/Desktop/FMM/TESTS/', 'C:/Users/wibo-/Desktop/FMM/TEMP')