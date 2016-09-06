from discord.ext import commands
import discord.utils

#
# This is a modified version of checks.py, originally made by Rapptz
#
#                 https://github.com/Rapptz
#          https://github.com/Rapptz/RoboDanny/tree/async
#

def is_owner_check(ctx):
    """Checks if author id matches the owner's"""
    return ctx.message.author.id == "146719621368643584"

def is_owner():
    return commands.check(is_owner_check)

def is_staff_check(ctx):
    """Checks if the staff role is in the author's role list"""
    return {"simsvip staff"} & {role.name.lower() for role in ctx.message.author.roles}

def is_staff():
    return commands.check(is_staff_check)

def is_servoRepair_check(ctx):
    """Checks if the repair role is in the author's role list"""
    return {"servo repairman"} & {role.name.lower() for role in ctx.message.author.roles}

def is_servoRepair():
    return commands.check(is_servoRepair_check)

def is_mod_check(ctx):
    """Checks if the repair and staff roles are in the author's role list"""
    return {"simsvip staff", "servo repairman"} & {role.name.lower() for role in ctx.message.author.roles}

def is_mod():
    return commands.check(is_mod_check)
