import logging


class CustomLog:
    def __init__(self, filename:str, level:int):
        self.FileName = filename
        self.Level = level

    def SetUpConfig(self):
        logging.basicConfig(filename=self.FileName,
                            filemode='a',
                            level=self.Level, #logging.DEBUG,
                            format="[WEB.API]: %(asctime)s:%(levelname)s - %(message)s")

