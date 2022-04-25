import logging


def Loggin(func):

    def wrapper(*args) -> list:
        result = func(*args)

        for r in result:
            logging.info(r.__dict__)

        return result

    return wrapper
