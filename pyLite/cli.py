import click
import os
import shutil
from .utils import copy_template, create_directory

@click.group()
def main():
    pass

@main.command()
@click.argument('project_name')
def create(project_name):
    """
    Create a new PyLite project.
    """
    base_dir = os.getcwd()
    project_dir = os.path.join(base_dir, project_name)

    if os.path.exists(project_dir):
        click.echo(f"Directory {project_name} already exists!")
        return

    create_directory(project_dir)
    copy_template('app.py', project_dir)
    copy_template('config.py', project_dir)
    copy_template('run.py', project_dir)
    copy_template('requirements.txt', project_dir)
    copy_template('schema.py', project_dir)
    copy_template('development.log', project_dir)

    pyLite_dir = os.path.join(project_dir, 'components', 'blog')
    create_directory(pyLite_dir)



    components_dir = os.path.join(project_dir, 'components', 'blog')
    create_directory(components_dir)
    copy_template('components/blog/service.py', components_dir)
    copy_template('components/blog/url.py', components_dir)

    platform_dir = os.path.join(project_dir, 'platform')
    create_directory(platform_dir)

    for platform in ['desktop', 'web', 'mobile']:
        platform_path = os.path.join(platform_dir, platform)
        create_directory(platform_path)
        copy_template(f'platform/{platform}/url.py', platform_path)
        copy_template(f'platform/{platform}/settings.py', platform_path)

    click.echo(f"Project {project_name} created successfully!")

@main.command()
@click.option('--platforms', multiple=True, default=['backend'], help="Specify platforms to run (e.g. --platforms backend desktop web mobile)")
def run(platforms):
    """
    Runy the PyLite application.
    """
    platforms_str = " ".join(platforms)
    os.system(f'python run.py --platforms {platforms_str}')

if __name__ == "__main__":
    main()
