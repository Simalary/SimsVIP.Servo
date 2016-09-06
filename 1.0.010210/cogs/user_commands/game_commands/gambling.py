from discord.ext import commands as game_GambleCMDs
import discord.utils

import sys
import unicodedata
import random

class Games_Gambling:
    """Gamble random amounts."""

    def __init__(self, bot):
        self.bot = bot

    @game_GambleCMDs.command(pass_context=True, name='gamble', aliases=['Gamble', 'GAMBLE'])
    async def gamble(self, ctx):
        if len(ctx.message.content) <= 7:
            await self.bot.say('{}, you need to specify a number. You can\'t just gamble nothing.'.format(ctx.message.author.mention))
        else:
            try:
                gamble = int(ctx.message.content[8:])
                if (gamble == 0) or (gamble <=0):
                        await self.bot.say('{}, you need to specify a number **higher than 0**. '.format(ctx.message.author.mention))
                        return
            except:
                await self.bot.say('{}, you need to specify a **number**, you can\'t just gamble letters, it doesn\'t work that way.'.format(ctx.message.author.mention))
                return
            gamble_set = random.randint(1,100)
            if gamble_set >= 50:
                gamble_won = int(gamble) * 2
                await self.bot.say('{}, you gambled {}, rolled {}, and won twice the amount! You have won **{}**! \U0001F62E'.format(ctx.message.author.mention, gamble, gamble_set, gamble_won))
            else:
                await self.bot.say('{}, you gambled {}, rolled {}, and lost! \U0001F61E'.format(ctx.message.author.mention, gamble, gamble_set))

    @game_GambleCMDs.command(pass_context=True, name='supergamble', aliases=['SuperGamble', 'Supergamble', 'SUPERGAMBLE'])
    async def supergamble(self, ctx):
        if len(ctx.message.content) <= 12:
            await self.bot.say('{}, you need to specify a number. You can\'t just gamble nothing.*'.format(ctx.message.author.mention))
        else:
            try:
                gamble = int(ctx.message.content[13:])
                if (gamble == 0) or (gamble <=0):
                        await self.bot.say('{}, you need to specify a number **higher than 0**.'.format(ctx.message.author.mention))
                        return
            except:
                await self.bot.say('{}, you need to specify a **number**, you can\'t just gamble letters, it doesn\'t work that way.'.format(ctx.message.author.mention))
                return
            gamble_set = random.randint(1,100)
            if gamble_set >= 80:
                gamble_won = int(gamble) * 3
                await self.bot.say('{}, you gambled {}, rolled {}, and won three times the amount! You have won **{}**! \U0001F62E'.format(ctx.message.author.mention, gamble, gamble_set, gamble_won))
            else:
                await self.bot.say('{}, you gambled {}, rolled {}, and lost! \U0001F61E'.format(ctx.message.author.mention, gamble, gamble_set))

def setup(bot):
    gGamble = Games_Gambling(bot)
    bot.add_cog(gGamble)
