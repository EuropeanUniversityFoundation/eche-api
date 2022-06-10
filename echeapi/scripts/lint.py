
import subprocess


def main():
    print('=== FLAKE8 ===')
    subprocess.run(['flake8'])

    print('=== ISORT ===')
    subprocess.run(['isort', '--apply'])


if __name__ == '__main__':
    main()
