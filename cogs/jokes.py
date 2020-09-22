from discord.ext import commands
from utils import get_momma_jokes

class Jokes(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        

    @commands.command(name="roast",help="Tease another member with yo mama joke")
    async def yomomma(self,ctx,name=''):
        insult=await get_momma_jokes()
        if name !='':  
            mem=name
        else:
            mem=str(ctx.message.author.name)

        insult=insult.replace("Yo mama's",mem)
        insult=insult.replace("Yo mama",mem)
        insult=insult.replace("she","he")
        insult=insult.replace("her","his")
        insult=insult.replace("her's","his")
        await ctx.send(insult)

   
def setup(bot):
    bot.add_cog(Jokes(bot))