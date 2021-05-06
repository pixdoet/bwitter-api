# testbuildfirewall is a test build, which is basically
# programmer words for a sandbox. enjoy :)

# this script should not be in the github repo, nor should it be in the hands of
# people unauthorised. As such, this is not free software, and should not be
# treated as such

# Licensing
# Not free software. Do not change any of it unless you are authorised
# Licensing ends :)

# DO NOT use any of this code in the official release unless it's stable.
# This is subject to change, so play with it as much as you want
# DO NOT change the version, changelog and license

# 1.7bf4 (sandbox)

import discord
from discord.ext import commands
# import shotafy # no pedo
import lyrical
# import animefy # need some fixing
# import searchify # we wait until searchify is fixed
import random
import nekos
import serverfy
import randintgenpp as rnd

bot = commands.Bot(command_prefix='fw ')

@bot.event
async def on_ready():
    print('Bot ready')
    await bot.change_presence(activity=discord.Game("This a test build, run fw tester"))
    
@bot.event
async def on_message(message):
    if message.author == bot.user:
        print("Loop")
    if message.content.startswith("firewall"):
        await message.send("The prefix for firewall has changed to fw")
    await bot.process_commands(message)
    print ('Message from {0.author.name} in #{0.channel.name}: {0.content}'.format(message))

# fw say
@bot.command(pass_context=True, aliases = ['say','chickennugget'])
async def chickennuggets(ctx,arg):
    if arg == "":
        await ctx.send("Say something don't leave it blank")
    elif arg == " ":
        await ctx.send("No spaces please")
    else:
        await ctx.send(arg)

#fw ping
@bot.command(pass_context=True, aliases = ['ping','pong'])
async def firewallPing(ctx):
    embedder = discord.Embed(title="Ping", description="", color=0x5ced0e)
    embedder.add_field(name="Pong!", value=':ping_pong: {0} secs'.format(bot.latency, 1))
    await ctx.send(embed=embedder)

#fw contribute
@bot.command(pass_context=True, aliases = ['contribute'])
async def firewallContributeMessage(ctx):
    embedder = discord.Embed(title="Contribute to Firewall!", description="", color=0x5ced0e)
    embedder.add_field(name="Github: ", value="https://github.com/pixdoet/firewall-bot/")
    await ctx.send(embed=embedder)

#fw lyrics
@bot.command(pass_context=True, aliases = ['lyrics'])
async def firewallGetLyrics(ctx,sname,aname):
    embedder = discord.Embed(title="Lyrics of"+sname, description="", color=0x5ced0e)
    lyrics = lyrical.find(sname,aname)
    embedder.add_field(name="Lyrics", value=lyrics)
    await ctx.send(embed=embedder)

#fw kekw
@bot.command(pass_context=True, aliases = ['kekw'])
async def firewallKekw(ctx):
    embedder = discord.Embed(title="KEKW", description="", color=0x5ced0e)
    embedder.set_image(url="https://www.streamscheme.com/wp-content/uploads/2020/07/kekw-emote.jpg")
    await ctx.send(embed=embedder)

#fw WOK
@bot.command(pass_context=True, aliases = ['wok'])
async def firewallWok(ctx):
    await ctx.send("THE KING OF THE WOKS HAS ARRIVED")
    await ctx.send('https://my-test-11.slatic.net/p/3074a0dace3a3e245e25fb4275a3c867.jpg')
    await ctx.send(":WOK::WOK::WOK::WOK::WOK::WOK:")

#fw thomas
@bot.command(pass_context=True, aliases = ['thomas','tomme'])
async def firewallThomas(ctx):
    embedder = discord.Embed(title="Thomas", description="", color=0x5ced0e)
    embedder.add_field(name="Thomas in a nutshell:", value="Why you call Thomas he's gae")
    await ctx.send(embed=embedder)

#fw anime
#@bot.command(pass_context=True, aliases = ['anime'])
#async def firewallAnime(ctx,animeTitle):
    #synopsis = animefy.search(animeTitle)
    #await ctx.send(synopsis)

#fw nooneasked
@bot.command(pass_context=True, aliases = ['nooneasked'])
async def firewallNooneasked(ctx):
    embedder=discord.Embed(title="No one asked", description="", color=0x5ced0e)
    embedder.set_image(url="https://qph.fs.quoracdn.net/main-qimg-468b02bba8c4b3086c3dc7245709a3d6")
    await ctx.send(embed=embedder)

#fw randomsauce
@bot.command(pass_context=True, aliases = ['randomsauce'])
async def firewallRandomsauce(ctx):
    embedder = discord.Embed(title="Random sauce generator", description="", color=0x5ced0e)
    rndsauce = random.randrange(0,350999)
    embedder.add_field(name="Your random sauce:", value=rndsauce)
    await ctx.send(embed=embedder)

#fw mwa
@bot.command(pass_context=True, aliases = ['mwa','mua'])
async def firewallMwa(ctx,whoToMwa):
    await ctx.send("You mwaed :kissing_heart: " + whoToMwa + "!")
    
#fw respects
@bot.command(pass_context=True, aliases = ['f','respects','respect'])
async def firewallRespect(ctx, whoToF):
    await ctx.send("You paid respects[f] to " + whoToF)
    await ctx.send("https://cdn1.dotesports.com/wp-content/uploads/2018/09/08153731/Untitled.png")
    await message.add_reaction(":regional_indicator_f:")

#fw givebrain
@bot.command(pass_context=True, aliases = ['givebrain'])
async def firewallGiveBrain(ctx, whoToGive):
    await ctx.send("You gave your brain :brain: to " + whoToGive)

