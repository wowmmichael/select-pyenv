from setuptools import setup

setup(
    name="select-pyenv",
    version="0.0.1",
    install_requires=[
        'Click',
    ],
    extras_require={"dev": [
        "pytest",
        "flake8",
        "black",
        "jedi",
        "ipython"
    ]},
    entry_points='''
        [console_scripts]
        select-pyenv=select_pyenv:cli
    ''',
)
