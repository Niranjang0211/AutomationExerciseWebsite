import configparser
config = configparser.RawConfigParser()

config.read(r"C:\Users\niranjan.m\PycharmProjects\AutomationExerciseWebsite\AutomationExerciseWebsite\Configurations\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url = config.get('commonInfo', 'baseUrl')
        return url

