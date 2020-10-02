import requests
import json
import configparser as cfg
class telegram_bot():
    def __init__(self,config):
        self.token = self.read_token_from_config_file(config)
        self.base = f" https://api.telegram.org/bot{self.token}/"
        def getupdates(self, offset = None ):
        	url = self.base + "/getupdates?timeout=100"
        	if offset:
        		url = url + f"offset{offset+1}"
        	r = requests.get(url)
        	return json.loads(r.content)
    def sendmessage(self,msg,chat_id):
     	url = self.base + f"sendmessage?chat_id={chat_id}&text={msg}"
     	if msg is not None:
     		requests.get(url)
    def read_token_from_config_file(self,configg):
      	x = cfg.cofnfigparser()
      	x.read(config)
      	return x.get('creds','token')



