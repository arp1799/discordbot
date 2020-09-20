import io
import aiohttp
import discord
import random
from discord.ext import commands

class Images(commands.Cog):#Bot is passed as parameter as commands.Cogs 
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx,er):
        print(er)
        await ctx.send("Please check with #help usage of this command or contact your admin")

    @commands.command(name='cat',help='Output random cat image')
    async def cat(self,context):
        async with context.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://aws.random.cat/meow") as resp:
                    if resp.status != 200:
                        return await context.send('Could not download file...')
                    data= await resp.json()
                    embed=discord.Embed(title='Meow')
                    embed.set_image(url=data['file'])
                    embed.set_footer(text="http://random.cat/")
                    await context.send(embed=embed)

    @commands.command(name='dog',help='Output random dog image')
    async def dog(self,context):
        async with context.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("http://random.dog/woof.json") as resp:
                    if resp.status != 200:
                        return await context.send('Could not download file...')
                    data= await resp.json()
                    embed=discord.Embed(title='woooof')
                    embed.set_image(url=data['url'])
                    embed.set_footer(text="http://random.dog/")
                    await context.send(embed=embed)

    @commands.command(name='fox',help='Output random fox image')
    async def fox(self,context):
        async with context.channel.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomfox.ca/floof/") as resp:
                    if resp.status != 200:
                        return await context.send('Could not download file...')
                    data= await resp.json()
                    embed=discord.Embed(title='woooof')
                    embed.set_image(url=data['image'])
                    embed.set_footer(text="https://randomfox.ca/")
                    await context.send(embed=embed)


def setup(bot):    
    bot.add_cog(Images(bot))