import logging

class LogGeneration:

    @staticmethod
    def logGen():
        #logging.basicConfig()
        logging.basicConfig(filename=r".\\Logs\\automation.log",
                            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
                            ,datefmt='%m/%d/%y %I:%M:%s %p')
        logger=logging.getLogger("automationLogger")
        logger.setLevel(logging.INFO)
        return logger