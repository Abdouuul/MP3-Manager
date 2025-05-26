import configparser
import os
import sys
import pyodbc

# Determine the absolute path to the project root directory
# __file__ is the path to app_config.py.
# If app_config.py is in Config/, then its dirname is Config/, and dirname of that is the project root.
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construct the absolute path to the config.ini file
CONFIG_INI_PATH = os.path.join(PROJECT_ROOT, 'Config', 'config.ini')
LOCAL_CONFIG_INI_PATH = os.path.join(PROJECT_ROOT, 'Config', 'config.local.ini')



def load_config():
    """Loading configuration from the Config.ini and returning the API_key"""
    config = configparser.ConfigParser()

    # Checking if the config file is created
    if not os.path.exists(CONFIG_INI_PATH):
        raise Exception('The config.ini file doesn\'t exist')
        sys.exit(1)    
    config.read(CONFIG_INI_PATH)

    if not os.path.exists(LOCAL_CONFIG_INI_PATH):
        raise Exception('The config.local.ini file doesn\'t exist')
        sys.exit(1)
    config.read(LOCAL_CONFIG_INI_PATH)

    try:
        API_KEY = config['API']['API_KEY']
        DATABASE_URL = config['API']['Database_URL']
        API_URL = config['API']['API_URL']

    except KeyError:
        raise ('Unable to get the information from config file')

    if not API_KEY:
        raise ValueError('API_KEY has value ', API_KEY)
        sys.exit(1)
    
    return API_KEY, DATABASE_URL, API_URL

#Get the API_KEY and DATABASE_URL from load_config
API_KEY, DATABASE_URL, API_URL = load_config()


class Config:
    SQLALCHEMY_DATABASE_URI =(DATABASE_URL)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

