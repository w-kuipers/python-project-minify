import argparse
from python_project_minify import directory

from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('python_project_minify').version
except DistributionNotFound:
    __version__ = '1.0.1'

def main():

    parser = argparse.ArgumentParser(prog='minify-project', description='Minify Python Project Source')
    parser.add_argument('src', type=str, help='The project source directory')
    parser.add_argument('dst', type=str, help='The minified project destination directory')

    args = parser.parse_args()

    directory(args.src,args.dst)

if __name__ == '__main__':
    main()