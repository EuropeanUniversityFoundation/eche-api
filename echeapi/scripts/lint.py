
import os
import subprocess

from echeapi import settings


def main():
    os.chdir(settings.src_dir)

    print('=== FLAKE8 ===')
    subprocess.run(['flake8'])

    print('=== ISORT ===')
    subprocess.run(['isort', '--apply'])


if __name__ == '__main__':
    main()
