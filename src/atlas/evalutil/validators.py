import os
from pathlib import Path
from atlas.evalutil.config_handler import config


def validate_input_directory():
    input_dir = Path(config['input_dir'])
    if not input_dir.exists():
        print(f"Input directory '{input_dir.absolute()}' does not exist.")
        exit(1)

    _, dirs, files = next(os.walk(input_dir))
    expected_dirs = ['evaluator_results']
    expected_files = ['scenario_sizes.csv']

    missing_dirs = [d for d in expected_dirs if d not in dirs]   
    missing_files = [f for f in expected_files if f not in files]

    if missing_dirs or missing_files:
        print("Input directory is not valid. Please check the following:")
        if missing_dirs: print(f"Missing directories: {missing_dirs}")
        if missing_files: print(f"Missing files: {missing_files}")
        exit(1)