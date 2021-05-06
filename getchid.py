import discord

TOKEN = ('ODA3MDc0MjIxMTg4MTg2MTEy.YByscQ.s1W4rGUSsMZifU6mB-NPoGIj3NE')
client = discord.Client()

@client.event
async def on_ready():
    print("Bot ready")
    a = 0
    running = False
    while running:
        channel = client.get_channel(811828775771308053)
        await channel.send(a)
        a += 1

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msgChId = message.guild.id
    print(msgChId)


client.run(TOKEN)
