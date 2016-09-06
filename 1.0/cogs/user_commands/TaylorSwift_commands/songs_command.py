from __future__ import print_function

from discord.ext import commands as ts_SongCommand
import discord.utils

import sys
import unicodedata
import asyncio
import random

Songs = ["Tim McGraw", "Picture to Burn", "Teardrops on My Guitar", "A Place in This World", "Cold As You", "The Outside",
         "Tied Together With a Smile", "Stay Beautiful", "Should've Said No", "Mary's Song", "Our Song",
         "I'm Only Me When I'm With You", "Invisible", "A Perfectly Good Heart",

         "Jump Then Fall", "Untouchable", "Forever and Always (piano)", "Come In With The Rain", "SuperStar", "The Other Side of the Door",
         "Fearless", "Fifteen", "Love Story", "White Horse", "You Belong With Me", "Breathe", "Tell Me Why", "You're Not Sorry",
         "The Way I Loved You", "Forever and Always", "The Best Day", "Change",

         "Mine", "Sparks Fly", "Back to December", "Speak Now", "Dear John", "Mean", "The Story of Us",
         "Never Grow Up", "Enchanted", "Better Than Revenge", "Innocent", "Haunted", "Last Kiss", "Long Live",
         "Ours", "If This Was A Movie", "Superman",

         "State of Grace", "Red", "Treacherous", "I Knew You Were Trouble", "All Too Well", "22", "I Almost Do", "We Are Never Ever Getting Back Together",
         "Stay Stay Stay", "The Last Time", "Holy Ground", "Sad Beautiful Tragic", "The Lucky One", "Everything Has Changed", "Starlight", "Begin Again",
         "The Moment I Knew", "Come Back, Be Here", "Girl At Home",

         "Welcome To New York", "Blank Space", "Style", "Out of the Woods",
         "All You Had To Do Was Stay", "Shake it Off", "I Wish You Would", "Bad Blood", "Wildest Dreams", "How You Get the Girl", "This Love",
         "I Know Places", "Clean",
         "Wonderland", "You Are In Love", "New Romantics", "Safe and Sound", "Eyes Open", "Today Was a Fairytale", "Sweeter Than Fiction"]

class TaylorSwift_SongsCommand:
    """User command that picks a random Taylor Swift Song."""

    def __init__(self, bot):
        self.bot = bot

    @ts_SongCommand.command(pass_context=True, name='ts', aliases=['TS'])
    async def _tsSONG(self, ctx, *, option=None):
        if option is None:
            await self.bot.say('{0.message.author.mention}, you need to specify an option for the TS command. (Example: **!ts song**)'.format(ctx))
        elif option == "song".lower():
            rand_song = random.choice(Songs)
            await self.bot.say('{0.message.author.mention}, you should listen to **{1}**.'.format(ctx, rand_song))
        else:
            await self.bot.say('{0.message.author.mention}, the available options are: `song`.'.format(ctx))


def setup(bot):
    ts_sc = TaylorSwift_SongsCommand(bot)
    bot.add_cog(ts_sc)