#fw cry
@bot.command(pass_context=True, aliases = ['cry'])
async def firewallCry(ctx):
    await ctx.send("Boo Hoo Hoo:sob:")
    await ctx.send("https://fsa.zobj.net/crop.php?r=DxAJwethh781KLDbcjIvfG4FEdv3XKovrPPEb7emfvYIe6nikzZfBCeY5re7NFthuz1WUS-S9cLz2hQKCGr6qPoF3QiPJmSsjFSzcD0YfecG0u0dvAoL6o1iekCAOlaJ3nRVS-Hvy3l9BPLs")

#fw sob
@bot.command(pass_context=True, aliases = ['sob'])
async def firewallSob(ctx):
    await ctx.send("Boo Hoo Hoo:sob:")
    await ctx.send("https://i.pinimg.com/originals/2d/78/28/2d78285f218a3692496922c7635c5daf.gif")

#fw racist
@bot.command(pass_context=True, aliases = ['racist'])
async def firewallRacist(ctx):
    await ctx.send("Racism is not cool. No race is better than another, no race is worse than another.")
    await ctx.send("Learn more: https://en.wikipedia.org/wiki/Anti-racism")

#fw pingmeme
@bot.command(pass_context=True, aliases = ['pingmeme'])
async def firewallPingmeme(ctx):
    await ctx.send("Other bots: Ping normally")
    await ctx.send("Firewall: \n **HGDBKHHDCLAMKNVKEFNSNLCJNSLNWDJNCKS**")

#fw google
#@bot.command(pass_context=True, aliases = ['google','search','gsearch'])
#async def firewallSearch(ctx,searchQuery, searchResultsNum):
    #gsearchres = searchify.searchg(searchQuery, searchResultsNum)
    #await ctx.send("Results: \n" + gsearches)

#fw shota
#@bot.command(pass_context=True, aliases = ['gg'])
#async def firewallShota(ctx):
    #shota2send = shotafy.rndshota()
    #await ctx.send(shota2send)
    #await ctx.send("So cute :)")

#fw noshota
@bot.command(pass_context=True, aliases = ['noshota','shota','shotacon'])
async def firewallNoshota(ctx):
    await ctx.send("The shota command has been removed. Fuck shotacons")
    
#fw fuckyou
@bot.command(pass_context=True, aliases=['fuckyou','bung moktar'])
async def firewallFuckyou(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/766933316095574016/816171443636928562/gif.gif")

#fw embed
@bot.command(pass_context=True, aliases=["embed"])
async def firewallEmbed(ctx, ename, etext):
    embedder = discord.Embed(title="The firewall embedder", description="", color=0x0000f0)
    embedder.add_field(name=ename, value=etext, inline=False)
    await ctx.send(embed=embedder)
    
#fw twitter
@bot.command(pass_context=True, aliases=["twitter"])
async def firewallTwitter(ctx):
    embedder = discord.Embed(title="Check out my Twitter!", description="", color=0xffffff)
    embedder.add_field(name="Link to Twitter:", value="https://twitter.com/_hiew_", inline=False)
    await ctx.send(embed=embedder)

#fw neko
@bot.command(pass_context=True, aliases=["catgirl","neko"])
async def firewallNeko(ctx, searchTerm):
    # no embeds until we figure out how to embed images
    sendimg = nekos.img(searchTerm)
    await ctx.send(sendimg)

#fw nkop
@bot.command(pass_context=True, aliases=["nkop","nekohelp"])
async def firewallNekoHelp(ctx):
    gameboy = "'feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo', 'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk', 'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron', 'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar', 'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo', 'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg', 'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom', 'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif', 'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof'"
    await ctx.send(gameboy)

#fw tester
@bot.command(pass_context=True, aliases=["tester"])
async def firewallTester(ctx):
    embedder = discord.Embed(title="Firewall Test Build", description="", color=0x5ced0e)
    embedder.add_field(name="Why do I see the message 'run fw tester'?", value="I don't know")
    await ctx.send(embed=embedder)

#fw random
@bot.command(pass_context=True, aliases=["random","randint"])
async def firewallRandom(ctx):
    genno = rnd.gen()
    embedder = discord.Embed(title="Random Number Generator", description="", color=0x5ced0e)
    embedder.add_field(name="Value:", value=genno)
    await ctx.send(embed=embedder)
    
#fw version
@bot.command(pass_context=True, aliases = ['version','ver'])
async def firewallVersion(ctx):
    embedder = discord.Embed(title="Version", description="", color=0x5ced0e)
    embedder.add_field(name="Firewall version", value="Firewall Helios 1.7bf4(playground)")
    await ctx.send(embed=embedder)

#fw changelog
@bot.command(pass_context=True, aliases = ['changelog'])
async def firewallChangelog(ctx):
    await ctx.send("Full changelog here: https://github.com/pixdoet/firewall-bot/blob/main/firewall-changelog")
    await ctx.send("Firewall Helios 1.7bf4 \n -Temporarily disabled shota command(will re-enable) \n     \n     \n")

#fw license
@bot.command(pass_context=True,aliases=['license'])
async def firewallLicense(ctx):
    embedder = discord.Embed(title="License", description="Licensing for Firewall", color=0x5ced0e)
    embedder.add_field(name="Licensing", value="Firewall  Copyright (C) 2021  Hiew Jun Ian(wok#9607) \n This program comes with ABSOLUTELY NO WARRANTY \n This is free software, and you are welcome to redistribute it under certain conditions")
    await ctx.send(embed=embedder)


TOKEN = ('ODA3MDc0MjIxMTg4MTg2MTEy.YByscQ.s1W4rGUSsMZifU6mB-NPoGIj3NE') # insert your token here
bot.run(TOKEN)
