
from src.domain.ingestions.ingestion_factory import IngestionFactory
from src.domain.ingestions.type_ingestion import TypeIngestion
from src.infra.cross_cutting.loggin import Loggin


class Ingestion():

    def __init__(self) -> None:
        self.__ingestion = IngestionFactory.ingestion(TypeIngestion.GITHUB)

    @Loggin
    def fetch_data(self):
        return self.__ingestion.fetch_data()
