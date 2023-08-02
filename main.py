import discord
from discord.ext import commands
from discord import FFmpegAudio
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

clients = commands.Bot(command_prefix="!",intents = discord.Intents.all())

intents = discord.Intents.default()
intents.members = True

@clients.event
async def on_ready():
    print("The bot is ready")
    print("________________")

@clients.command()
async def hello(ctx):
    await ctx.send("Hello, I am FACC bot")

@clients.event
async def on_member_join(member):
    channel = clients.get_channel(1132445836492685385)
    await channel.send(f"{member.name} has joined the server")

@clients.event
async def on_member_remove(member):
    channel = clients.get_channel(1132445836492685385)
    await channel.send(f"{member.name} left the server")

@clients.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegAudio
    else:
        await channel.send('Error: You must be in a voice channel to run this command')

@clients.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice.clients):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("The bot isn't in a voice channel")
'''
@clients.command()
async def play(ctx, url):
    voice_channel = ctx.author.voice.channel
    voice_client = ctx.voice_client

    if not voice_client:
        await voice_channel.connect()
        voice_client = ctx.voice_client

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']

    voice_client.stop()
    voice_client.play(discord.FFmpegPCMAudio(url2),

'''

@clients.event
async def on_message(message):
    if message.content == "fortnite":
        await message.delete()
        await message.channel.send(f"{message.author.name} likes fortnite")

@clients.command()
async def embed(ctx):
    embed = discord.Embed (title = "Help", url = "https://google.com", description = "Look up your question here^", color = 0x4dff4d)
    await ctx.send(embed = embed)


print("This is a test")

clients.run('MTEzMjQ0MDQxNDQ1Mjk5NDA2OA.G_PBC4.7BGlBpLutaTbRLAyZY8MBypBUCLVABwgrqd34k')


