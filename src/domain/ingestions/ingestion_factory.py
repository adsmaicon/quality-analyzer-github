from src.domain.ingestions.github_ingestion import GithubIngestion
from src.domain.ingestions.type_ingestion import TypeIngestion


class IngestionFactory():

    @staticmethod
    def ingestion(type: TypeIngestion):
        if type == TypeIngestion.GITHUB:
            return GithubIngestion()