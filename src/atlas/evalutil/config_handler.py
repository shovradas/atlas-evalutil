import pkg_resources, tomlkit
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Union


DEFAULT_CONFIG = {
    'input_dir': 'data/input',
    'output_dir': 'data/output'
}


class ConfigFileHandler(ABC):
    @abstractmethod
    def read(path: Union[str, Path]) -> Dict:
        pass
    @abstractmethod
    def write(config: Dict, path: Union[str, Path]):
        pass


class TomlConfigFileHandler(ConfigFileHandler):
    def read(self, path: Union[str, Path]) -> Dict:
        if not (path := Path(path)).exists():
            raise FileNotFoundError(f"File not found at: '{path.absolute().as_uri()}'.")
        return tomlkit.parse(path.read_text())

    def write(self, config: Dict, path: Union[str, Path]) -> None:
        if not (path := Path(path)).exists():
            raise FileNotFoundError(f"File not found at: '{path.absolute().as_uri()}'.")
        path.write_text(tomlkit.dumps(config))


class ConfigValidator:
    def __init__(self, reference_config) -> None:
        self.reference_config = reference_config

    def validate(self, config: Dict):
        configurables = list(self.reference_config.keys())
        for key in config:
            if key in configurables: continue   # TODO: Check multilevel keys
            raise KeyError(f"Invalid key '{key}'.")


class Config(dict):
    def __init__(self, default_config, file_handler, config_validator, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.default_config = default_config
        self.file_handler = file_handler
        self.config_validator = config_validator

        self.leveled_paths = []
        self.top_level_config = None
        self.top_level_path = None
        
        self.reference_config = None

    def append_path(self, path: Union[str, Path]):
        self.leveled_paths.append(Path(path))

    def load(self):
        self.update(self.default_config)
        for path in self.leveled_paths:
            if not path.exists(): continue

            try:
                leveled_config = self.file_handler.read(path)
                self.config_validator.validate(leveled_config)
            except KeyError as e:
                raise Exception(f"{e}\nFile at: '{path.absolute().as_uri()}'.")

            self.top_level_config, self.top_level_path = leveled_config, path
            self.update(leveled_config)

        self.reference_config = self.copy()

    def reload(self):
        self.clear()
        self.load()

    def save(self):
        for key in self.reference_config:
            if key not in self:
                self.top_level_config.pop(key)
                continue
            if self[key] == self.reference_config[key]: # TODO: Check multilevel keys
                continue
            self.top_level_config[key] = self[key]

        try:
            self.config_validator.validate(self.top_level_config)
        except KeyError as e:
            raise Exception(f"Error while saving: {e}")

        self.file_handler.write(self.top_level_config, self.top_level_path)


config = Config(DEFAULT_CONFIG, TomlConfigFileHandler(), ConfigValidator(DEFAULT_CONFIG))
file_name = 'atlas-evalutil.toml'
config.append_path(Path(pkg_resources.resource_filename(__name__, '')) / file_name)    # Global: Package directory
config.append_path(Path.home() / file_name)                                            # User  : User home directory
config.append_path(file_name)                                                          # Local : Working directory
config.load()