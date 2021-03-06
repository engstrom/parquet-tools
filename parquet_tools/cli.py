import argparse
from parquet_tools.commands import show, csv, inspect


def main() -> None:
    parser = argparse.ArgumentParser(
        prog='parquet-tootls',
        description='parquet CLI tools'
    )
    subparsers = parser.add_subparsers()
    show.configure_parser(subparsers.add_parser(
        'show',
        help='Show human readble format. see `show -h`',
        description='Show parquet file conent with human readablity.'))
    csv.configure_parser(subparsers.add_parser(
        'csv',
        help='Cat csv style. see `csv -h`',
        description='Cat parquet as csv style.'))
    inspect.configure_parser(subparsers.add_parser(
        'inspect',
        help='Inspect parquet file. see `inspect -h`',
        description='Inspect parquet file.'))

    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
