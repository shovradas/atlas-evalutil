import inspect
from pathlib import Path
import matplotlib.pyplot as plt

from atlas.evalutil import data
from atlas.evalutil import validators
from atlas.evalutil.color_utils import generate_gradient_colors
from atlas.evalutil.config_handler import config
from atlas.evalutil.unit_utils import TimeUnit, MemoryUnit, time_factor, memory_factor
from atlas.evalutil.export_utils import ExportFormat


class CommandBase:
    def __init__(self, args: dict) -> None:
        self.args: dict = args
  
    def execute(self, action) -> None:
        method = getattr(self, action)
        parameter_names = inspect.signature(method).parameters
        parameters = {name: self.args[name] for name in parameter_names}
        method(**parameters)


class ScenarioCommand(CommandBase):
    def __init__(self, args: dict) -> None:
        super().__init__(args)
        validators.validate_input_directory()

    def list(self, export: bool=False):
        scenarios = data.get_scenarios()
        header = 'SCENARIOS'

        row_width = len(max([header, *scenarios], key=len))
        border = lambda : f"+ {''.ljust(row_width, '-')} +"
        row = lambda x: f"| {x.ljust(row_width)} |"

        output = "{border}\n{header}\n{border}\n{rows}\n{border}".format(
            border=border(),
            header=row(header),
            rows = '\n'.join([row(scenario) for scenario in scenarios]),
        )

        print(output)
        
        if export:
            Path(config.OUTPUT_DIR).mkdir(parents=True, exist_ok=True)
            file = open(f"{config.OUTPUT_DIR}/scenarios.txt", 'w')
            file.write(output)
            file.close()


class ChartCommand(CommandBase):
    def __init__(self, args: dict) -> None:
        super().__init__(args)
        validators.validate_input_directory()

    def time_usage(self, time_unit: TimeUnit, memory_unit: MemoryUnit, export: bool=False, export_format=ExportFormat.SVG) -> None:
        # get data
        time_usage = data.get_time_usage()
        scenario_sizes = data.get_scenario_sizes()

        # scaling
        time_usage = time_usage / time_factor(time_unit)
        scenario_sizes = scenario_sizes / memory_factor(memory_unit)
        time_usage = time_usage.divide(scenario_sizes['size'], axis='index').dropna(axis='index')

        # Formatting
        time_usage.sort_index(key=lambda x: x.str.lower().str.len(), axis='index', inplace=True)
        time_usage.sort_index(key=lambda x: x.str.lower().str.len(), axis='columns', inplace=True)
        time_usage.columns = time_usage.columns.str.replace('_', ' ').str.title()

        color_iterator = generate_gradient_colors(skip=3)
        # display and/or save
        time_usage.plot(
            figsize=(12, 8),
            rot=45,
            title=f"Scenario vs Time usage per size",
            xlabel="Scenario Names",
            ylabel=f"Time ({time_unit.value}) / Size ({memory_unit.value})",
            xticks=range(time_usage.index.size),
            linewidth=2,
            color={col: next(color_iterator) for col in sorted(time_usage.columns)}
        )
        plt.tight_layout(pad=4)

        if export:
            Path(config['output_dir']).mkdir(parents=True, exist_ok=True)
            export_path = f"{config['output_dir']}/time_usage.{export_format.value}"
            plt.savefig(export_path)
            print(f"Time usage chart exported at {Path(export_path).absolute().as_uri()}")

        plt.show()

    def memory_usage(self, time_unit: TimeUnit, memory_unit: MemoryUnit, export: bool=False, export_format=ExportFormat.SVG) -> None:
        # get data
        memory_usage = data.get_memory_usage()    

        # scaling
        memory_usage = memory_usage / memory_factor(memory_unit)
        memory_usage.index = memory_usage.index / time_factor(time_unit)

        # formatting
        memory_usage.sort_index(key=lambda x: x.str.lower().str.len(), axis='columns', inplace=True)
        memory_usage = memory_usage[memory_usage.columns[::-1]]

        color_iterator = generate_gradient_colors()
        # display and/or save
        memory_usage.plot(
            figsize=(12, 8),
            title=f"Time vs Memory usages",
            xlabel=f"Time ({time_unit.value})",
            ylabel=f"Memory Usage ({memory_unit.value})",
            linewidth=2,
            color={col: next(color_iterator) for col in memory_usage.columns}          
        )
        plt.tight_layout(pad=4)
        
        if export:
            Path(config['output_dir']).mkdir(parents=True, exist_ok=True)        
            export_path = f"{config['output_dir']}/memory_usage.{export_format.value}"
            plt.savefig(export_path)
            print(f"Memory usage chart exported at {Path(export_path).absolute().as_uri()}")

        plt.show()


class ConfigCommand(CommandBase):
    def list(self) -> None:
        for key, value in config.items():
            print(f"{key} = {value}")

    def set(self, pairs) -> None:
        updated = {}
        for key, value in pairs:
            config[key] = value
            updated.update({key: value})
        
        config.save()
        print("Configuration updated for:", *[f"{k} = {v}" for k, v in updated.items()], sep='\n')

    def get(self, key:str) -> None:
        if key not in config:
            print(f"'{key}' is not a valid configuration key")
            return
        print(f"{key} = {config[key]}")

    
    def reset(self, key) -> None: 
        config.pop(key)
        config.save()
        print(f"Configuration for {key} is restored")
