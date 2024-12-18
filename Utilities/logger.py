import logging

class logclass:
    def getthelogs(self):

        logger = logging.getLogger()
        filehandler = logging.FileHandler("Logs\\logfile.log",mode="w") #mode="w" is used to remove previous logs and insert new
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)#logging.DEBUG is used to set level in which below level logs will not be logged.
        return logger