import sys
from argparse import ArgumentParser, Namespace

from atlas.evalutil.commands import ScenarioCommand, ChartCommand, ConfigCommand
from atlas.evalutil.export_utils import ExportFormat
from atlas.evalutil.unit_utils import TimeUnit, MemoryUnit
from atlas.evalutil.config_handler import config


def build_parser():
    parser = ArgumentParser(prog='atlas-evalutil', description='aTLAS Evaluation Result Utility')
    parser.set_defaults(parser=parser, Command=None, action=None)
    parser.add_argument('--config-file', '-c', type=str, help='custom config file')

    subparsers = parser.add_subparsers()

    # common arguments for scenario and chart commands
    common_parser = ArgumentParser(add_help=False)
    common_parser.add_argument('--input-version', '-v', type=str, help=f"specifies input version to use if available inside input directory (example: v0, v1 etc.)")
    common_parser.add_argument('--input-dir', '-i', type=str, help=f"read inputs from specified directory (default: {config['input_dir']})")
    common_parser.add_argument('--output-dir', '-o', type=str, help=f"save outputs into specified directory (default: {config['output_dir']})")
    common_parser.add_argument('--export', '-e', action="store_true", default=False, help=f"save outputs into output directory")
    common_parser.add_argument('--export-format', '-f', type=ExportFormat, default=ExportFormat.SVG, help=f"format of exported chart within {{{', '.join([e.value for e in ExportFormat])}}} (default: {ExportFormat.SVG.value})")

    # scenario command
    scenario_parser = subparsers.add_parser('scenario', aliases=['s'], parents=[common_parser], description='Scenario Command', help='evaluated scenario details')
    scenario_parser.set_defaults(parser=scenario_parser, Command=ScenarioCommand, action='list')

    # chart command
    chart_parser = subparsers.add_parser('chart', aliases=['c'], parents=[common_parser], description='Chart Command', help='evaluation charts')    
    chart_parser.set_defaults(parser=chart_parser, Command=ChartCommand)
    group = chart_parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--time-usage', '-t', dest='action', action="store_const", const='time_usage', help='displays chart for time usage')
    group.add_argument('--memory-usage', '-m', dest='action', action="store_const", const='memory_usage', help='displays chart for ram usage')
    chart_parser.add_argument('--memory-unit', '-mu', type=MemoryUnit, required=False, default=MemoryUnit.MEGABYTE, help=f"unit of ram usage in {{{', '.join([e.value for e in MemoryUnit])}}} (default: {MemoryUnit.MEGABYTE.value})")
    chart_parser.add_argument('--time-unit', '-tu', type=TimeUnit, required=False, default=TimeUnit.SECOND, help=f"unit of time in {{{', '.join([e.value for e in TimeUnit])}}} (default: {TimeUnit.SECOND.value})")

    # config command
    config_parser = subparsers.add_parser('config', description='Config Command', help='config management')
    config_parser.set_defaults(parser=config_parser, Command=ConfigCommand)
    
    group = config_parser.add_mutually_exclusive_group()
    group.add_argument('--list', '-l', dest='action:list', action='store_true', help='display all configs')
    group.add_argument('--set', '-s', dest='action:set:pairs', type=lambda x: x.split("="), nargs='+', metavar='key=value', help='set config value')
    group.add_argument('--get', '-g', dest='action:get:key', metavar='key', help='display config value')
    group.add_argument('--reset', '-r', dest='action:reset:key', metavar='key', help='reset config value')

    return parser


def resolve_action(args: dict) -> None:
    if action:=args.pop('action') : return action

    # try parsing actions from options in case of action
    # is not specified by parser(s) or needs to be overridden by an option
    # expected format: "action:<action_name>:[parameter_name]"
    for arg in list(args.keys()):
        if not arg.startswith('action'): continue
        if not (value:=args.pop(arg)): continue
        _, action, parameter = (arg.split(':') + [None])[:3] # parameter=None incase of boolean action
        if parameter: args[parameter] = value
        return action


def override_config(args: dict):
    if path := args.pop('config_file'):
        config.append_path(path)
        config.reload()

    if 'input_version' in args and args['input_version']:
        config['input_dir'] = f"{config['input_dir']}/{args['input_version']}"
        config['output_dir'] = f"{config['output_dir']}/{args['input_version']}"


def main():
    parser = build_parser()
    args:Namespace = parser.parse_args() #;print(args); exit(1)
    args:dict = vars(args)
    
    override_config(args)
    
    parser, Command = args.pop('parser'), args.pop('Command')
    action = resolve_action(args)
    if Command and action:
        Command(args).execute(action)
    else:
        parser.print_help()


if __name__ == "__main__":
    sys.exit(main())