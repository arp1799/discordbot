import os
import io
import aiohttp
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot=commands.Bot(command_prefix='#')

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

#-----------exit command-------------
@bot.command(name='exit',help="exiting bot")
async def exit(context):
    response = "BYE BOIS"
    await context.send(response)
    await bot.logout()


bot.run(TOKEN)


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
