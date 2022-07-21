import asyncio
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from random import randint


# CHANGE THIS TO YOUR FFMPEG PATH 
ffmpeg = "C:/ffmpeg/bin/ffmpeg.exe"
client = commands.Bot('.')

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client.user))


@client.event
async def on_message(message):
    # Detects if the author is a bot instead of itselfs
    if message.author.bot:
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

        # Entering in a voice chat
        if message.author.voice:

            # Detectes if its already connected to a voice chat
            if not client.voice_clients:
                channel = await message.author.voice.channel.connect()

            # Gets the voice channel as "channel"
            else:
                channel = client.voice_clients

            channel.play(FFmpegPCMAudio(executable=ffmpeg, source="sounds/Ayaya.mp3"), after= lambda e: asyncio.run_coroutine_threadsafe(channel.disconnect(),client.loop))