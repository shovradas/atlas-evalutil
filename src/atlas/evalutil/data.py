import glob
from importlib.machinery import SourceFileLoader
from pathlib import Path

import pandas
from pandas import DataFrame

from atlas.evalutil.config_handler import config


def get_evaluator_results(keys: list[str], scenario_name:str = '') -> DataFrame:
    data = []
    directory = f"{config['input_dir']}/evaluator_results"
    for file in glob.glob(f"{directory}/*.py"):
        module = SourceFileLoader(Path(file).stem, file).load_module()

        # Filter by scenario name if specified
        if scenario_name and scenario_name != module.SCENARIO_NAME: continue
        
        item = {key.lower(): getattr(module, key.upper()) for key in keys}
        data.append(item)

    return DataFrame(data)


def get_scenario_sizes() -> DataFrame:
    data_frame = pandas.read_csv(f"{config['input_dir']}/scenario_sizes.csv", names=['scenario_name', 'size'])
    data_frame.index = data_frame.pop('scenario_name')
    return data_frame


def get_scenarios() -> list[str]:    
    data_frame = get_evaluator_results(['scenario_name'])
    return sorted(data_frame['scenario_name'].unique(), key=lambda x: len(x.lower()))


def get_time_usage() -> DataFrame:
    data_frame = get_evaluator_results(['scenario_name', 'atlas_times'])

    data_frame = data_frame.join(DataFrame(data_frame.pop('atlas_times').values.tolist()))
    data_frame = data_frame.groupby("scenario_name").mean()    

    return data_frame


def get_memory_usage() -> DataFrame:
    data_frame = get_evaluator_results(['scenario_name', 'ram_usages'])

    data_frame = data_frame.join(DataFrame(data_frame.pop('ram_usages').values.tolist()))

    data_frame = data_frame.apply(  # Add time label to memory usages
        lambda row: row.apply(
            lambda col: {k:v for k,v in enumerate(col, start=1)} if type(col)==list else col
        )
    )

    scenario_groups = data_frame.groupby(by='scenario_name')    
    data_frame = pandas.DataFrame()
    for scenario_name, scenario_group in scenario_groups:
        # scenario_name = '10x10'
        # scenario_group = scenario_groups.get_group(scenario_name)
        scenario_group = scenario_group.dropna(axis='columns')                  # example: scenario 10x10 has 10 host only. therefore dropping 7 columns incase of 17 hosts
        scenario_group = scenario_group.drop(columns=['scenario_name'])
        scenario_group = pandas.concat([DataFrame(scenario_group[c].tolist()).T for c in scenario_group.columns])
        scenario_group.dropna(axis='index', inplace=True)                       # some host might take more seconds for the same scenario in different runs. therefore keeping those extra rows out of the average

        
        scenario_group = scenario_group.groupby(scenario_group.index).mean()
        series = scenario_group.mean(axis='columns')

        data_frame[scenario_name] = series    

    return data_frame


def get_memory_usage_anova() -> DataFrame:
    data_frame = get_evaluator_results(['scenario_name', 'ram_usages'])

    data_frame = data_frame.join(DataFrame(data_frame.pop('ram_usages').values.tolist()))

    data_frame = data_frame.apply(  # Add time label to memory usages
        lambda row: row.apply(
            lambda col: {k:v for k,v in enumerate(col, start=1)} if type(col)==list else col
        )
    )

    print(data_frame)

    scenario_groups = data_frame.groupby(by='scenario_name')    
    data_frame = pandas.DataFrame()
    for scenario_name, scenario_group in scenario_groups:
        # scenario_name = '10x10'
        # scenario_group = scenario_groups.get_group(scenario_name)
        print(scenario_group)
        
        scenario_group = scenario_group.dropna(axis='columns')                  # example: scenario 10x10 has 10 host only. therefore dropping 7 columns incase of 17 hosts
        scenario_group = scenario_group.drop(columns=['scenario_name'])
        scenario_group = pandas.concat([DataFrame(scenario_group[c].tolist()).T for c in scenario_group.columns])
        print(scenario_group)
        scenario_group.dropna(axis='index', inplace=True)                       # some host might take more seconds for the same scenario in different runs. therefore keeping those extra rows out of the average

        print(scenario_group)        
        scenario_group = scenario_group.groupby(scenario_group.index).mean()
        series = scenario_group.mean(axis='columns')
        print(scenario_group)

        data_frame[scenario_name] = series
        break

    print(data_frame)

    return data_frame