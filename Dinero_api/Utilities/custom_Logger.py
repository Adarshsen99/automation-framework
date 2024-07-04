
import logging


class LogGen():

    @staticmethod
    def loggen():
        path = '/home/karunakar/DineroQa/Dinero_api/logs/logs_API.log'

        logger = logging.getLogger()
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler = logging.FileHandler(path)
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger