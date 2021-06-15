import click
from pathlib import Path


last_cmd_file = Path.home() / '.select-pyenv'


@click.command()
def cli():
    """Select pyenv."""
    versions = list_pyenv_versions()
    default_version_name = str(Path('.').absolute().parts[-1])
    if default_version_name in versions:
        default_idx = versions.index(default_version_name) + 1
    else:
        default_idx = None

    print(f"\t[0]: + Create a new version")
    for i, v in enumerate(versions):
        print(f"\t[{str(i + 1)}]: {v}")

    idx = click.prompt(
        f"Please enter your choice (0-{str(len(versions))})",
        type=click.IntRange(0, len(versions)),
        default=default_idx
    )
    if idx == 0:
        base_idx = click.prompt(
            f"Specify base (1-{str(len(versions))})",
            type=click.IntRange(1, len(versions)),
        )
        version = click.prompt(
            'Specify new version name',
            type=click.STRING,
            default=default_version_name,
        )
        cmd = create_pyenv_version(versions[base_idx - 1], version)
    else:
        cmd = select_pyenv_version(versions[idx - 1])

    print(cmd)
    with last_cmd_file.open('w') as f:
        f.write(cmd)


def list_pyenv_versions():
    version_dir = Path.home() / '.pyenv' / 'versions/'
    return sorted([f.name for f in version_dir.iterdir()])


def select_pyenv_version(version):
    return build_command(['source', 'activate', version])


def create_pyenv_version(base_version, version):
    return build_command(['pyenv', 'virtualenv', base_version, version])


def build_command(cmd_pieces):
    return ' '.join(cmd_pieces)
