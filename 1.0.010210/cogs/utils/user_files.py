import discord.utils

import discord
import asyncio

from Servo import bot

import sys
import re
import unicodedata

class UserFiles:
    """Files that store information for users."""

    def __init__(self, bot):
        self.bot = bot

    async def userlist(self):
        for server in self.bot.servers:
            for member in server.members:
                names = str(member.name)
                newNames = unicodedata.normalize('NFKD', names).encode('ascii','ignore')
                with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt', "a") as m:
                    if str(newNames) in open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt').read():
                        pass
                    else:
                        m.write('\n{} (#{}) | {}'.format(newNames, member.discriminator, member.id))


    async def pointsinfo(self):
        for server in self.bot.servers:
            for member in server.members:
                names = str(member.name)
                newNames = unicodedata.normalize('NFKD', names).encode('ascii','ignore')
                with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt', "a") as p:
                    if str(newNames) in open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Points.SimsVIP.txt').read():
                        pass
                    else:
                        p.write('\n{} (#{}) | POINTS: 500'.format(newNames, member.discriminator))

    @bot.event
    async def on_ready(self):
        await self.userlist()
        await self.pointsinfo()

def setup(bot):
    uFiles = UserFiles(bot)
    bot.add_cog(uFiles)
