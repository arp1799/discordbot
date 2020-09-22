import os
from discord.ext import commands
from settings import DTOKEN


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

bot.run(DTOKEN)


