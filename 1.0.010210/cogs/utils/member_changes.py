from discord.ext import commands as u_MiscCMDs
import discord.utils

import sys
import unicodedata

from Servo import bot
from Servo import general_channel, sims_legacies_channel,announcements_channel, labratory_channel

class MemberChanges:
    """Checks for when changes to members occure."""

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_member_join(self, member):
        """When a member joins, the bot will welcome them
           to the server with a mention.

           The user will then be added to the user files."""
        server = member.server
        fmt = 'Welcome {0.mention} to the **{1.name} Chat Server**! \U0001F604'
        await self.bot.send_message(server, fmt.format(member, server))
        name = str(member.name)
        newName = unicodedata.normalize('NFKD', names).encode('ascii','ignore')
        with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt', "a") as p:
            if str(newName) not in p:
                p.write('\n{} (#{}) | POINTS: 500'.format(newName, member.discriminator))
        with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt', "a") as m:
            if str(newNames) not in p:
                m.write('\n{} (#{}) | {}'.format(newNames, member.discriminator, member.id))

    @bot.event
    async def on_member_remove(self, member):
        server = member.server
        fmt = '{0.mention} has left the server. \U0001F626'
        await self.bot.send_message(server, fmt.format(member))
        name = str(member.name)
        newName = unicodedata.normalize('NFKD', names).encode('ascii','ignore')
        with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt', "a") as p:
            for line in p:
                if str(newName) not in line:
                    p.write('\n{} (#{}) | POINTS: 500'.format(newName, member.discriminator))
        with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt', "a") as m:
            for line in m:
                if str(newNames) not in line:
                    m.write('\n{} (#{}) | {}'.format(newNames, member.discriminator, member.id))
    @bot.event
    async def on_member_update(self, before, after):
        if after.name != before.name:
            await self.bot.send_message(general_channel, '**{}** has changed their username to **{}**.'.format(before.name, after.name))
            beforenames = str(before.name)
            afternames = str(after.name)
            newBeforeNames = unicodedata.normalize('NFKD', beforenames).encode('ascii','ignore')
            newAfterNames = unicodedata.normalize('NFKD', afternames).encode('ascii','ignore')
            m = open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt','r')
            filedata = m.read()
            m.close()
            p = open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt','r')
            filedata = p.read()
            p.close()

            newdata = filedata.replace(str(newBeforeNames),str(newAfterNames))

            m = open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt','w')
            m.write(newdata)
            m.close()
            p = open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt','w')
            p.write(newdata)
            p.close()
        if after.nick != before.nick:
            if after.nick is None:
                await self.bot.send_message(general_channel, '**{}** has cleared their nickname.'.format(before.name))
            else:
                await self.bot.send_message(general_channel, '**{}** has changed their nickname to **{}**.'.format(before.name, after.nick))


def setup(bot):
    MemChngs = MemberChanges(bot)
    bot.add_cog(MemChngs)
