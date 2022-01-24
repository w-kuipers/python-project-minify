import os

def get_list(ignore_file):

    ## Need empty list
    ignore = []

    ## Check if file exists
    if not os.path.exists(ignore_file):
        return [] ## Return empty list if file not exist

    ## Read file and create list of lines
    with open(ignore_file, "r") as f:
        for l in f:
            if l == '\n' or l.lstrip()[0] == '#': ## Ignore empty lines and commented lines
                continue

            ignore.append(l.strip())

    ## Add .ppmignore to list
    if not 'PRESERVE_PPMIGNORE' in ignore:
        ignore.append('*.ppmignore')

    return ignore