from setuptools import setup, find_namespace_packages

setup(
    name='atlas_evalutil',
    version='1.0.0',
    author='Shovra Das',
    author_email = "shovradas@gmail.com",
    description='aTLAS Evaluation Result Utility',
    long_description=open('README.md').read(),
    python_requires='>=3.9, <4',
    package_dir={'': 'src'},
    packages=find_namespace_packages(
        include=['atlas.*'],
        where='src'
    ),
    install_requires=[
        'matplotlib==3.6.2',
        'pandas==1.5.2',
        'tomlkit==0.11.6',
        'pingouin==0.5.3'
    ],
    extras_require={
        'test': ['pytest==7.2.0'],
        'build': ['wheel==0.38.4']
    },
    entry_points={
        'console_scripts': [
            'atlas-evalutil=atlas.evalutil.cli:main'
        ]
    }
)