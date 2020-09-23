from discord.ext import commands
import datetime
import discord

from utils import dm_user

from rps.model import RPS
from rps.parser import RockPaperScissorParser
from rps.controller import RPSGame

from guessit.controller import GuessitGame

class Games(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def hm(self, ctx, guess: str):
        player_id = ctx.author.id
        guessit_instance = GuessitGame()
        game_over, won = guessit_instance.run(player_id, guess)

        if game_over:
            game_over_message = "You did not win"
            if won:
                game_over_message = "Congrats you won!!"

            game_over_message = game_over_message + \
                " The word was %s" % guessit_instance.get_secret_word()

            await guessit_instance.reset(player_id)
            await ctx.send(game_over_message)

        else:
            await ctx.send("Progress: %s" % guessit_instance.get_progress_string())
            await ctx.send("Guess so far: %s" % guessit_instance.get_guess_string())

    @commands.command(name="rps",help="Play rock paper scissor with bot",usage="rock | paper | scissor as input")
    async def rckpaperscsor(self,ctx,user_choice:RockPaperScissorParser=RockPaperScissorParser(RPS.ROCK)):
        game_ins=RPSGame()
        user_choice=user_choice.choice
        won, bot_choice=game_ins.run(user_choice)
    
        if won is None:
            message = "It's a draw! Both chose: %s" % user_choice
        elif won is True:
            message = "You win: %s vs %s" % (user_choice, bot_choice)
        elif won is False:
            message = "You lose: %s vs %s" % (user_choice, bot_choice)

        await ctx.send(message)
        


def setup(bot):
    bot.add_cog(Games(bot))
