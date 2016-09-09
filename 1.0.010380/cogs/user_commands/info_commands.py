from discord.ext import commands as u_InfoCMDS
import discord.utils

import sys
import unicodedata

class User_InfoCommands:
    """User commands that get information."""

    def __init__(self, bot):
        self.bot = bot

    @u_InfoCMDS.command(pass_context=True, name='info', aliases=['Info', 'INFO'])
    async def info(self, ctx):
        """Asks what the user wants info to."""
        await self.bot.say('{}, please specify what you want the info to, using `!infobot`, `!infoserver`, or `!infouser`.'.format(ctx.message.author.mention))

    @u_InfoCMDS.command(pass_context=True, name='infoserver', aliases=['InfoServer', 'INFOSERVER', 'infoServer', 'Infoserver'])
    async def info_server(self, ctx):
        """Returns information about the server."""
        await self.bot.say('{} has requested the server info: \n\nServer Name: {}\nServer ID: `{}`\nServer Owner: {}\nServer Region: {}\nServer Member Count: `{}`'.format(ctx.message.author.mention, ctx.message.server.name, ctx.message.server.id, ctx.message.server.owner, ctx.message.server.region, ctx.message.server.member_count) + '\nIf you still have any questions regarding server information, you may ask {}'.format(ctx.message.server.owner))

    @u_InfoCMDS.command(pass_context=True, name='infobot', aliases=['InfoBot', 'INFOBOT', 'infoBot', 'Infobot'])
    async def info_bot(self, ctx):
        """Returns information about the bot."""
        botVersion = '1.0.010380'
        await self.bot.say('{} has requested my bot information: \n\nBot Name: {} \nBot ID: `{}` \nBot Version: `{}` \nBot Developer: Simalary (Chris)#6397'.format(ctx.message.author.mention, self.bot.user.name, self.bot.user.id, botVersion))

    @u_InfoCMDS.command(pass_context=True, name='infouser', aliases=['InfoUser', 'INFOUSER', 'infoUser', 'Infouser'])
    async def info_user(self, ctx, member : discord.Member = None):
        """Returns information about the user.
           If the user asks for another user's information,
           that will be returned."""
        if member is None:
                with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt') as p:
                        for line in p:
                                name = str(ctx.message.author.name)
                                newName = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
                                if str(newName) in line:
                                        points = line.rsplit(": ",1)[1]
                                        await self.bot.say('{}\'s info: \n\nUsername: {} | #{} \nID: `{}` \nStatus: {} \nSimPoints: `{}`\nDate Joined: `{}`\nDate Created: `{}`\nAvatar: {}'.format(ctx.message.author.mention, ctx.message.author.name, ctx.message.author.discriminator, ctx.message.author.id, ctx.message.author.status, points, ctx.message.author.joined_at, ctx.message.author.created_at, ctx.message.author.avatar_url))
        else:
                with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt') as p:
                        for line in p:
                                name = str(member.name)
                                newName = unicodedata.normalize('NFKD', name).encode('ascii','ignore')
                                if str(newName) in line:
                                        points = line.rsplit(": ",1)[1]
                                        await self.bot.say('{}, here is {}\'s info: \n\nUsername: {} | #{} \nID: `{}` \nStatus: {} \nSimPoints: `{}`\nDate Joined: `{}`\nDate Created: `{}`\nAvatar: {}'.format(ctx.message.author.mention, member.name, member.name, member.discriminator, member.id, member.status, points, member.joined_at, member.created_at, member.avatar_url))


def setup(bot):
    U_IC = User_InfoCommands(bot)
    bot.add_cog(U_IC)
