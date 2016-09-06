from discord.ext import commands as u_MiscCMDs
import discord.utils

import sys
import unicodedata
import asyncio
import random

class User_MiscCommands:
    """User commands that are random."""

    def __init__(self, bot):
        self.bot = bot

    @u_MiscCMDs.command(pass_context=True, name='source', aliases=['Source', 'SOURCE'])
    async def _botsource(self, ctx):
        """Returns the source code link for the bot."""
        source_link = "https://github.com/Simalary/SimsVIP.Servo"
        await self.bot.say('{0.message.author.mention}, my source code is available at <{1}>.'.format(ctx, source_link))

    @u_MiscCMDs.command(pass_context=True, name='choose', aliases=['Choose', 'CHOOSE'])
    async def choose(self, ctx):
        """Takes words or sentences seperated by "; "
           and picks a random item after."""
        if len(str(ctx.message.content)) < 9:
                await self.bot.say('{}, the usage is **!choose Option 1; Option 2; Option 3**, until you run out of options.'.format(ctx.message.author.mention))
        else:
                choices = str(ctx.message.content[8:])
                if '; ' not in choices:
                        await self.bot.say('{}, the usage is **!choose Option 1; Option 2; Option 3**, ntil you run out of options.'.format(ctx.message.author.mention))
                else:
                        options = choices.split('; ')
                        await self.bot.say('{}, I choose: **{}**.'.format(ctx.message.author.mention,random.choice(options)))

    @u_MiscCMDs.command(pass_context=True, name='8ball', aliases=['8BALL'])
    async def ball(self, ctx, question):
        """Picks a random 8ball answer for a yes or no question."""
        if ctx.message.author == self.bot.user:
                return
        answers = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes, definitely.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                       'Reply hazy, try again.', 'Ask again later.', 'Better not tell you know.', 'Cannot predict now.', 'Concentrate and try again.',
                       'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'The chances are the same as you buying every pack, so not likely.']
        await self.bot.say('{}, {}'.format(ctx.message.author.mention, random.choice(answers).lower()))

    @u_MiscCMDs.command(pass_context=True, name='randompack', aliases=['pack', 'PACK', 'RandomPack', 'Pack', 'RAONDOMPACK'])
    async def randompack(self, ctx):
        """Returns a random SP, GP, or EP from The Sims 4 to the user."""
        if ctx.message.author == self.bot.user:
                return
        packs = ['Get Together', 'Get to Work', 'City Life',
                       'Luxury Party Stuff', 'Perfect Patio Stuff', 'Cool Kitchen Stuff', 'Spooky Stuff', 'Movie Hangout Stuff', 'Romantic Garden Stuff', 'Kids Room Stuff', 'Backyard Stuff',
                       'Outdoor Retreat', 'Spa Day', 'Dine Out']
        pack = random.choice(packs)
        if pack == 'City Life':
                await self.bot.say('{}, you should buy **{}** when it comes out.'.format(ctx.message.author.mention, pack))
        else:
                await self.bot.say('{}, you should buy **{}**.'.format(ctx.message.author.mention, pack))

    @u_MiscCMDs.command(pass_context=True, name='secret', aliases=['SECRET', 'Secret'])
    async def _miscSECRET(self, ctx):
        """A secret command that will PM the author."""
        PM = 'WOAH \U0001F62E! You found the secret command, you\'re cool. \n\n(P.S. - Don\'t tell anyone about it.)'
        await self.bot.send_message(ctx.message.server.get_member(ctx.message.author.id), PM)
        await self.bot.delete_message(ctx.message)

    @u_MiscCMDs.command(pass_context=True, name='plumbob', aliases=['Plumbob', 'PLUMBOB'])
    async def _misc_IMGplumbob(self, ctx):
        """Returns a gif of the plumbob from the Sims 4."""
        await self.bot.say('{}, http://i.imgur.com/q8xJsJQ.gif'.format(ctx.message.author.mention))

    @u_MiscCMDs.command(pass_context=True, name='changelog', aliases=['Changelog', 'ChangeLog', 'CHANGELOG'])
    async def changelog(self, ctx, opt=None):
        """Gets the bots changelog.

           If a subcommand is "beta", the old changelog for
           the beta is returned."""
        if ctx.message.author == self.bot.user:
                return
        if opt is None:
            await self.bot.say('**Update: 9/5/16   //   1.0**\n\nServo is finally out of the beta stage!\n\nChanges & Fixes:\n  - The new format and tech information:\n    - Servo now uses the cogs function of discord.py, making everything organized, and tidy.\n    - Servo now supports discord.py plugins! Basically, these are plugins that can easily be added or removed, and Servo will still run if they don\'t work.\n      - This allows easily editing the plugin, and reloading it, instead of restarting Servo completely!\n      - If you guys know Python, you can make plugins too! Ask me through a PM for information!\n    - I have recoded about 75% of Servo, allowing a slight performance boost.\n    - Throughout Servo\'s code, I have added documentation notes, these are little tidbits of information to explain a specific function.\n    - Servo now has a new checks system. This allows checking for roles, IDs, and other information of users, to see who can use a command.\n      - This allows easier management of staff and owner commands.\n  - Command changes and notes:\n    - The `!name` command can now only be done by me.\n    - The `!chat` command has been removed, since it has never been used. The method of mentioning Servo still works with Cleverbot functionality.\n    - The `!throw` command now allows you to specify another user if you wish, and then Servo will attack that user.\n    - The `!help` command is still disabled until further notice.\n    - When you use any command that allows getting other user stuff, you can now get Servo\'s info.\n      - Before, this wouldn\'t work, because of the Cleverbot functionality, but it now has been fixed.\n  - New commands:\n      - `!ts` is a command based around Taylor Swift. The current option is `song`, which returns a random Taylor Swift song you should listen to.\n      - `!servo` is a command that allows you to see if Servo is running.\n        - Try in #general and then #laboratory-and-spam - you\'ll get different results.')
        elif opt == "beta".lower():
            await self.bot.say('**Update: 7/14/16   //   0.1.1** \n\n- Servo will no longer be rude if you make a mistake or lose in gambling. \n - With gambling, you can no longer gamble a negative amount. \n   - Wouldn\'t that just make you lose more anyway, or would they have to give you money? \U0001F914 \n\n**Update: 7/14/16   //   0.1.1.102** \n\n- A new command `!randompack` (or it\'s alias `!pack`) will let Servo give you a suggestion on what pack for The Sims 4 you should buy. \n   - Isn\'t it nice to always have someone suggest something fun to buy? \n      - Especially when you\'re bored with what you have now?\n         - Because you\'re so selfish and aren\'t thankful for what you have?\n         - Sorry, got too excited. \n\n**Update: 7/14/16   //   0.1.1.202** \n\n- Every command now has capitalized aliases, allowing the first letter to be capitalized, the merged words\' first letter (like YouTube), or the whole command. \n   - You\'re welcome you quick typers that speal most thimgs wronj, or the ones who can\'t let LEt Go oF the ShiFT key aT THe riGHT TImE.\n\n**Update: 7/15/16   //   0.1.2.102** \n\n- Servo now logs the chat, and keeps track of who said it, and in which channel. \n   - We\'re onto you guys, we\'re watching. \n-You can now use `!changelog` to look at the changelog. \n   - Wow, so many useless changes every time! \n-Want to get hit with something? Use `!throw` and watch out!')
            await self.bot.say('**Update: 7/15/16   //   0.1.2.202** \n\n- Fixed a small issue that would cause Servo to create a blank log, alongside a complete one. \n   - We\'re watching you guys still, don\'t think we\'ll ever stop. \n\n**Update: 7/15/16   //   0.1.2.301** \n\n- Fixed a formatting error in the changelog that would cause the headers to not be bolded. \n\n- Changed the formatting of the log file neames to M - D - Y, instead of D - M- Y. \n\n**Update: 7/15/16   //   0.1.2.402** \n\n - Added Backyard Stuff into the responses for `!pack`.')
            await self.bot.say('**Update: 7/15/16   //   0.1.2.506** \n\n- Staff can now use the new mod command, `!setgame` to choose which game Servo is currently playing. \n   - This can be cleared using `!setgame none` or `!setgame clear`. \n\n**Update: 7/15/16   //   0.1.2.604** \n\n- When staff members use the `!setgame` command, there will now be a reply indicating completion, and then will be deleted shortly after. \n\n**Update: 8/1/16   //   0.1.2.708** \n\n - Corrected the typo of \'Luxary\' to \'Luxury\' from the `!pack` command. \n - The changelog order is now reversed, showing the more recent updates at the bottom. \n    - It makes sense because that\'s what you would see at first, right? \n\n**Update: 8/26/16   //   0.1.3.102** \n\n- Added commands for getting info: `!infobot`, `!infoserver`, `!infouser`. \n   - `!infobot` displays information about Servo. \n   - `!infoserver` displays server information. \n   - `!infouser` displays info about the user who commits the command. \n   - None of those descriptions were useful. *shrugs* \n- Added `!version` (or `!botversion`) to show Servos\'s current version. \n- Other things. \n   - Some secret things. \n       - Things I\'ve been planning for a while. \U0001F60F')
            await self.bot.say('**Update: 8/27/16   //   0.1.4.608** \n\n- There is a new negative response when answering yes or no questions with `!8ball`. \n- A new **secret** command. *Hint, hint.* \n   - If you find this out, do not tell anybody. \n      - You will be punished and killed.\n         - Ahem, sorry. Got a little too carried away. \n\n**Update: 8/27/2016   //   0.1.5.809** \n\nPretty big update today:\n\n- Servo now notifies the server of username, and nickname changes.\n- Member usernames and IDs are now being stored.\n   - Maybe for secret stuff? Who knows? \U0001F60F \n- Added `!choose`. (Usage like `!choose <option1>;<option2>`) This allows Servo to make hard decisions for you. \n   - There is no limit to the amount of choices. Make sure to follow the formatting perfectly.\n- The `!help` command has been removed until further notice. \n\n**Update: 8/28/2016   //   0.1.5.909** \n\nSmall update this time: \n\n- When logging, Servo will now remove any emojis in the user\'s name, or message. This will now reduce the amount of "invalid character" errors, and log more chat.\n   - Yeah, we are still watching you guys.\n   - There is still a bug that that will cause "b\'" and "\'" to wrap around the user\'s name and message inside the logs, and the user list files. This will be solved soon.')
            await self.bot.say('\n**Update: 9/1/16   //   0.1.6.101**\n\nA big update this time around:\n\nChanges:\n - When using `!infouser`, you can now request the info of another user by mentioning them. (Example: `!infouser @Simalary®️ (Chris)#6397`)\n - Staff can now use `!name <username>` to set Servo\'s new username. (Example: `!name Servo (Alpha)`)\n    - If the username cannot be changed at that time, Servo will send an error saying so.\n    - The command will only run if Servo is running on my PC.\n - Some secret stuff has been added. \U0001F60F\nFixes:\n - Fixed some nice try mesages that were missing smirks. \n\n**Update: 9/2/16   //   0.1.6.306**\n\nChanges & Additions:\n\n - \'City Life\' has been added to a response for the `!pack` command.\n    - The response will say \'@Servo (Beta)#6771, you should buy **City Life** when it comes out.\', since the pack isn\'t out yet. Duh.\n - Added `!plumbob`. This will have Servo send you a cute gif of the plumbob from the Sims 4.\n\nFixes:\n\n - The logs will correctly show Servo\'s messages, instead of mixing the channel and the message around.\n    - It\'s not opposite day.\n       - Wait, does that mean it is opposite day?\n - The `!choose` command is more specific now.\n    - The usage is `!choose Option 1; Option 2; Option 3`, until you run out of choices.\n    - **The formatting is specific**, use "; ", not ";" when seperating your choices.')
            await self.bot.say(' \n**Update: 9/2/16   //   0.1.6.307**\n\nChanges:\n - When getting another user\'s info with `!infouser @USER#0000`, the response from Servo will now say you are getting **that** person\'s info. \n\n**Update: 9/3/16   //   0.1.7.102**\n\nChanges & Additions:\n - There is a new feature called **SimPoints**. Every user will have points, as of right now, everyone has 500.\n   - The default amount for when someone joines the server is 500.\n   - At the moment, there is no way to gain or lose points.\n   - To check your amount of points, you may use `!infouser` or `!points`.\n      - You can see another user\'s points by using `!infouser @USER#0000` or `!points @USER#0000`.')
        else:
            await self.bot.say('{}, if you want the old beta changelog, type `!changelog beta`. If you want the current changelog, type `!changelog`.')

    @u_MiscCMDs.command(pass_context=True, name='servo', aliases=['Servo', 'SERVO'])
    async def _miscServo(self, ctx):
        """Tells the user the bot is here, and then makes a joke
           about them freaking out, when he is the one who freaks out"""
        if ctx.message.channel.id == "132432812056772608":
            await self.bot.say('{0.message.author.mention}, you needed me?')
        else:
            await self.bot.say('{0.message.author.mention}, I\'m here! I\'m running! DON\'T FREAK OUT. CALM! AHHHHHH!'.format(ctx))
            await asyncio.sleep(1.5)
            await self.bot.say('{0.message.author.mention}, OMG! AHHHHHHHHHHHHHHH! HELP!'.format(ctx))
            await asyncio.sleep(1.5)
            await self.bot.say('{0.message.author.mention}, OH MY GOSH! HELP!'.format(ctx))
            await asyncio.sleep(3)
            await self.bot.say('{0.message.author.mention}, I\'m calm.'.format(ctx))

    @u_MiscCMDs.command(pass_context=True, name='throw', aliases=['Throw', 'THROW'])
    async def _miscThrow(self, ctx, member : discord.Member=None):
        """Throws an item at the specified user. If no user
           is given, the bot will attack the message author."""
        if member is None:
            objects_first = ['*Throws a pie at*', '*Throws a shoe at*', 'A piece of poop hits', 'A rock hits', '*Throws a hammer at*', '*Tosses a computer at*', 'Throws a red slushie at*']
            name_middle = ['*Hits {} with a boulder.*'.format(ctx.message.author.mention), '*Wrecks {} with a wrecking ball.*'.format(ctx.message.author.mention)]
            objects_last = ['{} gets burned with a flame thrower.'.format(ctx.message.author.mention), '{} is hit by a flying poop.'.format(ctx.message.author.mention), '*Hits {} with a phone*.'.format(ctx.message.author.mention)]
            guess = random.randint(1, 100)
            if (guess > 0) and (guess < 25):
                    await self.bot.say('{}  {}'.format(random.choice(objects_first), ctx.message.author.mention))
            elif (guess > 25) and (guess < 60):
                    await self.bot.say('{}'.format(random.choice(name_middle)))
            elif (guess > 60) and (guess < 100):
                    await self.bot.say('{}'.format(random.choice(objects_last)))
        else:
            objects_first = ['*Throws a pie at*', '*Throws a shoe at*', 'A piece of poop hits', 'A rock hits', '*Throws a hammer at*', '*Tosses a computer at*', 'Throws a red slushie at*']
            name_middle = ['*Hits {} with a boulder.*'.format(member.mention), '*Wrecks {} with a wrecking ball.*'.format(member.mention)]
            objects_last = ['{} gets burned with a flame thrower.'.format(member.mention), '{} is hit by a flying poop.'.format(member.mention), '*Hits {} with a phone*.'.format(member.mention)]
            guess = random.randint(1, 100)
            if (guess > 0) and (guess < 25):
                    await self.bot.say('{}  {}'.format(random.choice(objects_first), member.mention))
            elif (guess > 25) and (guess < 60):
                    await self.bot.say('{}'.format(random.choice(name_middle)))
            elif (guess > 60) and (guess < 100):
                    await self.bot.say('{}'.format(random.choice(objects_last)))

def setup(bot):
    U_MC = User_MiscCommands(bot)
    bot.add_cog(U_MC)
