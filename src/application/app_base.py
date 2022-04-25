"""_summary_
"""
from abc import ABC, abstractmethod


class AppBase(ABC):
    """_summary_
    """

    @staticmethod
    @abstractmethod
    def run():
        """_summary_
        """
        raise NotImplementedError
