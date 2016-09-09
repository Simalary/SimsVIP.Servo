from __future__ import print_function

import discord
from discord.ext import commands

from cogs.utils.extension_loader import extensions_list

import random
import json, asyncio
import datetime, re

description = "Servo"

initial_extensions = extensions_list

prefix = ['!', '\\', '?']
bot = commands.Bot(command_prefix=prefix, description=description, pm_help=None)

@bot.event
async def on_ready():
    print('')
    print('LOGGED IN: {0.user.name}#{0.user.discriminator}: {0.user.id}'.format(bot))
    print('---------------')
    print('')
    print('')

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    await bot.process_commands(message)

@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CheckFailure):
        await bot.send_message(ctx.message.channel, '{0.author.mention}, nice try. \U0001F60F'.format(ctx.message))

def load_credentials():
    with open('credentials.json') as c:
        return json.load(c)

announcements_channel = discord.Object(id='160485301830156288')
sims_legacies_channel = discord.Object(id='173075469237747712')
general_channel = discord.Object(id='160471773077438465')
labratory_channel = discord.Object(id='164458255714746368')

credentials = load_credentials()

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print('Extension loaded: {}'.format(extension))
        except Exception as e:
            print('Extension failed to load: {}\n{}: {}'.format(extension, type(e).__name__, e))

    bot.client_id = credentials['client_id']
    bot.run(credentials['token'])
