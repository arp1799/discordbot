from discord.ext import commands
import datetime
import discord

class Admin(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(name="kick",help="Kick user from guild along with reason")
    @commands.is_owner()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member=None,reason:str="No reason specified"):
        if member is not None:
            await ctx.guild.kick(member,reason=reason)
            await ctx.send("User kicked from guild")
        else:
            await ctx.send("Specify member to kick along with reason")
    
    @commands.command(name="ban",help="Ban user from guild along with reason")
    @commands.is_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member=None,reason:str="No reason specified"):
        if member is not None:
            await ctx.guild.ban(member,reason=reason)
            await ctx.send("User banned from guild")
        else:
            await ctx.send("Specify member to ban along with reason")
    
    @commands.command(name="unban",help="Unban user from guild along with reason")
    @commands.is_owner()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self,ctx,member:str="",reason:str="No reason specified"):
        if member == "":
            await ctx.send("Specify member to unban along with reason")
            return
        ban_list=await ctx.guild.bans()
        for mem in ban_list:
            if mem.user.name == member:
                await ctx.guild.unban(mem.user,reason=reason)
                await ctx.send("User unbanned")
                return
        await ctx.send("User not found in ban list")

    @commands.command(name="unload",help="Unload any section of commands")
    @commands.is_owner()
    async def unload(self,ctx,cog:str):
        try:
            s="cogs."+cog
            self.bot.unload_extension(s)
        except Exception as e:
            print(e)
            await ctx.send("Could not unload Cog...")
            return
        await ctx.send("Cog Unloaded")
    
    @commands.command(name="load",help="Load the section of commands which was unloaded before")
    @commands.is_owner()
    async def load(self,ctx,cog:str):
        try:
            s="cogs."+cog
            self.bot.load_extension(s)
        except Exception as e:
            print(e)
            await ctx.send("Could not load Cog...")
            return 
        await ctx.send("Cog Loaded")
        
    @commands.command(name="reload",help="Reoad the section of commands")
    @commands.is_owner()
    async def reload(self,ctx,cog:str):
        try:
            s="cogs."+cog
            self.bot.unload_extension(s)
            self.bot.load_extension(s)
        except Exception as e:
            print(e)
            await ctx.send("Could not reload Cog...")
            return 
        await ctx.send("Cog Reloaded")

    @commands.command(name="status",help="Status of server")
    async def stats(self,ctx):
        guild=ctx.guild
        voice_chnls=len(guild.voice_channels)
        text_chnls=len(guild.text_channels)
        members=guild.member_count
        #members_list = await guild.fetch_members(limit=150).flatten()
        embed=discord.Embed(description="Server Status",colour=discord.Colour.dark_purple())
        embed.set_author(name=self.bot.user.name)
        embed.set_thumbnail(url="https://www.internetandtechnologylaw.com/files/2019/06/iStock-872962368-chat-bots.jpg")
        embed.set_image(url="https://lh3.googleusercontent.com/CYwIC5j2M_EDP1wFJH5hgfZFB2qhvr9T5bbeT90uRDDjkJBQRpKBSJVjQ-rSxTqsiFU8cNw52nPSLjumMzzvv9ER5jUb9u7BphJji2ZXOvUbX5TIfypEH_kcJ2IyCxvu4D5sykTdhOretzSI8H2ncCh7vAaj1JVQIS8uP5fXIv_YoRlv_RzO1KNiV3O2xB0SUt_ePsrO99fTlEvZPxQhxGfURJlqklgwg-fILr7G5gYUTfuxxZXznS199Ko_5d_NCmZBTz41_-1BNFoJy4rDNp-qq9tx9dY9W740Emi2jhs8tQtj-XX3xGQFUG8euvaAOhq7f6jEa_fA-o2yOwr2CrqrVhjudsygDzy_29vK8RoQWeJJ8Roelx46qDqlxlqcek2hGY2LG2Hjbi3t_B6bXihbWaMUEby-ErkZCYf73MhMBpNF2KX0Jmy2_WMbPwvj7eH6X_2c6f111T3t1Ce05ZUmVmb2Xtl6g8BLjFBM77oSw-7HcRVWwzrMm5HNAc3V9uBZASj_8ENRidmh9PVzBVHrDa1QkF-uUTUphU3p54gkCP3s8m832gmCPnZcVRNQwqIcS2uxYi6Gq2HqyQtFgd6Uam5oWzb9sSo0O13L5LQ55fc_CeJACH5RMb1sNScaZRYnKx4eHJpi8_8ZCOKsgqxxkVVq9N7uBgDXQk97Oj_ULxCmpLjEL693yfHCug=w1141-h855-no?authuser=0")
        embed.add_field(name="Server Name",value=guild.name,inline=False)
        embed.add_field(name="# Voice Channels",value=voice_chnls)
        embed.add_field(name="# Text Channels",value=text_chnls)
        embed.add_field(name="# Members ",value=members)
        embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=embed)
    
    

def setup(bot):
    bot.add_cog(Admin(bot))

