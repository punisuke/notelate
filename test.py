import subprocess
from setup import version

commands = [
    'pip uninstall -y notelate',
    'python setup.py sdist bdist_wheel',
    f'pip install  ./dist/notelate-{version}-py3-none-any.whl',
    'notelate',
    'notelate dark',
    'notelate list',
    'notelate add c:/',
]

for c in commands:
    subprocess.call(c.split())
