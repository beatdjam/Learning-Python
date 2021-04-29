import os

from googleads import ad_manager

script_dir = os.path.dirname(__file__)
CONFIG_FILE = os.path.join(script_dir, '../googleads.yaml')


class GoogleAdManagerClient:
    __client = None

    def __new__(cls, *args, **kwargs):
        if cls.__client is None:
            cls.__client = ad_manager.AdManagerClient.LoadFromStorage(CONFIG_FILE)
        return cls.__client
