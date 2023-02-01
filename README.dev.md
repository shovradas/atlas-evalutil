# aTLAS Evaluation Result Utility
> Instruction for future developers

## Prerequisites
- Python 3.9+
- Pip 21+
- Setuptools 56+

Use below command(s) to determine if your environment meets the prerequisites
```bash
python -V                       # Python version
python -m pip -V                # Pip version
python -m pip show setuptools   # Setuptools version
```

## Environment
From terminal navigate to project-root, create and activate the virtual environment
```bash
atlas-evalutil> python -m venv .venv
atlas-evalutil> .venv\Scripts\activate  # Windows
# Or,
atlas-evalutil$ source .venv/bin/activate # UNIX-like
```

## Develop
Install the current project in development mode along with all dependencies.
```bash
(.venv) atlas-evalutil> pip install -e .[test,build]
```
Running the project
```bash
(.venv) atlas-evalutil> atlas-evalutil           # As executable
# Or,
(.venv) atlas-evalutil> python -m atlas.evalutil # As python module
```

## Distribute
To distribute the package run the following command(s)
```bash
(.venv) atlas-evalutil> python setup.py sdist
(.venv) atlas-evalutil> python setup.py bdist_wheel
```

## Commands
Refer to [README.md](./README.md) for available commands.