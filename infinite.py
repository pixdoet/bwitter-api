# quick script i whipped up just to test the embed function
# using lyrical as a test subject
import discord
from discord.ext import commands
import lyrical

TOKEN = ('ODA3MDc0MjIxMTg4MTg2MTEy.YByscQ.v4y7WKDF6BpfWDulGNFXgibnzCc')

bot = commands.Bot(command_prefix='ebt ')
@bot.event
async def on_ready():
    print("FW infinite ready")

@bot.command(pass_context=True, aliases = ['lol'])
async def firewallEmbedderTest(ctx, song, artist):
    songly = lyrical.find(song, artist)
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Lyrics", value=songly, inline=False)
    await ctx.send(embed=embedVar)

bot.run(TOKEN)
