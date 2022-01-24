import argparse
import sys
from python_project_minify import directory

from pkg_resources import get_distribution, DistributionNotFound

try:
    version = get_distribution('python_project_minify').version
except DistributionNotFound:
    version = '0.0.0'

print(version)

def main():

    parser = argparse.ArgumentParser(prog='minifyProject', description='Minify Python Project Source')
    parser.add_argument('path', type=str, help='The projects source directory')

    args = parser.parse_args()

    sys.stdout.write(
        directory(
            args.path,
        )
    )


if __name__ == '__main__':
    main()