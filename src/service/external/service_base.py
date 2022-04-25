from email import header
import requests

from src.settings import GITHUB


class ServiceBase():

    def _request(self, **kwargs):
        response = requests.get(
            kwargs.get("url"),
            params=kwargs.get("params"),
            headers=kwargs.get("headers"),
            auth=(GITHUB['USER'], GITHUB['AUTH_KEY'])
        )

        return response.json() if response.text else None
