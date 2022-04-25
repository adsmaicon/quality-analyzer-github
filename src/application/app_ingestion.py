""" ingestão de dados
"""
import json
from time import sleep
from src.application.app_base import AppBase
from src.domain.ingestion import Ingestion
from src.service.queue.queue import Queue
from src.settings import QUEUE, GENERAL


class AppIngestion(AppBase):
    """ Classe responsavel por buscar dados
    """

    @staticmethod
    def run():
        """Metodo resposavel por executar a ação
        """
        queue = Queue(QUEUE["QUEUE_NAME"])
        ingestion = Ingestion()

        while True:
            data_repos = ingestion.fetch_data()

            for data in data_repos:
                queue.send_message(json.dumps(data.__dict__))

            if GENERAL["APP_ENV"] == "TEST":
                break

            sleep(300)
