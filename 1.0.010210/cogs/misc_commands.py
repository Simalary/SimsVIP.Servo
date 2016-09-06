from discord.ext import commands
import discord.utils

from cogs.utils import checks

class Misc:
    """Misc commands"""

    def __init__(self, bot):
        self.bot = bot

    #Commands for checking rank
    @commands.command(pass_context=True, name='owner', hidden=True)
    @checks.is_owner()
    async def _owner(self, ctx):
        """If checks works, replies only to the owner"""
        await self.bot.say('{0.message.author.mention}, you are my owner.'.format(ctx))

    @commands.command(pass_context=True, name='staff', hidden=True)
    @checks.is_staff()
    async def _staff(self, ctx):
        """If checks works, replies only to staff"""
        await self.bot.say('{0.message.author.mention}, you are staff.'.format(ctx))

    @commands.command(pass_context=True, name='servoRepair', hidden=True, aliases=['servorepair'])
    @checks.is_servoRepair()
    async def _servoRepair(self, ctx):
        """If checks works, replies only to repairmen"""
        await self.bot.say('{0.message.author.mention}, you are a repairman for me.'.format(ctx))

def setup(bot):
    m_c = Misc(bot)
    bot.add_cog(m_c)
