from discord.ext import commands as u_CBcmds
import discord.utils

import sys
import unicodedata
import asyncio
import random
import cleverbot

from Servo import bot

class User_CleverBotCMD:
    """User commands that are random."""

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_message(self, message):
        if self.bot.user.mention in message.content:
            if message.author == self.bot.user:
                return
            if message.channel.id == '160471773077438465':
                return
            if message.content.startswith("!"):
                return
            else:
                cleverbot_client = cleverbot.Cleverbot()
                question = message.content
                CBanswer = cleverbot_client.ask(question)
                await self.bot.send_message(message.channel, '{}, {}'.format(message.author.mention, CBanswer))
        else:
            await bot.process_commands(message)

def setup(bot):
    cbCMD = User_CleverBotCMD(bot)
    bot.add_cog(cbCMD)
