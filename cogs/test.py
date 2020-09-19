import io
import aiohttp
import discord
import random
from discord.ext import commands

class Test(commands.Cog):#Bot is passed as parameter as commands.Cogs 
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='rimage',help='input image link to share with other members')
    async def webimage(self,context,my_url):
        async with aiohttp.ClientSession() as session:
            async with session.get(my_url) as resp:
                if resp.status != 200:
                    return await context.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await context.send(file=discord.File(data, 'cool_image.png'))


    @commands.command(name='image')
    async def image(self,context):
        await context.send(file=discord.File('my_file.png'))

    @commands.command(name='hitesh',help="roast hitesh bhudania member of fb&cl")
    async def temp(self,context):
        response="LUND"
        await context.send(response)

    @commands.command(name='hitesh_mul',help="mul facts about hitesh bhudania")
    async def facts(self,context,times:int):
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

    

    #-------------------------------------------------------nsfw------------------------------------------

    @commands.command(name='boobies',help='as the name suggests')
    async def boobies(self,context):
        boobies=[
            
        ]
        res=random.choice(boobies)
        async with aiohttp.ClientSession() as session:
            async with session.get(res) as resp:
                if resp.status != 200:
                    return await context.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                await context.send(file=discord.File(data, 'cool_image.png'))

def setup(bot):    
    bot.add_cog(Test(bot))