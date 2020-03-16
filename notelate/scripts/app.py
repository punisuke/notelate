from .notelate import Notelate
import requests
import os
import sys
import glob
import shutil
import warnings
warnings.simplefilter("ignore")


# templates in this list is installed by default
template_list = [
    'basic',
    'dark'
]


def main():
    nl = Notelate(template_list)
    if len(sys.argv) == 1:
        templat_name = 'basic'
        nl.copy_template(templat_name)
        return True

    if sys.argv[1] == 'list':
        print('printing template list in local')
        nl.print_list(local=False)
    elif sys.argv[1] == 'local':
        print('printing template list in local')
        nl.print_list(local=True)
    elif sys.argv[1] == 'add':
        nl.add_template_path(sys.argv[2])
    else:
        templat_name = sys.argv[1]
        nl.copy_template(templat_name)


if __name__ == '__main__':
    main()
