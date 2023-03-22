import requests
import random
import sys
import os
from help.user_agents import UserAgent
from help.banner import colors
import logging






class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s ')

logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)


user_agent = UserAgent().random()

class request:

    def __init__(self , url):
        self.url = url
        self.session = requests.Session()
    
    def Get_banner(self):
        logging.info(colors.green + " Get from  %s" , self.url)

    
    def Post_banner(self):
        logging.info(colors.green + "posting To  %s" , self.url)


    def get(self , url , timeout=None , headers=None):
        self.Get_banner()
        return self.session.get(url , headers={'User-Agent': user_agent})


    def post(self , url , data=None , json=None , files=None , timeout=None , headers=None):
        self.Post_banner()
        return self.session.post(url , data=data , headers={'User-Agent': user_agent})
    



