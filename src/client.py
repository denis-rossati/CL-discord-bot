import discord
from discord.ext import commands
from random import randint


client = commands.Bot('.')

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    which_ayaya = randint(0, 1)

    if 'ayaya' in message.content.lower():
        natural_typing = randint(2, 7)
        letter_a = 'a' * natural_typing
        ayaya = 'ayay' + letter_a

        print(natural_typing % 2)
        if (natural_typing % 2) >= 1:
            ayaya = ayaya.upper()

        if which_ayaya == 0:
            await message.channel.send(ayaya)

        if which_ayaya == 1:
            await message.reply(ayaya)