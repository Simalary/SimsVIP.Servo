from discord.ext import commands as ownercmds
import discord.utils
from discord.utils import _bytes_to_base64_data

from cogs.utils import checks as chks

from collections import OrderedDict, deque, Counter

from Servo import credentials
from Servo import general_channel, sims_legacies_channel,announcements_channel, labratory_channel

import requests
import socket
import sys
import datetime
import os
import time

class OwnerCommands:
    """Owner commands"""

    def __init__(self, bot):
        self.bot = bot

    @ownercmds.command(pass_context=True, name='reload', hidden=True)
    @chks.is_owner()
    async def _reload(self, ctx, *, module=None):
        """Reloads a module."""
        if module==None:
            await self.bot.say('{}, you need to specify an extension. (Example: **!reload cog.mod_commands**)'.format(ctx.message.author.mention, module))
            return
        try:
            self.bot.unload_extension(module)
            self.bot.load_extension(module)
        except Exception as e:
            await self.bot.say('{}, extension failed to reload: **{}**. \n{}: {}'.format(ctx.message.author.mention, module, type(e).__name__, e))
        else:
            await self.bot.say('{}, extension reloaded: **{}**.'.format(ctx.message.author.mention, module))

    @ownercmds.command(pass_context=True,name='token')
    @chks.is_owner()
    async def _getToken(self, ctx):
        """Print the token in the console."""
        await self.bot.delete_message(ctx.message)
        print(credentials['token'])

    @ownercmds.command(pass_context=True,name='shutdown')
    @chks.is_owner()
    async def _quit(self, ctx):
        """Shuts off the bot."""
        await self.bot.say('{0.message.author.mention}, shutting down.'.format(ctx))
        await self.bot.logout()

    @ownercmds.command(pass_context=True, name='update', aliases=['Update', 'UPDATE'])
    @chks.is_owner()
    async def _update(self, ctx, *, update_info):
        """Like !talk, this sends a message as the bot, but to multiple
        channels."""
        await self.bot.send_message(general_channel, update_info)
        await self.bot.send_message(labratory_channel, update_info)
        await self.bot.delete_message(ctx.message)

    @ownercmds.command(pass_context=True, name='name', aliases=['Name', 'NAME', 'username', 'USERNAME', 'Username'])
    @chks.is_owner()
    async def _setBotName(self, ctx, *, username=None):
        """Set the bot's new username."""
        if (username == None):
            await self.bot.say('{0.message.author.mention}, you need to specify a username. (Example: **!name Servo: The Best Bot Ever**)'.format(ctx))
        else:
            NewName = username
            OldName = self.bot.user.name
            HostName = 'LAPTOP-UFA73040'
            AvatarPath = "C:\\Users\\harpe\\Documents\\Discord\\Bots\\SimsVIP.Servo (Python) [1.0]\\Avatar.PNG"
            if NewName == OldName:
                    await self.bot.say('{}, **{}** is the same as my current username.'.format(ctx.message.author.mention, NewName))
            else:
                    if socket.gethostname() != HostName:
                            await self.bot.say('{}, ERROR: This command can only be run when I am running on Simalary (Chris)\'s computer.'.format(ctx.message.author.mention))
                    else:
                            with open(AvatarPath, 'rb') as m:

                                headers = {'Authorization': credentials['token']}
                                payload = {'username': NewName, 'avatar':  _bytes_to_base64_data(m.read())}
                                r = requests.patch('https://discordapp.com/api/users/@me', headers=headers, json=payload)

                                if str(r.json()) == '{\'username\': [\'You are changing your username too fast. Try again later.\']}':
                                    await self.bot.say('{}, my username cannot be changed at this time, please try again later.'.format(ctx.message.author.mention))
                                    #print(r.json())
                                else:
                                    m = open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt','r')
                                    filedata = m.read()
                                    m.close()

                                    newdata = filedata.replace(str(OldName),str(NewName))

                                    m = open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\USERS\\' + 'Members.SimsVIP.txt','w')
                                    m.write(newdata)
                                    m.close()
                                    await self.bot.say('{}, has changed my username to **{}**.'.format(ctx.message.author.mention, NewName))
                                    #print(r.json())

def setup(bot):
    o_c = OwnerCommands(bot)
    bot.add_cog(o_c)
