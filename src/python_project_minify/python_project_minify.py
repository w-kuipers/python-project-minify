from shutil import copyfile
from pathlib import Path
from .ignore import get_list ## Remove dot for dev
from tqdm import tqdm
from colorama import init, Fore
import os
import python_minifier

## Initialize colorama
init(autoreset=True)

def directory(src, dst):   
    
    ## Format paths
    src = os.path.abspath(src)+os.sep
    dst = os.path.abspath(dst)+os.sep

    ## Get a list of files to be ignored
    ignore = get_list('{}/.ppmignore'.format(src))

    ## Generate path list
    path_list = list(enumerate(os.walk(src, topdown=True)))

    ## Calculate amount of files to process
    amount_to_process = 0
    for i, root_dirs_files in path_list:
        amount_to_process += 1

    ## Initialize progressbar
    progress_bar = tqdm(0, total=amount_to_process, desc="Processing files", leave=False)

    ## Create a loop from src directory
    for i, root_dirs_files in path_list:

        progress_bar.update(1)

        root = root_dirs_files[0]

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


    progress_bar.close()
    print(Fore.GREEN + "\nMinified.")

    return