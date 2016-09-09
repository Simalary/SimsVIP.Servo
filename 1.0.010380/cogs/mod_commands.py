from discord.ext import commands
import discord.utils

from cogs.utils import checks

from Servo import general_channel, sims_legacies_channel,announcements_channel, labratory_channel

import asyncio

class ModCommands:
    """Mod commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, name='talk', aliases=['Talk', 'TALK'])
    @checks.is_mod()
    async def talk(self, ctx, *, text):
        """Repeats the message, and deletes the original.
           Acting like the bot originally said it."""
        await self.bot.say(text)
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True, name='announce', aliases=['Announce', 'ANNOUNCE'])
    @checks.is_mod()
    async def announcement(self, ctx, *, text):
        """Repeats the message, and deletes the original.
           Acting like the bot originally said it."""
        await self.bot.send_message(announcements_channel, text)
        await self.bot.delete_message(ctx.message)

    @commands.command(pass_context=True, name='topic', aliases=['Topic', 'TOPIC'])
    @checks.is_mod()
    async def _topic(self, ctx, *, topic):
        """Sets the channel topic to the specified text."""
        newtopic = topic
        if (newtopic == "clear".lower()) or (newtopic is None) or (newtopic == "none".lower()):
            await self.bot.edit_channel(ctx.message.channel, topic = "")
            await self.bot.say('{}, has cleared this channel\'s topic.'.format(ctx.message.author.mention))
        else:
            await self.bot.edit_channel(ctx.message.channel, topic = newtopic)
            await self.bot.say('{}, has changed this channel\'s topic to "{}".'.format(ctx.message.author.mention, newtopic))

    @commands.command(pass_context=True, name='setgame', aliases=['SETGAME','SetGame'])
    @checks.is_mod()
    async def setgame(self, ctx, *, game=None):
        """Sets the bot's current game status."""
        if (game is None):
            await self.bot.say('{}, please specify the game you want me to play. (Example: **!setgame The Sims:tm: 4**)'.format(ctx.message.author.mention))
        elif (game == "") or (game == "none") or (game == "clear"):
            delete_too = await self.bot.say('{} has cleared my game status.'.format(ctx.message.author.mention))
            await self.bot.change_status(game=discord.Game(name=None))
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(delete_too)
        else:
            await self.bot.change_status(game=discord.Game(name=game))
            delete_too = await self.bot.say('{} has set my game status to **{}**'.format(ctx.message.author.mention, game))
            await asyncio.sleep(5)
            await self.bot.delete_message(ctx.message)
            await self.bot.delete_message(delete_too)

    @commands.command(pass_context=True, name='clear', aliases=['Clear', 'CLEAR'])
    @checks.is_mod()
    async def clear(self, ctx, times=0):
        """Clears the specified amount of messages from
           the channel the message is sent from.If no
           amount is specified, the bot will attempt to
           remove all messages. If the specific channel
           id below is the current channel id, the whole
           channel history will not be cleared."""
        if (times is None):
            if ctx.message.channel.id == '160471773077438465':
                await self.bot.send_message(ctx.message.channel, '{}, complete message history cannot be cleared in this channel.'.format(ctx.message.author.mention))
        else:
                if (times == 0) or (times is None):
                    await self.bot.send_message(ctx.message.channel, '{} is deleting this channel\'s chat history...'.format(ctx.message.author.mention))
                    logs = self.bot.logs_from(ctx.message.channel)
                    await asyncio.sleep(5)
                    deleted = 0
                    async for message in logs:
                        try:
                            deleted += 1
                            await self.bot.delete_message(message)
                            if deleted == 5:
                                await asyncio.sleep(0.1)
                                pass
                            await self.bot.delete_message(message)
                        except:
                            pass

                elif (times > 0) and (times < 30):
                    delete_count = int(times)
                    deleted = 0
                    if (times == 1):
                        delete_too = await self.bot.send_message(ctx.message.channel, '{} is deleting `1` message from this channel\'s chat history...'.format(ctx.message.author.mention))
                    else:
                        delete_too = await self.bot.send_message(ctx.message.channel, '{} is deleting `{}` messages from this channel\'s chat history...'.format(ctx.message.author.mention, times))
                    logs = self.bot.logs_from(ctx.message.channel)
                    await asyncio.sleep(5)
                    await self.bot.delete_message(delete_too)
                    await self.bot.delete_message(ctx.message)
                    async for message in logs:
                        try:
                            deleted += 1
                            await self.bot.delete_message(message)
                            if deleted == times:
                                break
                            if deleted == 5:
                                await asyncio.sleep(0.1)
                        except:
                            pass

                elif (times < 0):
                    await self.bot.say('{}, you cannot delete `{}` messages from the channel.'.format(ctx.message.author.mention, times))

                elif (times > 30) & (ctx.message.channel.id == '160471773077438465'):
                    await self.bot.say('{}, it is not safe to delete more than `30` messages at a time in this channel.'.format(ctx.message.author.mention))

                else:
                    delete_count = int(times)
                    deleted = 0
                    delete_too = await self.bot.send_message(ctx.message.channel, '{} is deleting `{}` messages from this channel\'s chat history...'.format(ctx.message.author.mention, times))
                    logs = self.bot.logs_from(ctx.message.channel)
                    await asyncio.sleep(5)
                    await self.bot.delete_message(delete_too)
                    await self.bot.delete_message(ctx.message)
                    async for message in logs:
                        try:
                            deleted += 1
                            await self.bot.delete_message(message)
                            if deleted == times:
                                break
                            if deleted == 5:
                                await asyncio.sleep(0.1)
                        except:
                            pass
def setup(bot):
    m_c = ModCommands(bot)
    bot.add_cog(m_c)
