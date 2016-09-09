from discord.ext import commands as game_RPS
import discord.utils

import sys
import unicodedata
import random

class Games_RPS:
    """Play rock, paper, scissors with the bot."""

    def __init__(self, bot):
        self.bot = bot

    @game_RPS.command(pass_context=True, name='rps', aliases=['RPS'])
    async def _gameRPS(self, ctx):
        number = random.randint(0, 100)
        if (number >= 0) and (number <= 30):
            if (number >= 0) and (number <= 10):
                m = '{}, you played \U0001F5FF , and I played \U0001F5D2 , I win. \U0001F604'
                await self.bot.say(m.format(ctx.message.author.mention))
            if (number > 10) and (number <= 20):
                m = '{}, you played \U0001F5D2 , and I played \u2702 , I win. \U0001F604'
                await self.bot.say(m.format(ctx.message.author.mention))
            if (number > 20) and (number <= 30):
                m = '{}, you played \u2702 , and I played \U0001F5FF , I win. \U0001F604'
                await self.bot.say(m.format(ctx.message.author.mention))
        if (number  > 30) and (number <= 60):
            if (number > 30) and (number <= 40):
                m = '{}, you played \u2702 , and I played \U0001F5D2 , you win. \U0001F626'
                await self.bot.say(m.format(ctx.message.author.mention))
            if (number > 40) and (number <= 50):
                m = '{}, you played \U0001F5D2 , and I played \U0001F5FF , you win. \U0001F626'
                await self.bot.say(m.format(ctx.message.author.mention))
            if (number > 50) and (number <= 60):
                m = '{}, you played \U0001F5FF , and I played \u2702 , you win. \U0001F626'
                await self.bot.say(m.format(ctx.message.author.mention))
        if (number  > 60) and (number <= 100):
            if (number > 60) and (number <= 75):
                m = '{}, we both played \u2702 , it\'s a tie! \U0001F603'
                await self.bot.say(m.format(ctx.message.author.mention))
            if (number > 75) and (number <= 85):
                m = '{}, we both played \U0001F5D2 , it\'s a tie! \U0001F603'
                await self.bot.say(m.format(ctx.message.author.mention))
            if (number > 85) and (number <= 100):
                m = '{}, we both played \U0001F5FF , it\'s a tie! \U0001F603'
                await self.bot.say(m.format(ctx.message.author.mention))

def setup(bot):
    gRPS = Games_RPS(bot)
    bot.add_cog(gRPS)
