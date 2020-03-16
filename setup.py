#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import os

from setuptools import setup, find_packages

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


def _requires_from_file(filename):
    return open(filename).read().splitlines()


# version
here = os.path.dirname(os.path.abspath(__file__))
version = next((line.split('=')[1].strip().replace("'", '')
                for line in open(os.path.join(here,
                                              'notelate',
                                              '__init__.py'))
                if line.startswith('__version__ = ')),
               '0.0.4')

if __name__ == '__main__':
    setup(
        name="notelate",
        version=version,
        url='https://github.com/punisuke/notelate',
        author='punisuke',
        author_email='punisuke-@outlook.jp',
        maintainer='punisuke',
        maintainer_email='punisuke-@outlook.jp',
        description='generate jupyter notebook/lab template via command line',
        long_description=readme,
        long_description_content_type="text/markdown",
        packages=find_packages(),
        install_requires=_requires_from_file('requirements.txt'),
        license="MIT",
        classifiers=[
            'Programming Language :: Python :: 2',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.3',
                'Programming Language :: Python :: 3.4',
                'License :: OSI Approved :: MIT License',
        ],
        entry_points="""
            # -*- Entry points: -*-
            [console_scripts]
            notelate = notelate.scripts.app:main
            """,
    )
