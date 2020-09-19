#involves functions revolving around random function

from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name="roll",help="Gives random integer between agr1 and agr2")
    async def random(self,ctx,*args):
        n=random.randrange(int(args[0]),int(args[1]))
        await ctx.send(n)
    
    @commands.command(name="rolldice",help="Roll the dice to get integer between 1-6")
    async def dice(self,ctx):
        n=random.randrange(1,6)
        await ctx.send(n)

    @commands.command(name="coinflip",help="Flips the coin")
    async def coin(self,ctx,*args):
        n=random.randint(0,1)
        await ctx.send("Heads" if n==1 else "Tails")
    
    @commands.command(name="group",help="Divide args(members) into arg2(no of groups) groups")
    async def group(self,ctx,*args):
        x=int(args[0])
        y=len(args)-1
        len_of_each=int(y/x)
        if y%x!=0:
            len_of_each+=1
        print(len_of_each)
        n = [i for i in range(1,len(args))]
        response = ''
        print(n)
        for i in range(x):
            for j in range(len_of_each):
                if(len(n)==0):
                    break
                x = random.randint(0,len(n)-1)
                response+=args[n[x]]+','
                del n[x]
            response+='\n'
        print(response)
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Gamble(bot))