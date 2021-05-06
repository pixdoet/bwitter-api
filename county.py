# sauce code for count.py

import discord
import time

TOKEN = ('ODA3MDc0MjIxMTg4MTg2MTEy.YByscQ.v4y7WKDF6BpfWDulGNFXgibnzCc') # token
client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready")
    a = 0
    running = True
    while running:
        channel = client.get_channel(816508594555715604)
        await channel.send(a)
        a += 1
        time.sleep(0.5)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msgChId = message.channel.id
    print(msgChId)


client.run(TOKEN)
