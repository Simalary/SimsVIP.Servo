from __future__ import print_function

from discord.ext import commands
import discord.utils
import discord
from Servo import bot

import unicodedata
import time
from colorama import Fore, Back, Style
from colorama import init
init()

class Logging:
    """Logs the chat"""

    def __init__(self, bot):
        self.bot = bot

    @bot.event
    async def on_ready(self):
        with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\LOGS\\' + time.strftime("%m-%d-%Y") + '--SimsVIP.txt', "a") as f:
            f.write('\n------------------\n')
            """Writes to the log file, seperating old information from new"""

    @bot.event
    async def on_message(self, message):
        await self.bot.wait_until_ready()
        try:
            if message.author.id == message.server.owner:
                try:
                    newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                    print(Style.RESET_ALL + Fore.RED + 'Kit   :   {}   |   (CHANNEL: {})'.format(newMessageContent, message.channel.name) + Style.RESET_ALL)
                except:
                    print(Style.RESET_ALL + Back.RED + 'ERROR: Invalid character.'.format(message.author, message.content, message.channel.name) + Style.RESET_ALL)

            elif {"servo repairman"} & {role.name.lower() for role in message.author.roles}:
                if message.author.id == "146719621368643584":
                    try:
                        newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                        print(Style.RESET_ALL + Fore.GREEN + 'Simalary   :   {}   |   (CHANNEL: {})'.format(newMessageContent, message.channel.name) + Style.RESET_ALL)
                    except:
                        print(Style.RESET_ALL + Back.RED + 'ERROR: Invalid character.'.format(message.author, message.content, message.channel.name) + Style.RESET_ALL)

            elif {"simsvip staff"} & {role.name.lower() for role in message.author.roles}:
                    try:
                        newMessageAuthor = unicodedata.normalize('NFKD', str(message.author.name)).encode('ascii','ignore')
                        newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                        print(Style.RESET_ALL + Fore.YELLOW + '{}   :   {}   |   (CHANNEL: {})'.format(newMessageAuthor, newMessageContent, message.channel.name) + Style.RESET_ALL)
                    except:
                        print(Style.RESET_ALL + Back.RED + 'ERROR: Invalid character.'.format(message.author, message.content, message.channel.name) + Style.RESET_ALL)
            elif message.author.id == "164448613647253504":
                    try:
                        newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                        print(Style.RESET_ALL + Fore.BLUE + 'Servo   :   {}   |   (CHANNEL: {})'.format(newMessageContent, message.channel.name) + Style.RESET_ALL)
                    except:
                        print(Style.RESET_ALL + Back.RED + 'ERROR: Invalid character.'.format(message.author, message.content, message.channel.name + Style.RESET_ALL))
            else:
                    try:
                        newMessageAuthor = unicodedata.normalize('NFKD', str(message.author.name)).encode('ascii','ignore')
                        newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                        print(Style.RESET_ALL + Fore.WHITE + '{}   :   {}   |   (CHANNEL: {})'.format(newMessageAuthor, newMessageContent, message.channel.name) + Style.RESET_ALL)
                    except:
                        print(Style.RESET_ALL + Back.RED + 'ERROR: Invalid character.'.format(message.author, message.content, message.channel.name) + Style.RESET_ALL)

            with open('C:\\Users\\harpe\\Documents\\Discord\\Bots\\LOGS\\' + time.strftime("%m-%d-%Y") + '--SimsVIP.txt', "a") as f:
                if message.author == message.server.owner:
                    try:
                        newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                        f.write('{}   :   {}   |   (CHANNEL: {})'.format("Kit", newMessageContent, message.channel.name))
                        f.write('\n')
                    except:
                        f.write('ERROR: Invalid character.'.format(message.author, message.content, message.channel.name))
                        f.write('\n')

                elif {"servo repairman"} & {role.name.lower() for role in message.author.roles}:
                    if message.author.id == "146719621368643584":
                        try:
                            newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                            f.write('{}   :   {}   |   (CHANNEL: {})'.format("Simalary", newMessageContent, message.channel.name))
                            f.write('\n')
                        except:
                            f.write('ERROR: Invalid character.'.format(message.author, message.content, message.channel.name))
                            f.write('\n')
                    else:
                        try:
                            newMessageAuthor = unicodedata.normalize('NFKD', str(message.author.name)).encode('ascii','ignore')
                            newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                            f.write('{}   :   {}   |   (CHANNEL: {})'.format(newMessageAuthor, newMessageContent, message.channel.name))
                            f.write('\n')
                        except:
                            f.write('ERROR: Invalid character.'.format(message.author, message.content, message.channel.name))
                            f.write('\n')

                elif {"simsvip staff"} & {role.name.lower() for role in message.author.roles}:
                        try:
                            newMessageAuthor = unicodedata.normalize('NFKD', str(message.author.name)).encode('ascii','ignore')
                            newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                            f.write('{}   :   {}   |   (CHANNEL: {})'.format(newMessageAuthor, newMessageContent, message.channel.name))
                            f.write('\n')
                        except:
                            f.write('ERROR: Invalid character.'.format(message.author, message.content, message.channel.name))
                            f.write('\n')
                else:
                    if message.author.id == "164448613647253504":
                        try:
                            newMessageAuthor = unicodedata.normalize('NFKD', str(message.author.name)).encode('ascii','ignore')
                            newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                            f.write('Servo   :   {}   |   (CHANNEL: {})'.format(newMessageContent, message.channel.name))
                            f.write('\n')
                        except:
                            f.write('ERROR: Invalid character.'.format(message.author, message.content, message.channel.name))
                            f.write('\n')
                    else:
                        try:
                            newMessageAuthor = unicodedata.normalize('NFKD', str(message.author.name)).encode('ascii','ignore')
                            newMessageContent = unicodedata.normalize('NFKD', str(message.content)).encode('ascii','ignore')
                            f.write('{}   :   {}   |   (CHANNEL: {})'.format(newMessageAuthor, newMessageContent, message.channel.name))
                            f.write('\n')
                        except:
                            f.write('ERROR: Invalid character.'.format(message.author, message.content, message.channel.name))
                            f.write('\n')
        except:
            pass

def setup(bot):
    l = Logging(bot)
    bot.add_cog(l)
