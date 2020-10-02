from bot import telegram_bot
update_id = None
from google-search import search
bot = telegram_bot("config.cfg")
def make_reply(msg):
	if msg is not None :
		reply = list(search(msg, tld="co.in", num=10, stop=3, pause=1))
		return reply

while True:
	print("...")
	updates = bot.getupdates(offset=update_id)
	updates = updates["result"]
	
	if updates:
		for item in updates:
			update_id = item["update_id"]
			try:
				message = item["message"]["text"]
			except:
				message = None
			now = item["message"]["from"]["id"]
			reply = make_reply(message)
			bot.sendmessage(reply,now)
