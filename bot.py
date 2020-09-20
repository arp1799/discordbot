import os
import io
import aiohttp
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands
from settings import *
import youtube_dl

print(DTOKEN)
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')#to be deleted once nodemon work
GUILD = os.getenv('DISCORD_GUILD')#to be deleted once nodemon work

bot=commands.Bot(command_prefix='#')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

#-----------Class+Stuff needed for Playing Music----------
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


#-----------Playing Music------------
@bot.command(name='voice')
async def join_voice(context):
    connected = context.author.voice
    url = context.message.content.strip("#voice ")
    if connected:
        try:
            vc = await connected.channel.connect()
        except:
            pass
        player = await YTDLSource.from_url(url, loop=bot.loop)
        vc.play(player, after=lambda e: disconnect_after_played(context, vc))
        await context.send('Now playing: {}'.format(player.title))
    else:
        response = "Plese join a voice channel first."
        await context.send(response)



#-----------exit command-------------
@bot.command(name='exit',help="exiting bot")
async def exit(context):
    response = "BYE BOIS"
    await context.send(response)
    await bot.logout()

# print(DTOKEN)
bot.run(TOKEN)#TOKEN -> DTOKEN


#------------------GUILD MEMBERS LIST COMMAND------------------------------------
# @bot.command(name='guild')
# async def guild(context):
#     members = '\n - '.join([member.name for member in get_all_members])
#     print(f'Guild Members:\n - {members}')
#-------------------------CLIENT WORKING---------------------------
# client = discord.Client()
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#     guild = discord.utils.get(client.guilds, name=GUILD)
#     print("GUILD",guild)
#     print(
#         f'{client.user} is connected to the following guild:\n'
#         f'{guild.name}(id: {guild.id})'
#     )
#     members = '\n - '.join([member.name for member in guild.members])

#---------------------CLIENT WORK----------------------------------

# @client.event
# async def on_message(message):
#     text = message.content
#     if(text.split()[0] == 'fuck'):
#         if('hitesh' in message.content):
#             response = "LUND"
#             await message.channel.send(response)
#         elif "EXIT" in message.content:
#             response = "BYE BOIS"
#             await message.channel.send(response)
#             await client.logout()
#         elif message.content == 'raise-exception':
#             print(discord.DiscordException)

# client.run(TOKEN)
