#involves functions revolving around random function

from discord.ext import commands
import random

class Gamble(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx,er):
        print(er)
        await ctx.send("Please check with #help usage of this command or contact your admin")
    
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
    async def group(self,ctx):
        s = ctx.message.content
        print(s)
        s = s.strip('#group ')
        n = int(s[0])
        s = s[1:]
        s = s.split()
        random.shuffle(s)
        
        groups = [[] for i in range(n)]

        for i in range(len(s)):
            groups[i%n].append(s[i])
        
        random.shuffle(groups)
        
        response = ''
        for i in groups:
            for j in i:
                response += str(j)+" "
            response += '\n'
        print(response)
        await ctx.send(response)




def setup(bot):
    bot.add_cog(Gamble(bot))