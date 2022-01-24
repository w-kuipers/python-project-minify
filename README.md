# Python Project Minify

[![GitHub releases](https://img.shields.io/github/v/release/w-kuipers/simpleUID)](https://github.com/w-kuipers/python-project-minify/releases)
[![PyPI release](https://img.shields.io/pypi/v/simpleUID.svg)](https://pypi.org/project/python-project-minify/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Compile your python project into the most compact version it can be. 
This package internally uses the great [Python Minifier](https://github.com/dflook/python-minifier) package.



## Installation

### Install using PIP

    pip install python-project-minify

Note the `pip` refers to the Python 3 package manager. In environment where Python 2 is also available the correct command may be `pip3`.

## Usage

Import python_project_minify:

    import python_project_minify

It's simple, just provide a source and destination path:

    python_project_minify.directory('path/to/src', 'path/to/dst')

## Support

If you found a problem with the software, please [create an issue](https://github.com/w-kuipers/python-project-minify/issues) on GitHub.

## Maintainer

This project is maintained by [Wibo Kuipers](https://github.com/w-kuipers).

## Contributing

Your contributions are highly appreciated. Please [create a pull request](https://github.com/w-kuipers/python-project-minify/pulls) on GitHub. Bigger changes need to be discussed with the development team via the [issues section at GitHub](https://github.com/w-kuipers/python-project-minify/issues) first.


## License

[MIT LICENSE](https://github.com/w-kuipers/simpleUID/blob/master/LICENSE)
