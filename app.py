import argparse
import logging
from src.application.app_dash import AppDash
from src.application.app_ingestion import AppIngestion
from src.application.app_processing import AppProcessing

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(message)s')

ch.setFormatter(formatter)
logger.addHandler(ch)

APPS = {
    "ingestion": AppIngestion.run,
    "process": AppProcessing.run,
    "dash": AppDash.run
}


def main():
    parser = argparse.ArgumentParser(
        description='Painel de repositórios do GitHub.')
    parser.add_argument(
        "-p",
        dest="process",
        choices=['ingestion', 'process', 'dash'],
        type=str,
        help='Escolha entre uma das opições [ingestion, process, dash]')

    args = parser.parse_args()

    if args.process is not None:
        app_run = APPS.get(args.process)
        app_run()


if __name__ == '__main__':
    main()
