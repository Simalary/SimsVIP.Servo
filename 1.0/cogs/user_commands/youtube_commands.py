from discord.ext import commands as u_YTcmds
import discord.utils

import urllib.request
import urllib.parse
import re
import random

class User_YTcmds:
    """User commands that search for youtube videos."""

    def __init__(self, bot):
        self.bot = bot

    @u_YTcmds.command(pass_context=True, name='youtube', aliases=['YouTube', 'YOUTUBE', 'Youtube'])
    async def yt(self, ctx, *, query):
        query_string = urllib.parse.urlencode({'search_query' : query})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + (query_string))
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        video = ("http://www.youtube.com/watch?v=" + search_results[random.randint(1,10)])
        await self.bot.say('{}, {}'.format(ctx.message.author.mention, video))


    @u_YTcmds.command(pass_context=True, name='youtube_pop', aliases=['YouTube_Pop', 'YouTube_pop', 'YOUTUBE_POP', 'Youtube_pop', 'Youtube_Pop'])
    async def yt_pop(self, ctx, *, query):
        query_string = urllib.parse.urlencode({'search_query' : query})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + (query_string))
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        video = ("http://www.youtube.com/watch?v=" + search_results[0])
        await self.bot.say('{}, {}'.format(ctx.message.author.mention, video))

def setup(bot):
    yt_cmds = User_YTcmds(bot)
    bot.add_cog(yt_cmds)
