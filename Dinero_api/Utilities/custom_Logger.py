
import logging


class LogGen():

    @staticmethod
    def loggen():
        path = '/home/karunakar/PycharmProjects/Dinero_API/logs/logs_API.log'

        logger = logging.getLogger()
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(path)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger