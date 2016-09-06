from __future__ import print_function
from discord.ext import commands as packgenCMD
import discord.utils

import random

class User_PackGen:
    """User commands that allows making a funny pack name for The Sims 4.

       Idea submitted by Proculus#6163."""

    def __init__(self, bot):
        self.bot = bot

    @packgenCMD.command(pass_context=True, name='packgen', aliases=['Packgen', 'PACKGEN'])
    async def _packgen(self, ctx):
        """Asks the user for a word (or few words) and puts them into a random pack name."""
        await self.bot.send_message(ctx.message.channel,'{0.message.author.mention}, enter any random word(s) that come to mind. (Example: "Chris & Pie" or "Food")'.format(ctx))

        packName = await self.bot.wait_for_message(timeout=60.0, channel=ctx.message.channel, author=ctx.message.author)

        nameParts = ['Get {}'.format(packName.content), '{} Stuff'.format(packName.content), '{}'.format(packName.content), 'Get to {}'.format(packName.content)]

        pack = random.choice(nameParts)
        await self.bot.send_message(ctx.message.channel,'{0.message.author.mention}, The Sims 4: **{1}** sounds fun!'.format(ctx, pack))

        #print(Name)
        #await self.bot.say('{}, The Sims 4: **{}** sounds amazing!'.format(ctx.message.author.mention, name))

def setup(bot):
    U_PackGen = User_PackGen(bot)
    bot.add_cog(U_PackGen)
