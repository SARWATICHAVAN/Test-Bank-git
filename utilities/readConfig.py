import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfigfile:

    @staticmethod
    def GetUser():
        User = config.get(section='login data', option='user')
        return User

    @staticmethod
    def GetPass():
        Passw = config.get(section='login data', option='passw')
        return Passw

    # @staticmethod
    # def GetUsername():
    #     Username = config.get(section='signup data', option='username')
    #     return Username
    #
    # @staticmethod
    # def GetPassword():
    #     Password = config.get(section='signup data', option='password')
    #     return Password
    #
    # @staticmethod
    # def GetEmail():
    #     Email = config.get(section='signup data', option='email')
    #     return Email
    #
    # @staticmethod
    # def GetPhone():
    #     Phone = config.get(section='signup data', option='phone')
    #     return Phone
