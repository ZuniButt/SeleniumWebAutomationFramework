import inspect
import logging


class loggingParentClass:

    def getLogger(self):
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        fileHandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # This is the basic market level log file format. It can be changed.
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)  # set level is use to set the starting point of the logging file execution. if level is set as error then all error file and critical files will be executed and remaining two will be skipped.
        return logger




