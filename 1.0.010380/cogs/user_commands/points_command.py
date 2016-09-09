from discord.ext import commands as u_PointsCMD
import discord.utils

import sys
import unicodedata

class User_PointsCommand:
    """User command that will show points."""

    def __init__(self, bot):
        self.bot = bot

    @u_PointsCMD.command(pass_context=True, name='points', aliases=['POINTS', 'Points'])
    async def _getpoints(self, ctx, member : discord.Member = None):
        """Returns the points of the user.
           If no user is specified, the bot will return
           the author's points."""
        if member is None:
            with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt') as p:
                for line in p:
                    name = str(ctx.message.author.name)
                    newName = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
                    if str(newName) in line:
                        points = line.rsplit(": ",1)[1]
                        await self.bot.say('{}, you have `{}` SimPoints.'.format(ctx.message.author.mention, points))
        else:
            with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt') as p:
                for line in p:
                    name = str(member.name)
                    newName = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
                    if str(newName) in line:
                        points = line.rsplit(": ",1)[1]
                        await self.bot.say('{}, {} has `{}` SimPoints.'.format(ctx.message.author.mention,name , points))

def setup(bot):
    U_PC = User_PointsCommand(bot)
    bot.add_cog(U_PC)
