"""
Quickly set the appropriate DJANGO_SETTINGS_MODULE
"""

from pathlib import Path


def check_file_system(abspath):
    """Checks filesysten for required directories

    Parse through the Django Project Root to ensure that all required
    directories exist, creating them if they do not.

    Args:
        abspath (str): Absolute path to the Django Project Root
    """
    DIRS = ['apps', 'docs', 'logs', 'fixtures', 'media', 'static']
    for directory in DIRS:
        _posixPath = Path(abspath).joinpath(directory)
        if not Path(_posixPath).exists():
            Path(_posixPath).mkdir()


def get_available_settings(abspath):
    """Get Available Settings Modules

    Searches for all available settings modules; prints to the
    Command-Line Interface (CLI) for quick copy / paste.

    Args:
        abspath (str): Absolute path to the Django Project Root
    """
    filenames = []
    excluded_files = ['base.py', '__init__.py', '__pycache__']
    for filename in SETTINGS_DIR.iterdir():
        if not Path(filename).suffix == '.pyc' \
                and Path(filename).name not in excluded_files:
            filenames.append(Path(filename).name)
    if len(filenames) > 0:
        print(f'\n{YELLOW}Please select a DJANGO_SETTINGS_MODULE:{RESET}')
        for filename in filenames:
            print(
                '\t{0}export DJANGO_SETTINGS_MODULE='
                '{1}.settings.{2}{3}'.format(
                    YELLOW,
                    '{{ project_name }}',
                    filename[:-3],
                    RESET
                )
            )
    else:
        print(f'{RED}No DJANGO_SETTINGS_MODULE files found!{RESET}')


if __name__ == "__main__":

    # Terminal Output Color
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    SETTINGS_DIR = Path(PROJECT_ROOT).joinpath('{{ project_name }}/settings')

    check_file_system(PROJECT_ROOT)
    get_available_settings(PROJECT_ROOT)
