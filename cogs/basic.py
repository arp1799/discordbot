from discord.ext import commands
from utils import text_to_owo

class Common(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx,er):
        print(er)       
        if self.bot:
            await ctx.send("Please check with #help usage of this command or contact your admin")
        return

    @commands.command(name="owo",help="Converts text to owo text")
    async def owo(self,ctx):
        text=text_to_owo(ctx.message.content)
        await ctx.send(text)
    
    @commands.command(name="invite",help="Creates invite link valid for 1 day")
    async def invite(self,ctx):
        link=await ctx.channel.create_invite(max_age=1)
        await ctx.send(link)

def setup(bot):
    bot.add_cog(Common(bot))