import configparser

path = '/home/karunakar/PycharmProjects/Dinero_UI_Automation/configurations/config.ini'
config = configparser.RawConfigParser()
config.read(path)


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('commonData', 'url')
        return url
    @staticmethod
    def getApplicationEmail():
        email = config.get('commonData','email')
        return email

    @staticmethod
    def getApplicationPWD():
        pwd = config.get('commonData', 'password')
        return pwd