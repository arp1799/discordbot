# bot.py
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




bot=commands.Bot(command_prefix='#')

@bot.command(name='guild')
async def guild(context):
    members = '\n - '.join([member.name for member in get_all_members])
    print(f'Guild Members:\n - {members}')

@bot.command(name='randomimage',help='input image link to share with other members')
async def webimage(context,my_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(my_url) as resp:
            if resp.status != 200:
                return await context.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await context.send(file=discord.File(data, 'cool_image.png'))
    
@bot.command(name='image')
async def image(context):
    await context.send(file=discord.File('my_file.png'))

@bot.command(name='hitesh',help="roast hitesh bhudania member of fb&cl")
async def temp(context):
    response="LUND"
    await context.send(response)

@bot.command(name='hitesh_mul',help="mul facts about hitesh bhudania")
async def facts(context,times:int):
    words=['LUND:yeh aisa fact jispe kisi ko bhi shk nhi',
    'Tinder account controlled by yudhveer',
    'Bhudania ki randi:yuvi',
    'only knows two things :Yeah and XD(matlab mt puchna usse lekin)',
    'senior recuriter /chairman at hitesh Honda',
    'kaun hai kha se aaya abhi yeh kisi ko nhi pta',
    'rohit,yuvi,hitesh inn teeno ki bhaut complex relation hai aaps mein kuan kiska baap yeh teeno ko nhi pta']
    if(times>3 or times<=0):
        await context.send("abhi explore kr rhe hai apni aukat 1-3 facts ki hai")
    else:
        #response=random.choices(words,k=3)
        n = [i for i in range(7)]
        response = ''
        for i in range(3):
            x = random.randint(0,len(n)-1)
            response+=words[n[x]]+'\n'
            del n[x]
        await context.send(response)

@bot.command(name='exit',help="exiting bot")
async def exit(context):
    response = "BYE BOIS"
    await context.send(response)
    await bot.logout()

#-------------------------------------------------------nsfw------------------------------------------

@bot.command(name='boobies',help='as the name suggests')
async def boobies(context):
    boobies=[
        
    ]
    res=random.choice(boobies)
    async with aiohttp.ClientSession() as session:
        async with session.get(res) as resp:
            if resp.status != 200:
                return await context.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await context.send(file=discord.File(data, 'cool_image.png'))


bot.run(TOKEN)

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