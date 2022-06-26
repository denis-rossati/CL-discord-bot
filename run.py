import os
from src import Client

bot = Client.Bot()
bot.run(os.environ.get('TOKSON'))