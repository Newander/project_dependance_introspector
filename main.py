from pathlib import Path

from tree import Parser

if __name__ == '__main__':
    mac_dir = '/Users/sergeygavrilov/PycharmProjects/ids_fssp'
    venv_dir = '/home/newander/PycharmProjects/etl_scheduler/dags'

    project = Path(venv_dir)
    report_dest = Path.cwd() / 'result.csv'

    parser = Parser(project)
    parser.extract_tree()
    parser.build_tree()

    print(parser)
    parser.root.modules[7].get_imports()
    # parser.create_report(report_dest)