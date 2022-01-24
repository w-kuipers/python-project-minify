# Python Project Minify

[![GitHub releases](https://img.shields.io/github/v/release/w-kuipers/python-project-minify)](https://github.com/w-kuipers/python-project-minify/releases)
[![PyPI release](https://img.shields.io/pypi/v/python-project-minify.svg)](https://pypi.org/project/python-project-minify/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Compile your python project into the most compact version it can be. 
This package internally uses the great [Python Minifier](https://github.com/dflook/python-minifier) package.



## Installation

### Install using PIP

    pip install python-project-minify

Note the `pip` refers to the Python 3 package manager. In environment where Python 2 is also available the correct command may be `pip3`.

## Usage

### In console

Run the `minify-project` command in the terminal. It takes two arguments `src` and `dst`.

    minify-project path/to/src path/to/dst

### Python API

Import python_project_minify:

    import python_project_minify

It's simple, just provide a source and destination path:

    python_project_minify.directory('path/to/src', 'path/to/dst')

If you are providing paths with backslashes instead of forwardslashes like the example above, make sure to pass it with the `r` prefix. This way it will be treated as a raw string and won't throw an error.

    python_project_minify.directory(r'path\to\src', r'path\to\dst')

### Ignoring files and folders:
Create a file called `.ppmignore` in the root of your project.

    ## Ignore file in root
    file.txt

    ## Ignore specific file
    folder/subfolder/file.txt

    ## Wildcard ignore file
    *file.txt

    ## Ignore folder in root
    /folder

    ## Ignore specific folder
    /folder/subfolder

    ## Wildcard ignore folder
    */folder

    ## If for some reason it's necessary to keep the .ppmignore file in the destination folder
    PRESERVE_PPMIGNORE

## Support

If you found a problem with the software, please [create an issue](https://github.com/w-kuipers/python-project-minify/issues) on GitHub.

## Maintainer

This project is maintained by [Wibo Kuipers](https://github.com/w-kuipers).

## Contributing

Your contributions are highly appreciated. Please [create a pull request](https://github.com/w-kuipers/python-project-minify/pulls) on GitHub. Bigger changes need to be discussed with the development team via the [issues section at GitHub](https://github.com/w-kuipers/python-project-minify/issues) first.


## License

[MIT LICENSE](https://github.com/w-kuipers/simpleUID/blob/master/LICENSE)
