import configparser

path = '/home/karunakar/DineroQa/Dinero_automation/configurations/config.ini'
config = configparser.RawConfigParser()
config.read(path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonData', 'url')
        return url
    @staticmethod
    def getApplicationUsername():
        email = config.get('commonData','username')
        return email

    @staticmethod
    def getApplicationPWD():
        pwd = config.get('commonData', 'password')
        return pwd