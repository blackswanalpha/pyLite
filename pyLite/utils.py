import os
import shutil

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'templates')


def copy_template(template_name, dest_dir):
    """
    Copy a template file to the destination directory.
    """
    template_path = os.path.join(TEMPLATES_DIR, template_name)
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template {template_name} does not exist!")

    shutil.copy(template_path, dest_dir)


def create_directory(directory):
    """
    Create a directory if it doesn't exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
