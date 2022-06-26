import discord
from dotenv import load_dotenv

load_dotenv()

class Bot(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        print('Messaage from {0.author}: {0.content}'.format(message))
        if 'ayaya' in message.content.lower():
            await message.channel.send('AYAYAAA')
