
import os
import subprocess

from echeapi import settings


def main(*args):
    os.chdir(settings.SRC_DIR)

    print('=== FLAKE8 ===')
    subprocess.run(['flake8'])

    print('=== ISORT ===')
    subprocess.run(['isort', '--apply'])
