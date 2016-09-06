import discord.utils

extensions_list = ['cogs.utils.logging',
                  'cogs.utils.user_files',
                  'cogs.utils.member_changes',
                  'cogs.utils.extension_checker',
                  'cogs.utils.cleverbot',

                  'cogs.misc_commands',
                  'cogs.mod_commands',
                  'cogs.owner_commands',

                  'cogs.user_commands.info_commands',
                  'cogs.user_commands.points_command',
                  'cogs.user_commands.misc_commands',
                  'cogs.user_commands.youtube_commands',

                  'cogs.user_commands.game_commands.rock_paper_scissors',
                  'cogs.user_commands.game_commands.gambling',

                  'cogs.user_commands.TaylorSwift_commands.songs_command']

class extensionChecker:
    """Loads extensions"""

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    eC = extensionChecker(bot)
    bot.add_cog(eC)
