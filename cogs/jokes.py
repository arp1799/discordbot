import discord
from discord.ext import commands
from utils import get_momma_jokes

class Common(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx,er):
        print(er)
        await ctx.send("Please check with #help usage of this command or contact your admin")

    @commands.command(name="yomomma",help="Tease another member with yo mama joke")
    async def yomomma(self,ctx,member:discord.Member=None):
        insult=await get_momma_jokes()
        await ctx.send(insult)

   
def setup(bot):
    bot.add_cog(Common(bot))